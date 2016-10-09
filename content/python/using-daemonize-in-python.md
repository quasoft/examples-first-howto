Title: Example on using daemonize module in Python
Date: 2016-10-09 20:10
Category: Python
Tags: python, daemon, daemonize

Install:
--------

```bash
pip install daemonize
```

Example:
--------

```python
#!/usr/bin/env python3

import os
import sys
import time
from daemonize import Daemonize

def main():
    while True:
        time.sleep(10)

if __name__ == '__main__':
    appname=os.path.basename(sys.argv[0])
    pidfile='/tmp/mypidfile.pid'
    daemon = Daemonize(app=appname,pid=pidfile, action=main)
    daemon.start()

```
