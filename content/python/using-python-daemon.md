Title: Example on using python-daemon
Date: 2016-10-09 19:32
Category: Python
Tags: python, daemon, python-daemon

Install:
--------

```bash
pip install python-daemon
```

Example:
--------

```python
#!/usr/bin/env python3

import signal
import daemon
import lockfile
import time

def start():
    print("Initial setup")

def stop():
    print("Cleanup")

def reload():
    print("Reload config")

def run():
    while True:
        print("Main program")
        time.sleep(10)

context = daemon.DaemonContext(
    working_directory='/',
    umask=2,
    pidfile=lockfile.FileLock('/tmp/mylockfile')
    )

context.signal_map = {
    signal.SIGTERM: stop,
    signal.SIGHUP: 'terminate',
    signal.SIGUSR1: reload,
    }

# No need to change gid, as we want our service to run without root
#context.gid = grp.getgrnam('nogroup').gr_gid

# No files to preserve
#context.files_preserve = [important_file, interesting_file]

start()

with context:
    run()
    
```
