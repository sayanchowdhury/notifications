import requests

AUTH_TOKEN = "API TOKEN HERE"
USER_URL = "https://api.github.com/user"

def get_subscribed_repos_json():
    headers = {"Authorization": "token %s" % AUTH_TOKEN}
    user_data = requests.get(USER_URL, headers=headers)
    subscription_url = user_data.json()["subscriptions_url"]
    subscribed_repos = requests.get(subscription_url, headers=headers)
    subscribed_repos_json = subscribed_repos.json()

    return subscribed_repos_json

def parse_subscribed_repos(subscribed_repos_json):
    parsed_repos = []
    for subscribed_repo in subscribed_repos_json:
        temp_parsed_repo = {}
        temp_parsed_repo["name"] = subscribed_repo["name"]
        temp_parsed_repo["description"] = subscribed_repo["description"]
        temp_parsed_repo["url"] = subscribed_repo["html_url"]
        temp_parsed_repo["owner"] = subscribed_repo["owner"]["login"]
        parsed_repos.append(temp_parsed_repo)

    return parsed_repos

def display_repo_info(repo_dict):
    for repo in repo_dict:
        print("----------------")
        for key,value in repo.items():
            print("%s: %s" % (key, value))

if __name__ == "__main__":
    subscribed_repos = get_subscribed_repos_json()
    parsed_repos = parse_subscribed_repos(subscribed_repos)
    display_repo_info(parsed_repos)
