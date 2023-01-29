import json
import os
from pathlib import Path
from urllib.request import urlopen, Request

inp_project = os.environ.get('PROJECT')
inp_author = os.environ.get('AUTHOR')
file_name = Path(f'_repo/{inp_project}.md')
crowdin_projet_id = 452300

print(f'Collecting {inp_project} with {inp_author}...')

def get_data(url, key=None, default=0, auth=None):
  """Fetches data from remote endpoint"""
  httprequest = Request(url, headers={"Accept": "application/json"})

  if auth:
    httprequest.add_header("Authorization", f"Bearer {auth}")

  with urlopen(httprequest) as response:
    data = response.read().decode()
    data = json.loads(data)

  if key:
    data = data.get(key, default)

  return data

pypi_data = get_data(f'https://pypi.org/pypi/{inp_project}/json')

name = pypi_data['info']['name']
tagline = pypi_data['info']['summary']
author = inp_author or pypi_data['info']['author_email']
license = pypi_data['info']['license']
try:
  version = pypi_data['info']['version']
  stable = int(version.split('.')[0])>1
except:
  stable = False
bugtracker = pypi_data['info']['bugtrack_url'] or pypi_data['info']['project_urls'].get('Bug Tracker') or ''
homepage = pypi_data['info']['home_page'] or pypi_data['info']['project_urls'].get('Homepage')
keywords = pypi_data['info']['keywords']
readme = pypi_data['info']['description']

# Write data
file_name.write_text(
f"""---
name: {name}
author: {author}
license: {license}
open_source: true
stable: {stable}
maintained: true
pypi: true
package_name: {name}
github: {homepage}
gitlab:
source:
issue_tracker:{bugtracker}
website:
categories:
tags: {keywords}
---
{tagline}

{readme}
"""
)
