"""
A module for obtaining repo readme and language data from the github API.
Before using this module, read through it, and follow the instructions marked
TODO.
After doing so, run it like this:
    python acquire.py
To create the `data.json` file that contains the data.
"""
import os
import json
from typing import Dict, List, Optional, Union, cast
import requests
from tqdm.notebook import tqdm_notebook

from env import github_token, github_username

# required imports
from requests import get
import pandas as pd
from bs4 import BeautifulSoup
import time


# goes to github and pages through the most forked repos, grabbing the 'num_pages' number of pages
def fetch_github_repos(num_pages):
    items_list = []
    # we will grab repos filtering by which ones have a readme file
    # we increment the p= parameter to go to each subsequent page, and utilize the tqdm process bar to maintain sanity
    # this function takes roughly 45 minutes to run
    for i in tqdm_notebook(range(1,num_pages+1), desc = 'Retreiving data'):
        # add a sleep amount of random time so that we don't get HTTP 429s
        time.sleep(2.5)
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        url = f'https://github.com/search?l=&p={i}&q=spotify+filename%3AREADME.md+filename%3Areadme.md&ref=advsearch&type=Repositories'
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # each page has 10 results. Let's loop through and find each instance of page element element = 'a' class = 'v-align-middle'
        links = soup.find_all('a', class_='v-align-middle')
        for repo_link in links:
            time.sleep(2.5)
            repo_name = repo_link.text
            # add it to our output array
            items_list.append(repo_name)
    return items_list

# returns a list of github repo names, either from a file on disk or from github using the fetch_github_repos function
def get_github_repos(cached=False, num_pages = 100):
    # If the cached parameter is false, or the csv file is absent, use github
    if os.path.isfile('git_urls.csv') == False:
        # read from github
        repo_list = fetch_github_repos(num_pages)
        # and write to the cache file for next time
        df = pd.DataFrame(repo_list, columns=['repos'])
        df.to_csv('git_urls.csv', index=False)
    else:
        # read from the cache file on disk
        df = pd.read_csv("git_urls.csv")
        repo_list = df['repos'].to_list()

    # either way, return the list of repos
    return repo_list





headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )

def github_api_request(url: str) -> Union[List, Dict]:
    response = requests.get(url, headers=headers)
    response_data = response.json()
    if response.status_code != 200:
        raise Exception(
            f"Error response from github api! status code: {response.status_code}, "
            f"response: {json.dumps(response_data)}"
        )
    return response_data


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos/{repo}"
    repo_info = github_api_request(url)
    if type(repo_info) is dict:
        repo_info = cast(Dict, repo_info)
        return repo_info.get("language", None)
    raise Exception(
        f"Expecting a dictionary response from {url}, instead got {json.dumps(repo_info)}"
    )


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos/{repo}/contents/"
    contents = github_api_request(url)
    if type(contents) is list:
        contents = cast(List, contents)
        return contents
    raise Exception(
        f"Expecting a list response from {url}, instead got {json.dumps(contents)}"
    )


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists the files in a repo and
    returns the url that can be used to download the repo's README file.
    """
    for file in files:
        if file["name"].lower().startswith("readme"):
            return file["download_url"]
    return ""


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns a
    dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    readme_url = get_readme_download_url(contents)
    if (readme_url == ''):
        readme_contents = ''
    else:
        readme_contents = requests.get(get_readme_download_url(contents)).text
    
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": readme_contents,
    }


def scrape_github_data():
    REPOS = get_github_repos()
    return [process_repo(repo) for repo in tqdm_notebook(REPOS, desc = 'Populating DataFrame')]


if __name__ == "__main__":
    data = scrape_github_data()
    json.dump(data, open("data2.json", "w"), indent=1)
    
def github_df():
    if os.path.isfile('github_df.csv') == False:
        df = scrape_github_data()
        df = pd.DataFrame(df)
        df.to_csv('github_df.csv', index=False)
    else:
        # read from the cache file on disk
        df = pd.read_csv("github_df.csv")
        
    return df

    