import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime


def retrieve_recent_github_commits(repos=['test-word-react-add-in', 'word-add-in-pass-through-service', 'onit_java_sdk']):
    load_dotenv()
    if os.path.isfile('todays_git_commits.txt'):
        os.remove('todays_git_commits.txt')
    for repo in repos:
        with open('todays_git_commits.txt', 'a') as open_file:
            open_file.write('\n' + repo + '\n')
        url = f'https://api.github.com/repos/christopherjamesn/{repo}/commits?page=1&per_page=25'
        response = requests.get(
            url, auth=('ChristopherJamesN', os.environ['PERSONAL_ACCESS_TOKEN']))
        for value in response.json():
            print(value['commit']['message'])
            with open('todays_git_commits.txt', 'a') as open_file:
                day_string = value['commit']['committer']['date']
                # open_file.write('\n')
                #open_file.write(day_string + '\n')
                open_file.write('*' + value['commit']['message'] + '\n')


def retrieve_number_of_github_commits():
    load_dotenv()
    url = f'https://api.github.com/repos/christopherjamesn/commits'
    response = requests.get(
        url, auth=('ChristopherJamesN', os.environ['PERSONAL_ACCESS_TOKEN']))
    for value in response.json():
        print(value)


def retrieve_recent_gitlab_commits(repos=['test-word-react-add-in', 'word-add-in-pass-through-service', 'onit_java_sdk']):
    load_dotenv()
    if os.path.isfile('todays_gitlab_commits.txt'):
        os.remove('todays_gitlab_commits.txt')
    for repo in repos:
        with open('todays_gitlab_commits.txt', 'a') as open_file:
            open_file.write('\n' + repo + '\n')


retrieve_number_of_github_commits()
