# github-repo-transfer
Mass Transfer multiple Github repositories using Python.


# Requirements

1. The gh library must be installed.
2. Get a Github API token.

# Setup

Modify the python transfer.py file to include your token, current owner, and previous owner. Then run the file.
# Usage
```shell
chmod +x grab_repo_list.sh
python3 transfer.py
```

# What does this do?

This project is meant to serve as a way to transfer multiple Github repositories to a new owner. It utilises the github API under the hood. I designed this originally just to transfer some of my old work to an archive account, but it can be used to transfer any number of repositories to any number of owners.