Title: Merge master into branch:
Date: 2017-07-09 16:09
Category: Git
Tags: git, branch, merge, rebase

There two commands that can be used to merge changes from master to a branch:

- Rebase the branch to the HEAD of the master, rewriting the history of the branch:
        ```bash
        git checkout BRANCH
        git rebase master
        ```
    One advantage of using `rebase` is that the commit history will be kept clean. There won't be a 'Merging master into branch' commit.
	And the order of commits will correspond to the order in which they were made.
	But beware, `rebase` should be used only for local branches that are not shared with other people.
	Rewriting history of a branch shared with your team, is dangerous.
	Use it for your own branches only. 

- Merge changes from the master into the branch, without rebasing:
        ```bash
        git checkout BRANCH
        git merge origin/master
        ```
    The advantage of `merge` is that it works, even if the branch is shared with other people.
	Use it for feature branches used by several developers.
