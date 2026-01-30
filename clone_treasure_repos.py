import urllib.request
import json
import subprocess
import os
import sys

ORG_NAME = "treasureproject"
OUTPUT_DIR = "treasure_repos"

def fetch_repos():
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{ORG_NAME}/repos?page={page}&per_page=100"
        print(f"Fetching page {page}...")
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Python-Script')
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                if not data:
                    break
                repos.extend(data)
                if len(data) < 100:
                    break
                page += 1
        except Exception as e:
            print(f"Error fetching repos: {e}")
            break
    return repos

def clone_repos(repos):
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    total = len(repos)
    print(f"Found {total} repositories.")
    
    for i, repo in enumerate(repos):
        name = repo['name']
        clone_url = repo['clone_url']
        target_path = os.path.join(OUTPUT_DIR, name)
        
        print(f"[{i+1}/{total}] Cloning {name}...")
        
        if os.path.exists(target_path):
            print(f"  Skipping {name} (already exists)")
            continue
            
        try:
            subprocess.run(['git', 'clone', clone_url, target_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"  Failed to clone {name}: {e}")

if __name__ == "__main__":
    print(f"Targeting Organization: {ORG_NAME}")
    repos = fetch_repos()
    clone_repos(repos)
