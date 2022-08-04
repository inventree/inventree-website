from enum import Enum
import json
from pathlib import Path
from urllib.request import urlopen, Request

file_name = Path('_data/general/stats.yml')

class ReturnMode(Enum):
  data = 0
  header = 1

def get_data(url, key=None, default=0, mode: ReturnMode=ReturnMode.data):
  """Fetches data from remote endpoint"""
  httprequest = Request(url, headers={"Accept": "application/json"})

  with urlopen(httprequest) as response:
    if mode == ReturnMode.data:
      data = response.read().decode()
      data = json.loads(data)
    
    elif mode == ReturnMode.header:
      data = dict(response.headers.items())

  if key:
    data = data.get(key, default)

  return data

docker = get_data('https://hub.docker.com/v2/repositories/inventree/inventree', 'pull_count')
gh_data = get_data('https://api.github.com/repos/inventree/inventree')
stars = gh_data.get('stargazers_count', 0)
forks = gh_data.get('forks_count', 0)
# See https://stackoverflow.com/a/60458265/17860466 # to enabble anon add `&anon=true`
link = get_data('https://api.github.com/repos/inventree/inventree/contributors?per_page=1', mode=ReturnMode.header).get('Link')
contributors = link.split('page=')[-1].split('>')[0]

# Write data
file_name.write_text(
f"""stats:
  - name: Docker pulls
    number: {docker}
  - name: GitHub Stars
    number: {stars}
  - name: Forks
    number: {forks}
  - name: Contributors
    number: {contributors}""")
