import requests
import json


def retrieve_recent_github_commits():
    url = 'https://api.github.com/repos/christopherjamesn/dfs-insights-react-client/commits'
    response = requests.get(url)
    for value in response.json():
        print(value['commit']['message'])


retrieve_recent_github_commits()
