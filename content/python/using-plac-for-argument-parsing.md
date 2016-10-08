Title: Example on using `plac` for argument parsing in Python
Date: 2016-10-08 16:49
Category: Python
Tags: python, args, parsing

Install:
--------

```bash
pip install plac
```

Example:
--------

```python
#!/usr/bin/env python3

def main(
    someoption: ('Optional argument', 'option', 'o'),           # Optional argument with abbreviation
    someflag: ('Boolean flag - True if set', 'flag', 'f'),      # Boolean flag
    someint: ("Integer argument",'positional', None, float),    # Explicit positional with number type
    somestring:"String argument"='hello'                        # Implicit positional with default value
):
    """Example for parsing arguments with plac"""
    print('someint value: %d' % someint)
    print('somestring value: %s' % somestring)

    if (someflag):
        print("Flag -f is set")
    else:
        print("Flag -f is not set")

    if (someoption):
        print("Option -o is set: %s" % someoption)
    else:
        print("Option -o is not set")

if __name__ == '__main__':
    import plac
    plac.call(main)

```
