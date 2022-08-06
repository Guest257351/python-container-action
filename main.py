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

    requests.post(


if __name__ == "__main__":
    main()
