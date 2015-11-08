Title: Rename directory of project that is using virtualenv
Date: 2015-11-08 16:12
Category: Python
Tags: virtualenv, python

Examples:
---------

### Example 1. - Renaming and recreating virtualenv:

```bash
$ # MAKE BACKUP OF WHOLE PROJECT DIRECTORY     # Recommended
$ cd /path/to/myproject                        # cd to project directory
$ source .venv/bin/activate                    # Activate virtual environment
(.env)$ pip freeze > requirements.txt          # Create list of required packages
$ deactivate                                   # Deactivate virtual environment

$ mv /path/to/myproject /path/to/yourproject   # Rename project directory
$ mv .venv .venv.old                           # Backup old .venv directory

$ mkdir .venv                                  # Create new .venv directory
$ virtualenv -p /usr/bin/python2.7 .venv       # Recreate virtual environment
$ source .venv/bin/activate                    # Activate virtual environment
$ pip install -r requirements.txt              # Reinstall packages
```

Explanation:
------------

Note: This is only one of the possible approaches to rename a project directory containing a `virtualenv` environment. Recreating virtual environment is recommended only if the number of project dependencies is small and the time required to reinstall packages will not take more than a few minutes.
