# auto_deploy.py
import os
import subprocess
from github import Github
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "ai-autonomous-system"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

RENDER_API_KEY = os.getenv("RENDER_API_KEY")
RENDER_SERVICE_ID = os.getenv("RENDER_SERVICE_ID")

def create_or_get_repo():
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    try:
        repo = user.create_repo(REPO_NAME)
        print("GitHub repo created")
    except:
        repo = user.get_repo(REPO_NAME)
        print("GitHub repo exists")
    return repo.clone_url

def push_to_github(clone_url):
    os.chdir(BASE_DIR)
    subprocess.run(["git","init"])
    subprocess.run(["git","add","."])
    subprocess.run(["git","commit","-m","Initial commit from AI Money System"])
    subprocess.run(["git","branch","-M","main"])
    subprocess.run(["git","remote","add","origin",clone_url])
    subprocess.run(["git","push","-u","origin","main"])
    print("Code pushed to GitHub")

def trigger_render_deploy():
    url = f"https://api.render.com/v1/services/{RENDER_SERVICE_ID}/deploys"
    headers = {"Authorization": f"Bearer {RENDER_API_KEY}"}
    r = requests.post(url, headers=headers)
    if r.status_code == 201:
        print("Render deploy triggered successfully")
    else:
        print("Render deploy failed:", r.text)

if __name__ == "__main__":
    clone_url = create_or_get_repo()
    push_to_github(clone_url)
    trigger_render_deploy()
    print("GitHub + Render auto-deploy complete")
