import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime


def retrieve_recent_github_commits(repos=['test-word-react-add-in', 'word-add-in-pass-through-service', 'onit_java_sdk']):
    load_dotenv()
    for repo in repos:
        with open('todays_git_commits.txt', 'a') as open_file:
            open_file.write(repo + '\n')
        url = f'https://api.github.com/repos/christopherjamesn/{repo}/commits?page=1&per_page=5'
        response = requests.get(
            url, auth=('ChristopherJamesN', os.environ['PERSONAL_ACCESS_TOKEN']))
        for value in response.json():
            print(value['commit']['message'])
            with open('todays_git_commits.txt', 'a') as open_file:
                d = datetime.strptime(
                    value['commit']['committer']['date'], '%Y-%m-%d %H:%M:%S')
                day_string = d.strftime('%Y-%m-%d')
                open_file.write('\n')
                open_file.write(day_string + '\n')
                open_file.write(value['commit']['message'] + '\n')


def retrieve_recent_gitlab_commits(repos=['test-word-react-add-in', 'word-add-in-pass-through-service', 'onit_java_sdk']):
    load_dotenv()
    for repo in repos:
        with open('todays_gitlab_commits.txt', 'a') as open_file:
            open_file.write(repo + '\n')


retrieve_recent_github_commits()
retrieve_recent_gitlab_commits()
