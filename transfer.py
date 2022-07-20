import requests
from requests.structures import CaseInsensitiveDict

OWNER = '' # the original owner of the repo
NEW_OWNER = '' # the new owner of the repo
GITHUB_SECRET = '' # the github secret token

REPOSITORY_LIST = 'repo_list.txt' # path to the repository list file

def transfer_repository(repo_name):
    global OWNER, NEW_OWNER, GITHUB_SECRET
    url = f"https://api.github.com/repos/{repo_name}/transfer"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/vnd.github+json"
    headers["Authorization"] = f"token {GITHUB_SECRET}"
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = '{"new_owner":' + '"' + NEW_OWNER + '"}'
    resp = requests.post(url, headers=headers, data=data)
    return resp

repositories = []
with open(REPOSITORY_LIST, 'r') as f:
    for line in f:
        repositories.append(line.split()[0])

for repository in repositories:
    res = transfer_repository(repository)
    print(res.status_code)
