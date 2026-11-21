"""Macros for the InvenTree website.

Zensical loads this module (via the 'macros' plugin) when rendering any page
which sets 'render_macros: true' in its front matter. Zensical re-executes
this file for every rendered page, and does not expose the page list to
macros, so site data is read directly from disk.
"""

import posixpath
import re
import subprocess
from functools import cache
from pathlib import Path

import yaml

here = Path(__file__).parent
docs_dir = here.joinpath('docs')
plugin_dir = docs_dir.joinpath('plugins')
publisher_dir = here.joinpath('publishers')
data_dir = here.joinpath('data')

# Pages in the plugins directory which are not plugin entries
PLUGIN_INDEX_PAGES = {'index.md', 'community.md', 'tags.md', 'categories.md', 'publishers.md'}

FRONT_MATTER = re.compile(r'^---\s*\n(.*?)\n---\s*\n?', re.S)


def read_markdown(path: Path) -> tuple[dict, str]:
    """Split a markdown file into (front matter, body)."""
    text = path.read_text(encoding='utf-8')
    match = FRONT_MATTER.match(text)

    if not match:
        return {}, text

    return yaml.safe_load(match.group(1)) or {}, text[match.end() :]


def load_yaml(filename: str) -> dict:
    """Load a data file from the 'data' directory."""
    with open(data_dir.joinpath(filename), encoding='utf-8') as f:
        return yaml.safe_load(f) or {}


def slugify(value: str) -> str:
    """Convert a tag or category into an anchor (matches the old Jekyll slugify)."""
    return re.sub(r'[^a-z0-9]+', '-', str(value).lower()).strip('-')


def as_list(value) -> list[str]:
    """Tags and categories may be a list, a comma separated string, or empty."""
    if not value:
        return []
    if isinstance(value, str):
        value = value.split(',')
    return [str(v).strip() for v in value if str(v).strip()]


def excerpt(body: str, length: int = 200) -> str:
    """Return the first paragraph of a markdown body as plain text."""
    in_fence = False

    for block in re.split(r'\n\s*\n', body):
        block = block.strip()

        if block.startswith('```'):
            in_fence = block.count('```') % 2 == 1
            continue
        if in_fence:
            in_fence = '```' not in block
            continue
        if not block or block.startswith(('#', '!', '<', '|', '-', '*', '>', '[!')):
            continue

        text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', block)  # images
        text = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', text)  # links
        text = re.sub(r'<[^>]+>', '', text)  # html tags
        text = re.sub(r'[`*_]', '', text)
        text = ' '.join(text.split())

        if len(text) > length:
            text = text[:length].rsplit(' ', 1)[0] + '…'
        return text

    return ''


@cache
def git_dates(*directories: str) -> dict[str, str]:
    """Return the date of the last commit which added or modified each file (by filename).

    Pure renames are ignored, so that moving files does not change their date.
    """
    try:
        result = subprocess.run(
            ['git', 'log', '-M', '--diff-filter=AM', '--format=%x00%cs', '--name-only', '--', *directories],
            cwd=here,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return {}

    dates = {}

    for entry in result.stdout.split('\x00')[1:]:
        date, *files = entry.strip().splitlines()
        for filename in filter(None, files):
            dates.setdefault(Path(filename).name, date)

    return dates


@cache
def get_plugins() -> list[dict]:
    """Return all plugin entries, sorted by name."""
    # Plugin entries were stored in '_repo' before the move to Zensical
    dates = git_dates('docs/plugins', '_repo')
    plugins = []

    for path in plugin_dir.glob('*.md'):
        if path.name in PLUGIN_INDEX_PAGES:
            continue

        meta, body = read_markdown(path)
        meta['slug'] = path.stem
        meta['src'] = f'plugins/{path.name}'
        meta['categories'] = as_list(meta.get('categories'))
        meta['tags'] = as_list(meta.get('tags'))
        meta['excerpt'] = excerpt(body)
        meta['body'] = body
        meta['last_modified'] = dates.get(path.name)
        plugins.append(meta)

    return sorted(plugins, key=lambda p: str(p.get('name', p['slug'])).lower())


@cache
def get_publishers() -> dict[str, dict]:
    """Return all publishers, keyed by (lowercase) short name."""
    publishers = {}

    for path in publisher_dir.glob('*.yml'):
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f) or {}

        short_name = str(data.get('short_name') or path.stem)
        data['short_name'] = short_name
        data['anchor'] = short_name.lower()
        data['file'] = path.stem
        publishers[short_name.lower()] = data

    return publishers


def get_posts(blog: str = 'blog') -> list[dict]:
    """Return all posts for a blog, newest first."""
    posts = []

    for path in docs_dir.joinpath(blog, 'posts').glob('*.md'):
        meta, _ = read_markdown(path)
        meta['src'] = f'{blog}/posts/{path.name}'
        posts.append(meta)

    return sorted(posts, key=lambda p: str(p.get('date')), reverse=True)


def publisher_of(plugin: dict) -> dict:
    """Return the publisher record for a plugin (with a fallback for unknown authors)."""
    author = str(plugin.get('author') or '')
    return get_publishers().get(
        author.lower(), {'short_name': author, 'github': author, 'anchor': author.lower()}
    )


def define_env(env):
    """Register variables and macros for the macros plugin."""
    page = env.variables.get('page')
    page_dir = posixpath.dirname(page.path) if page else ''

    def link(target: str) -> str:
        """Link target for a docs-relative source path, from the current page.

        Zensical resolves both Markdown links and src/href attributes in raw HTML
        relative to the source file, so this is used for both.
        """
        path, _, anchor = target.partition('#')
        out = posixpath.relpath(path, page_dir or '.')
        return f'{out}#{anchor}' if anchor else out

    def author_link(publisher: dict, size: int = 20) -> str:
        github = publisher.get('github') or publisher['short_name']
        return (
            f'[![](https://github.com/{github}.png?size={size * 2})'
            f'{{ .iv-avatar width="{size}" height="{size}" loading="lazy" }} '
            f'{publisher["short_name"]}]'
            f'({link("plugins/publishers.md#" + publisher["anchor"])})'
        )

    def chips(plugin: dict) -> str:
        out = [
            f'[{c}]({link("plugins/categories.md#" + slugify(c))}){{ .iv-chip .iv-chip--category }}'
            for c in plugin['categories']
        ]
        out += [
            f'[{t}]({link("plugins/tags.md#" + slugify(t))}){{ .iv-chip }}'
            for t in plugin['tags']
        ]
        return ' '.join(out)

    def card(plugin: dict) -> str:
        lines = [
            f'-   __[{plugin.get("name", plugin["slug"])}]({link(plugin["src"])})__',
            '',
            f'    {author_link(publisher_of(plugin))}',
            '',
            '    ---',
            '',
        ]
        if plugin['excerpt']:
            lines += [f'    {plugin["excerpt"]}', '']
        if plugin_chips := chips(plugin):
            lines += [f'    {plugin_chips}', '']
        return '\n'.join(lines)

    def cards(plugins: list[dict]) -> str:
        if not plugins:
            return '*No plugins found.*'
        return '\n'.join(
            ['<div class="grid cards" markdown>', '', *map(card, plugins), '</div>']
        )

    @env.macro
    def plugin_cards(limit: int = 0, recent: bool = False) -> str:
        """Render a grid of plugin cards."""
        plugins = get_plugins()
        if recent:
            plugins = sorted(plugins, key=lambda p: p['last_modified'] or '', reverse=True)
        if limit:
            plugins = plugins[:limit]
        return cards(plugins)

    @env.macro
    def plugin_index(field: str) -> str:
        """Render an index of plugins grouped by 'tags' or 'categories'."""
        groups: dict[str, tuple[str, list]] = {}

        for plugin in get_plugins():
            for value in plugin[field]:
                label, members = groups.setdefault(slugify(value), (value, []))
                members.append(plugin)

        ordered = sorted(groups.items(), key=lambda g: g[1][0].lower())

        out = [
            ' '.join(f'[{label}](#{slug}){{ .iv-chip }}' for slug, (label, _) in ordered),
            '',
        ]
        for slug, (label, members) in ordered:
            out += [f'## {label} {{ #{slug} }}', '', cards(members), '']
        return '\n'.join(out)

    @env.macro
    def publisher_list() -> str:
        """Render all publishers, with their plugins and blog posts."""
        team = {str(m['tag']).lower() for m in load_yaml('team.yml').get('team', [])}
        plugins = get_plugins()
        posts = get_posts('blog')
        out = []

        for key, pub in sorted(get_publishers().items(), key=lambda p: str(p[1].get('name', p[0])).lower()):
            github = pub.get('github') or pub['short_name']
            out += [
                f'## {pub.get("name", pub["short_name"])} {{ #{pub["anchor"]} }}',
                '',
                f'![](https://github.com/{github}.png?size=96){{ .iv-avatar .iv-avatar--large width="48" height="48" loading="lazy" }}',
                f'[<i class="ti ti-brand-github"></i> {github}](https://github.com/{github}){{ .iv-chip }}',
            ]
            if pub.get('website'):
                out += [f'[<i class="ti ti-world"></i> Website]({pub["website"]}){{ .iv-chip }}']
            if key in team:
                out += [f'[<i class="ti ti-shield-check"></i> Team Member]({link("about/team.md")}){{ .iv-chip .iv-chip--team }}']
            out += ['']
            if pub.get('tagline'):
                out += [f'> {pub["tagline"]}', '']

            own_plugins = [p for p in plugins if str(p.get('author', '')).lower() == key]
            if own_plugins:
                out += ['**Plugins**', '']
                out += [f'- [{p.get("name", p["slug"])}]({link(p["src"])})' for p in own_plugins]
                out += ['']

            own_posts = [p for p in posts if key in (str(a).lower() for a in p.get('authors', []))]
            if own_posts:
                out += ['**Blog Posts**', '']
                out += [f'- {p["date"]} – [{p.get("title")}]({link(p["src"])})' for p in own_posts]
                out += ['']

        return '\n'.join(out)

    @env.macro
    def feature_cards(*groups: str, extend: bool = False) -> str:
        """Render a single grid of feature cards from one or more groups in data/functions.yml."""
        data = load_yaml('functions.yml')
        out = ['<div class="grid cards" markdown>', '']

        for item in (item for group in groups or ('general',) for item in data.get(group, [])):
            out += [
                f'-   <i class="ti {item.get("icon", "ti-point")} iv-card-icon"></i> __{item["title"]}__',
                '',
                '    ---',
                '',
                f'    {item["text"]}',
                '',
            ]
            if extend and item.get('extend'):
                out += [f'    {item["extend"]}', '']
            if item.get('link'):
                out += [f'    [<i class="ti ti-arrow-right"></i> Learn more]({item["link"]})', '']

        out += ['</div>']
        return '\n'.join(out)

    @env.macro
    def stats() -> str:
        """Render the project statistics (updated daily by .github/get_stats.py)."""
        items = []

        for item in load_yaml('stats.yml').get('stats', []):
            items.append(
                '<div class="iv-stat">'
                f'<i class="ti {item["icon"]}"></i>'
                f'<span class="iv-stat__number">{int(item["number"]):,}</span>'
                f'<span class="iv-stat__label">{item["name"]}</span>'
                '</div>'
            )

        return f'<div class="iv-stats">{"".join(items)}</div>'

    @env.macro
    def team_members() -> str:
        """Render the active team members from data/team.yml."""
        out = []

        for member in load_yaml('team.yml').get('team', []):
            links = ' '.join(f'[{l["text"]}]({l["link"]}){{ .iv-chip }}' for l in member.get('links', []))
            out += [
                f'### ![](https://github.com/{member["tag"]}.png?size=96){{ .iv-avatar .iv-avatar--large width="48" height="48" loading="lazy" }} {member["name"]} ({member["tag"]}) {{ #{str(member["tag"]).lower()} }}',
                '',
                member.get('text', ''),
                '',
                links,
                '',
            ]

        return '\n'.join(out)

    @env.macro
    def team_intro() -> str:
        return load_yaml('team.yml').get('text', '')

    @env.macro
    def gallery(directory: str, per_page: int = 1) -> str:
        """Render an image carousel from all images in docs/assets/<directory>."""
        images = sorted(
            p.name
            for p in docs_dir.joinpath('assets', directory).iterdir()
            if p.suffix.lower() in {'.png', '.jpg', '.jpeg', '.gif', '.webp'}
        )
        slides = ''.join(
            f'<li class="splide__slide"><img src="{link(f"assets/{directory}/{name}")}" alt="" loading="lazy"></li>'
            for name in images
        )
        return (
            f'<section class="splide iv-gallery" data-per-page="{int(per_page)}" aria-label="Screenshots">'
            f'<div class="splide__track"><ul class="splide__list">{slides}</ul></div>'
            '</section>'
        )
