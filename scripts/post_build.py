"""Generate additional output files after 'zensical build'.

- plugins.json: machine readable plugin list (same schema as the old Jekyll site)
- blog/feed.atom, news/feed.atom: legacy feed URLs, kept for existing subscribers
- <page>.html: redirects from the old Jekyll page URLs (still linked from the docs)
"""

import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown

here = Path(__file__).parent.parent
sys.path.insert(0, str(here))

import main  # noqa: E402

site_dir = here.joinpath('site')


def plain_text(text: str) -> str:
    """Render markdown and strip all HTML tags."""
    return re.sub(r'<[^>]+>', '', markdown.markdown(text))


def build_plugins_json():
    """Write the plugin and publisher list to plugins.json."""
    plugins = {}
    publishers = {}

    for plugin in main.get_plugins():
        # Keys are the old Jekyll URLs (which now redirect), kept for compatibility
        plugins[f'/{plugin["author"]}/{plugin["slug"]}'] = {
            'name': plugin.get('name'),
            'author': plugin.get('author'),
            'url': f'/plugins/{plugin["slug"]}/',
            'last_modified': plugin['last_modified'],
            'open_source': plugin.get('open_source'),
            'license': plugin.get('license'),
            'stable': plugin.get('stable'),
            'maintained': plugin.get('maintained'),
            'pypi': plugin.get('pypi'),
            'package_name': plugin.get('package_name'),
            'links': {
                key: plugin.get(key)
                for key in ('website', 'issue_tracker', 'github', 'gitlab', 'source')
            },
            'categories': plugin['categories'],
            'tags': plugin['tags'],
            'content_txt': plain_text(plugin['body']),
            'content': plugin['body'],
        }

    for pub in main.get_publishers().values():
        tagline = pub.get('tagline', '')
        publishers[f'/{pub["file"]}'] = {
            'short_name': pub['short_name'],
            'name': pub.get('name'),
            'github': pub.get('github'),
            'website': pub.get('website'),
            'url': f'/plugins/publishers/#{pub["anchor"]}',
            'content_txt': plain_text(tagline),
            'content': tagline,
        }

    output = site_dir.joinpath('plugins.json')
    output.write_text(
        json.dumps({'plugins': plugins, 'publishers': publishers}, indent=2),
        encoding='utf-8',
    )
    print(f'Wrote {len(plugins)} plugins and {len(publishers)} publishers to {output}')


def copy_legacy_feeds():
    """The old site served Atom feeds at <blog>/feed.atom - serve the RSS feed there instead."""
    for blog in ('blog', 'news'):
        src = site_dir.joinpath(blog, 'feed_rss_created.xml')
        dst = site_dir.joinpath(blog, 'feed.atom')
        shutil.copyfile(src, dst)
        print(f'Copied {src} -> {dst}')


# Old Jekyll pages were served at <page>.html - the 'redirects' plugin in mkdocs.yml
# only handles .md sources, so these are written here
LEGACY_HTML = {
    'about/team.html': '/about/team/',
    'blog.html': '/blog/',
    'categories.html': '/plugins/categories/',
    'contribute.html': '/contribute/',
    'demo.html': '/demo/',
    'deploy.html': '/deploy/',
    'digitalocean.html': '/deploy/#digitalocean',
    'extend/api.html': '/extend/#rest-api',
    'extend/app.html': '/extend/app/',
    'fund.html': '/fund/',
    'news.html': '/news/',
    'newsletter.html': '/newsletter/',
    'plugins.html': '/plugins/community/',
    'publishers.html': '/plugins/publishers/',
    'support.html': '/support/',
    'tags.html': '/plugins/tags/',
}


def write_legacy_redirects():
    """Write a redirect page for each old Jekyll .html URL."""
    for path, target in LEGACY_HTML.items():
        url = html.escape(target)
        output = site_dir.joinpath(path)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            '<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n<title>Redirecting...</title>\n'
            f'<link rel="canonical" href="{url}">\n'
            f'<meta http-equiv="refresh" content="0; url={url}">\n'
            '</head>\n<body>\n'
            f'You\'re being redirected to a <a href="{url}">new destination</a>.\n'
            '</body>\n</html>\n',
            encoding='utf-8',
        )
    print(f'Wrote {len(LEGACY_HTML)} legacy redirects')


if __name__ == '__main__':
    if not site_dir.exists():
        sys.exit(f"'{site_dir}' does not exist - run 'zensical build' first")

    build_plugins_json()
    copy_legacy_feeds()
    write_legacy_redirects()
