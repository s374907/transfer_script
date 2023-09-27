import requests

# GitHub API base URL
base_url = "https://api.github.com"

# Replace with your GitHub Personal Access Tokens (PATs)
source_user_token = input("User Token to transfer from:")
target_user_token = input("User Token to transfer to:")

# Replace with the source and target GitHub usernames
source_user = input("Username to transfer from: ")
target_user = input("Username to transfer to: ")

# Function to get all repositories for a user
def get_user_repositories(username, token):
    url = f"{base_url}/users/{username}/repos"
    headers = {
        "Authorization": f"token {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to get repositories for user {username}: {response.text}")

# Function to transfer ownership of a repository
def transfer_repository_ownership(repository, source_user, target_user, source_token):
    url = f"{base_url}/repos/{source_user}/{repository['name']}/transfer"
    headers = {
        "Authorization": f"token {source_token}"
    }
    data = {
        "new_owner": target_user
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 202:
        print(f"Transferred ownership of {repository['name']} to {target_user}")
    else:
        print(f"Failed to transfer ownership of {repository['name']}: {response.text}")

# Get all repositories of the source user
source_repositories = get_user_repositories(source_user, source_user_token)

# Transfer ownership of each repository to the target user
for repository in source_repositories:
    transfer_repository_ownership(repository, source_user, target_user, source_user_token)