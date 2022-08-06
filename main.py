import os
import requests


def main():
    commits = os.environ["commits"]

    version = os.environ["versionNo"]

    messages = '\n'.join([i.message for i in commits])

    changelog = f"""Version {version}
```md
{messages}
```
"""
    json = {
      "content": changelog,
      "embeds": null,
      "attachments": []
      }

    requests.post("https://discord.com/api/webhooks/1005383165013135420/Y3AqDuwTIMTC3hdAN2nl9ZK0QAyCFGwsuX-UQyShh0TWaCabsG8C7MeSnKwBP8G6A-5n", json=changelog


if __name__ == "__main__":
    main()
