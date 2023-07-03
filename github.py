import requests

BASE_URL = "https://api.github.com"


class HTTPError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(
            f"HTTP Error: received status code {self.status_code}")


def request_url(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPError(response.status_code)
    return response.json()


def get_commits(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"
    commits = request_url(url)

    for commit in commits:
        message = commit['commit']['message']
        author = commit['commit']['author']['name']
        print(f"{author}: {message}")


def get_user(username):
    url = f"{BASE_URL}/users/{username}"
    user_info = request_url(url)

    name = user_info['name']
    company = user_info['company']
    location = user_info['location']
    print(f"name = {name}\ncompany = {company}\nlocation = {location}")


try:
    get_user("taeho0888")
    get_commits("coffeebreaker", "study")
except HTTPError as e:
    print(e)
