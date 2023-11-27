from enum import Enum

import argparse
import json
import os
import sys

from urllib.request import urlopen, Request


# External data
docker_project = 'inventree/inventree'
github_project = "InvenTree/InvenTree"
crowdin_project_id = 452300


class ReturnMode(Enum):
  data = 0
  header = 1


def get_data(url, key=None, default=0, mode: ReturnMode=ReturnMode.data, auth=None):
  """Fetches data from remote endpoint"""

  httprequest = Request(url, headers={"Accept": "application/json"})

  print(f"Requesting data from '{url}'")

  if auth:
    httprequest.add_header("Authorization", f"Bearer {auth}")

  with urlopen(httprequest) as response:

    if response.status != 200:
      raise Exception(f"Failed to fetch data from '{url}': {response.status}")

    if mode == ReturnMode.data:
      data = response.read().decode()
      data = json.loads(data)
    elif mode == ReturnMode.header:
      data = dict(response.headers.items())

    if key:
      data = data.get(key, default)

  return data


def get_docker_stats() -> dict:
  """Collect docker stats from remote endpoint"""

  docker_data = get_data(f'https://hub.docker.com/v2/repositories/{docker_project}')

  return docker_data or {}


def get_github_data(token: [str,  None]) -> dict:
  """Collect data from GitHub"""

  if not token:
    print("Note: No GitHub token provided")

  # Fetch base data
  gh_data = get_data(f'https://api.github.com/repos/{github_project}', auth=token)

  # Fetch contributor information
  gh_contributors = get_data(f'https://api.github.com/repos/{github_project}/contributors?per_page=1', mode=ReturnMode.header, auth=token)

  link = gh_contributors.get('Link', '')

  if link:
    gh_data['contributors'] = link.split('page=')[-1].split('>')[0]

  return gh_data


def get_crowdin_data(token: [str, None]) -> dict:
  """Collect data from Crowdin"""

  if not token:
    print("No Crowdin token provided, skipping Crowdin stats")
    return {}

  crowdin_data = get_data(f'https://api.crowdin.com/api/v2/projects/{crowdin_project_id}?limit=1000', 'data', auth=token)
  crowdin_data['languages'] = len(crowdin_data.get('targetLanguageIds', []))

  return crowdin_data


if __name__ == '__main__':

  parser = argparse.ArgumentParser(
  prog="InvenTree Stats",
  description="Fetch InvenTree stats data from remote endpoints",
  )

  parser.add_argument('--github-token', '-g', type=str, help='GitHub token (optional)')
  parser.add_argument('--crowdin-token', '-c', type=str, help='Crowdin token (optional)')

  args = parser.parse_args()

  print("Collecting InvenTree stats...")

  # Generate output filename
  output_filename = os.path.abspath(os.path.join(
  os.path.dirname(__file__),
  '..',
  'src',
  'data',
  'stats.json',
  ))

  # Fetch docker stats
  docker_data = get_docker_stats()

  docker_pulls = docker_data.get('pull_count', 0)

  # Fetch GitHub stats
  github_token = args.github_token or os.environ.get('GITHUB_TOKEN')
  github_data = get_github_data(github_token)

  github_forks = int(github_data.get('forks_count', 0))
  github_stars = int(github_data.get('stargazers_count', 0))
  github_contributors = int(github_data.get('contributors', 0))

  # Fetch Crowdin stats
  crowdin_token = args.crowdin_token or os.environ.get('CROWDIN_TOKEN')
  crowdin_data = get_crowdin_data(crowdin_token)

  crowdin_languages = crowdin_data.get('languages', 0)

  # Construct the output data (typescript)
  output_data = {
    "docker_pulls": docker_pulls,
    "github_stars": github_stars,
    "github_forks": github_forks,
    "github_contributors": github_contributors,
    "crowdin_languages": crowdin_languages,
  }

  with open(output_filename, 'w') as f:
    f.write(json.dumps(output_data, indent=2))

  print("InvenTree stats updated successfully:")
  print(f"Wrote data to '{output_filename}'")
