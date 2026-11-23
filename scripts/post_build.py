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
from datetime import timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

import markdown

here = Path(__file__).parent.parent
sys.path.insert(0, str(here))

import main  # noqa: E402

site_dir = here.joinpath('site')


def plain_text(text: str) -> str:
    """Render markdown and strip all HTML tags."""
    return re.sub(r'<[^>]+>', '', markdown.markdown(text))


def reformat_feed_dates(feed: Path) -> int:
    """Rewrite dates form RSS to Atom (ISO 8601)."""
    pattern = re.compile(
        r'(<(?:pubDate|lastBuildDate)\b[^>]*>)([^<]*)(</(?:pubDate|lastBuildDate)\s*>)'
    )
    content = feed.read_text(encoding='utf-8')

    def replace(match: re.Match[str]) -> str:
        date = parsedate_to_datetime(match.group(2).strip())
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return f'{match.group(1)}{date.isoformat(sep=" ", timespec="seconds")}{match.group(3)}'

    content, reformatted = pattern.subn(replace, content)
    feed.write_text(content, encoding='utf-8')
    return reformatted


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
        count = reformat_feed_dates(dst)
        print(f'Copied {src} -> {dst}; Reformatted {count} dates in target')


if __name__ == '__main__':
    if not site_dir.exists():
        sys.exit(f"'{site_dir}' does not exist - run 'zensical build' first")

    build_plugins_json()
    copy_legacy_feeds()
