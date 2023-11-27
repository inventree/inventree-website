"""Script to update InvenTree release notes, extracted from GitHub API"""

import json
import os

import argparse
import requests
import textwrap


RELEASE_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..',
    'src',
    'pages',
    'releases',
))


def generate_release_page(release_data, overwrite=False) -> bool:
    """Generate output markdown file for a given release
    
    Any release older than 0.8.0 is ignored - before this, release notes were not automatically generated.
    """

    tag = release_data['tag_name']
    published = release_data['published_at'].split('T')[0]
    release_data['date'] = published
    body = release_data['body']
    name = release_data['name'] or tag

    # Split tag into major, minor, patch
    try:
        major, minor, patch = [int(x) for x in tag.split('.')]
    except ValueError:
        return False
    
    if major == 0 and minor < 8:
        # Ignore releases before 0.8.0
        return False
    
    output_filename = os.path.join(RELEASE_DIR, f'{tag}.md')

    if os.path.exists(output_filename) and not overwrite:
        print(f"Release file already exists: {output_filename}")
        return True
    
    with open(output_filename, 'w') as f:

        f.write("---\n")
        f.write(f"title: Release {name}\n")
        f.write(f"version: {tag}\n")
        f.write(f"date: {published}\n")
        f.write("---\n\n")

        f.write(f"## InvenTree Release {name}\n\n")
        f.write(f"**Release Date:** {published}\n\n")
        f.write(f"{body}\n")

    print(f"Generated release file: {output_filename}")
    return True


def get_release_data(ignore_cache=False):
    """Return InvenTree release information.

    - Compile an index page at /src/pages/releases/index.md
    - Each individual release is stored in /src/pages/releases/<version>.md
    """

    # Check if we have a cached version of the release data
    json_file = os.path.join(os.path.dirname(__file__), '_releases.json')

    if os.path.exists(json_file) and not ignore_cache:
        # Release information has been cached to file

        print("Loading release information from 'releases.json'")
        with open(json_file) as f:
            return json.loads(f.read())

    # Download release information via the GitHub API
    print("Fetching InvenTree release information from api.github.com:")
    releases = []

    # Keep making API requests until we run out of results
    page = 1

    while 1:
        url = f"https://api.github.com/repos/inventree/inventree/releases?page={page}&per_page=150"

        response = requests.get(url, timeout=30)
        assert response.status_code == 200

        data = json.loads(response.text)

        if len(data) == 0:
            break

        for item in data:
            releases.append(item)

        page += 1

    # Cache these results to file
    with open(json_file, 'w') as f:
        print("Saving release information to 'releases.json'")
        f.write(json.dumps(releases))

    return releases


def generate_index_page(releases: dict):
    """Generate an index page for the releases"""

    output_filename = os.path.join(RELEASE_DIR, 'index.mdx')

    data = f"""
    ---
    title: InvenTree Releases
    description: InvenTree Release Notes
    ---

    import Admonition from '@theme/Admonition';

    ## InvenTree Releases

    ### Version Numbering

    The InvenTree project follows a formalized release numbering scheme, according to the [semantic versioning specification](https://semver.org/).

    ### Stable Branch

    The head of the *stable* code branch represents the most recent stable tagged release of InvenTree.

    <Admonition type='tip' title='Stable Docker'>
        To pull down the latest *stable* release of InvenTree in docker, use `inventree/inventree:stable`
    </Admonition>
        
    ### Development Branch

    The head of the *master* code branch represents the "latest and greatest" working codebase. All features and bug fixes are merged into the master branch, in addition to relevant stable release branches.

    <Admonition type='tip' title='Development Docker'>
    To pull down the latest *development* version of InvenTree in docker, use `inventree/inventree:latest`
    </Admonition>

    ## Stable Releases

    Refer to the table below for information on stable releases of InvenTree.

    <table id='releases'>
    <thead>
    <tr>
    <th>Version</th>
    <th>Release Date</th>
    <th>Release Notes</th>
    </tr>
    </thead>
    <tbody>
    """

    # Sort releases by descending date
    releases = sorted(releases.values(), key=lambda it: it['date'], reverse=True)

    maj_min = None

    for release in releases:

        major, minor, patch = [int(x) for x in release['tag_name'].split('.')]

        if maj_min != f'{major}.{minor}':
            maj_min = f'{major}.{minor}'

            data += f"""
            <tr>
            <td colspan='3' class='release-header'>
            <strong>{major}.{minor}.x</strong>
            </td>
            </tr>
            """

        tag = release['tag_name']
        name = release['name']
        date = release['date']

        url = f'/releases/{tag}'

        data += f"""
        <tr>
            <td>{name}</td>
            <td>{date}</td>
            <td><a href='{url}'>Release Notes</a></td>
        </tr>
        """
    
    data += "</tbody></table>"

    with open(output_filename, 'w') as f:

        # Note: Dedent adds an extra leading newline character
        f.write(textwrap.dedent(data)[1:])

    print(f"Generated release index file: {output_filename}")


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Extract release notes from GitHub API')

    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing release files', default=False)
    parser.add_argument('--ignore-cache', action='store_true', help='Ignore cached release data', default=False)

    args = parser.parse_args()

    release_data = get_release_data(ignore_cache=args.ignore_cache)

    # Track releases by version
    releases = {}

    for release in release_data:
        if generate_release_page(release, overwrite=args.overwrite):
            tag = release['tag_name']
            releases[tag] = release
    
    # Generate an index page
    generate_index_page(releases)
