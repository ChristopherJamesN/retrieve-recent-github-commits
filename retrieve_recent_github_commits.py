import requests


def retrieve_recent_github_commits():
    url = 'https://api.github.com/repos/christopherjamesn/dfs-insights-react-client/commits'
    response = requests.get(url)
    print(response.text)


retrieve_recent_github_commits()
