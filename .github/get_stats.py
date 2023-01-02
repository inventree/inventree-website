from enum import Enum
import json
import os
from pathlib import Path
from urllib.request import urlopen, Request

file_name = Path('_data/general/stats.yml')
github_project = "inventree/inventree"
crowdin_projet_id = 452300

class ReturnMode(Enum):
  data = 0
  header = 1

def get_data(url, key=None, default=0, mode: ReturnMode=ReturnMode.data, auth=None):
  """Fetches data from remote endpoint"""
  httprequest = Request(url, headers={"Accept": "application/json"})

  if auth:
    httprequest.add_header("Authorization", f"Bearer {auth}")

  with urlopen(httprequest) as response:
    if mode == ReturnMode.data:
      data = response.read().decode()
      data = json.loads(data)
    
    elif mode == ReturnMode.header:
      data = dict(response.headers.items())

  if key:
    data = data.get(key, default)

  return data

docker = get_data(f'https://hub.docker.com/v2/repositories/{github_project}', 'pull_count')
gh_data = get_data(f'https://api.github.com/repos/{github_project}')
stars = gh_data.get('stargazers_count', 0)
forks = gh_data.get('forks_count', 0)
# See https://stackoverflow.com/a/60458265/17860466 # to enabble anon add `&anon=true`
link = get_data(f'https://api.github.com/repos/{github_project}/contributors?per_page=1', mode=ReturnMode.header).get('Link')
contributors = link.split('page=')[-1].split('>')[0]
# Crowdin
  crowdin_data = get_data(f'https://api.crowdin.com/api/v2/projects/{crowdin_projet_id}?limit=1000', 'data', auth=os.environ.get('CROWDIN_TOKEN'))
languages = len(crowdin_data.get('targetLanguageIds', []))
#translators = get_data(f'https://api.crowdin.com/api/v2/projects/{crowdin_projet_id}/members', 'data', auth=crowdin_token)

# Write data
file_name.write_text(
f"""stats:
  - name: Docker pulls
    number: {docker}
    icon: fa-brands fa-docker
  - name: GitHub Stars
    number: {stars}
    icon: fa-solid fa-star
  - name: Forks
    number: {forks}
    icon: fa-solid fa-code-branch
  - name: Contributors
    number: {contributors}
    icon: fa-solids fa-hands-helping
  - name: Languages
    number: {languages}
    icon: fa-solid fa fa-language
"""