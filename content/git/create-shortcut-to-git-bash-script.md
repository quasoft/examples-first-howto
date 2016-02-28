Title: Create shortcut that executes a script via Git bash
Date: 2016-02-28 17:43
Category: Git
Tags: git, bash, shortcut, script

Example:
--------

To create a shortcut that executes a bash script in Git bash environment, add the following line in Target field of shortcut (or inside a batch script).

```batch
"C:\Program Files\Git\bin\sh.exe" -l "D:\path-to-script.sh"
```
