# upload_save.py

import os
import requests
import getpass

# 1. Set your Discord webhook URL here
WEBHOOK_URL = "https://discord.com/api/webhooks/1429860870686511266/1CaCq46qxmyLYYn2rW98ThL016IEBQPMO4avu6lm6sEezpq2lywY8_LN4PeW4dFOS3El"

# 2. Set the paths to the files you want to upload (you can add more!)
# Use '____' in place of the username — it will be replaced automatically
FILE_PATHS = [
    r"C:\Users\____\Downloads\clashAPI.py",
    # Add more paths here if needed
]

DISCORD_LIMIT_BYTES = 8 * 1024 * 1024  # 8 MB

def resolve_path(path_template: str) -> str:
    username = getpass.getuser()
    path = path_template.replace('____', username)
    path = os.path.expandvars(path)
    path = os.path.expanduser(path)
    return path

def upload_file(file_path, webhook_url):
    if not os.path.isfile(file_path):
        print(f"⚠️ File not found: {file_path}")
        return False

    size = os.path.getsize(file_path)
    if size > DISCORD_LIMIT_BYTES:
        print(f"❌ File too large to upload: {file_path}")
        return False

    with open(file_path, 'rb') as f:
        files = {'file': (os.path.basename(file_path), f)}
        response = requests.post(webhook_url, files=files)

    if response.status_code in (200, 204):
        print(f"✅ Uploaded: {os.path.basename(file_path)}")
        return True
    else:
        print(f"❌ Failed to upload: {file_path}")
        print(f"Status Code: {response.status_code}, Response: {response.text}")
        return False

def main():
    if "YOUR_DISCORD_WEBHOOK_URL_HERE" in WEBHOOK_URL:
        print("⚠️ Please set your Discord webhook URL in the script.")
        return

    print("📤 Starting upload...")
    for template in FILE_PATHS:
        full_path = resolve_path(template)
        upload_file(full_path, WEBHOOK_URL)

if __name__ == "__main__":
    main()
