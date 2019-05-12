import requests
import json
import formatter


def retrieve_recent_github_commits(repos=['dfs-insights-react-client']):
    for repo in repos:
        url = f'https://api.github.com/repos/christopherjamesn/{repo}/commits'
        response = requests.get(url)
        for value in response.json():
            print(value['commit']['message'])
            with open('todays_git_commits.txt', 'a') as open_file:
                open_file.write(value['commit']['committer']['date'] + '\n')
                open_file.write(value['commit']['message'] + '\n')


retrieve_recent_github_commits()
