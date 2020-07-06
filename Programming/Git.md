# Git

Git Lang:
nice tutorial: 
https://www.sbf5.com/~cduan/technical/git/git-1.shtml

How to start:
mkdir [project]
cd [project]
git init

Make some changes.
git add <file>

git commit -a    # Adds all modified files, but not new ones.

git log    # Shows a log of your commits.
git log --graph --oneline --all    # Visually see the tree of commits.
git status
git diff <file>
git mv <file>    # Rename files.
git rm <file>    # Remove files.


General workflow:
1. Do some programming.
2. git status to see what files I changed.
3. git diff [file] to see exactly what I modified. 
4. git commit -a -m [message] to commit. 
5. 

branch==head (almost!)

HEAD (in all caps) refers to the most recent commit in the branch.
- or does HEAD mean current commit?

A general head is a reference to a commit object. It's like a pointer.

When you do `git checkout <head-name>` you are pointing HEAD to the commit object <head-name>
- it is almost always best to git add and git commit before checking out! Otherwise git will complain.
- The important point here is, save your changes (commit them) before moving away from this commit/branch/head.
- Similarly for before merging... COMMIT YOUR CHANGES!

git branch    # shows existing heads, with a star at HEAD
git branch -r    # Show remote branches.
git diff <head1>..<head2>    # Shows diff between commits ref'ed by <head1> and <head2>
git diff <head1>...<head2>    # Shows diff between <head2> and the common ancestor of <head1>,<head2>
git log <head1>..<head2>    # Show change log between <head2> and common ancestor

#### Good workflow:

Keep master branch in a stable, releaseable state.

- Make new branches to play with new features.
- Merge new feature branches into master when ready.
- After merging, you should delete the branch: `git branch -d <head>`
- Remember: "commits are cheap"

How to merge:
git checkout <stable_head>
git merge <feature_branch>

Collaboration:
git clone <remote>    # Copies a repo.
- Also copies all commit objects!

git fetch <remote_repo_ref>    # Retrieves all commits from remote repo, but DOES NOT move your heads.
If instead you want to grab the remote changes and update your own heads:
git pull <remote_repo_ref> <remote_head>    # Retrieves remote commits AND updates heads. 
The remote heads usually start with origin/<head>
- `git pull` automatically does a `git fetch`

`git push` does the opposite of `git pull` and tries to add new commits to the remote repo. 
- Also updates remote head to point to same commit as local head.

"fast-forward merge" just means that the updates were linear. 
- i.e. the commit being updated just moves forward by X commits, with no branching involved.

You can add a new branch to the remote repo:
`git push --set-upstream origin new-branch`
`git branch --track`    # Not sure how to use this.
`git branch --set-upstream`    # Not sure how to use this.

Delete a branch on remote repo:
`git push [remote-repository-reference] :[head-name]`

Rebasing - an alternative to merging.
`git rebase <commit>`
1. Collect all commits between HEAD and common ancestor of <commit> and HEAD. 
2. Put HEAD at <commit>
3. Apply all collected commits to <commit>
- This makes it look kind of like a fast forward merge.
- Essentially just scoops up the commits along this branch and attaches them to <commit>

Suppose you want to make your master branch look just like remote master branch:
git checkout master
git reset --hard origin/master
- WARNING: this may also affect your other local branches...?

Ultimately, a Git repo is a tree of commits.

A tag is a stable release of your code. 
- You are tagging a specific commit object so you can always go back to it for stability.
- Think of it like a new master branch for a version of your code. 

Make a tag:
git tag -a <tag_name> -m "<some message about it>"

WARNING: Don't name your tag the same as one of your branches.

Delete a local tag:
git tag --delete <tagname>
Delete a remote tag:
git push <remote_alias> :ref/tags/<tag_name> 