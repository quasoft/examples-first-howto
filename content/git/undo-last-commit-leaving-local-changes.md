Title: Undo last git commit, leaving local changes:
Date: 2017-01-09 14:23
Category: Git
Tags: git, commit, undo, last, reset

Undo commit only, but leave index changes:

```bash
git reset --soft HEAD~1
```

Undo both commit and index changes:

```bash
git reset HEAD~1
```

Both actions leave changes in local files intact.
