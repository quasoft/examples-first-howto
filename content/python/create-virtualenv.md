Title: Use virtualenv to create isolated Python environments
Date: 2015-11-08 15:36
Category: Python
Tags: virtualenv, python

Examples:
---------

### Example 1. - Create virtual environment on Linux/Unix:

```bash
pip install virtualenv
cd /path/to/project
mkdir .venv
virtualenv -p /usr/bin/python2.7 .venv
source .venv/bin/activate
...
#install packages, compile project, etc.
...
deactivate
```

### Example 2. - Create virtual environment on Windows:

```batch
pip install virtualenv
cd C:\path\to\project
mkdir .venv
virtualenv -p C:\\Python27\\python.exe .venv
.venv\Scripts\activate.bat
...
REM install packages, compile project, etc.
...
REM close command prompt
```

Explanation:
------------

One of Python's powers is how easy it is to create and use modules and packages to extend the built-in functionality. By default all packages are installed in a global repository and are available to all projects that may need them.

This is very convenient until you need to use different versions of
the same package in separate projects. That is why it is common
convention to use the `virtualenv` tool when using python packages.

`virtualenv` is a tool for creating of isolated Python environments.
Such virtual environments contain all package dependencies of a project
and thus helps to avoid conflicts in package version requirements
across multiple Python projects.

Using `virtualenv` includes three steps:

1. Install virtualenv package.
2. Create an empty folder .venv (you can choose an arbitrary name).
3. Create a virtual ennvironment with `virtualenv` command.
4. Activate virtual ennvironment with `activate` script.
5. Do actual work on your project - eg. install packages with `pip install`, edit sources, compile project.
6. Deactivate virtual ennvironment with `deactivate` script or just close the terminal/console.

   Deactivation cleans up the temporary environment variables and is is required only if you intend to use the same terminal/console to work on another project. Usually it is enough to just close the terminal/console window.
