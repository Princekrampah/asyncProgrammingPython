## Git Branches

### Listing all available branches

```terminal
git branch
```

The branch with **\*** is the current branch, the HEAD branch

```terminal
*master
someotherbranch1
someotherbranch2
```

### Checkout which barnh you are on

```terminal
git status
```

### Creating a new branch

All git branches are created locally only and then published to the web(Github)

```terminal
git branch <new_branch_name>
```
Everytime you use this command git will assume you want to create a branch based on the current revision or state of your current branch.

You can create a branch based on a certain revision. Use the command below.

```terminal
git branch <new_branch_name> <revision_id>
```

### Switching Branches

To switch branches we use the **checkout** command.

```terminal
git checkout <branch_name>
```

There's a new command added to git we can use to switch branches as well.

```terminal
git switch <branch_name>
```

**NOTE:** Changing to a different branch causes the head to switch and point to that specific branch you have switched to.


### Renaming Branches

Sometimes you can misname a branch and its good to have the ability to rename that branch. Here's a command to do just that.

**NOTE:** First you need to be on that branch that you wish to rename. Use the switch command to do that.

```terminal
git switch <branch_name>
```

```terminal
git status
```

Once on the right branch then use the command below to rename the branch.

```terminal
git branch -m <new_branch_name>
```

Verify the name changed using:

```terminal
git status
```

You can also rename a branch that is not currently the *HEAD* branch or the checkedout branch. Use the command below to do just that. **Renaming a non-head branch**

```terminal
git branch -m <current_branch_name> <new_branch_name>
```


### Publishing Branches

You can publish local branches to remote branches using the command below. Make sure you first have a repo setup on the remove repo(Github). Then make sure it's been added to the local repo as well.


```terminal
git push -u origin <local-branch_name>
```
**origin**: this is the link to the remote repo.

**-u**: This flag is used to tell git to establish a tracking connection. Making tracking of the local and remote branches much easier. The reason we need a tracking connection is because, the remote and local repos are stored and managed as independent entities. The **-u** flag helps create a tracking connection between then enabling easy pull and push requests in the future.

### Tracking remote branches

Sometimes we have branches that are created on the remote repo maybe by another person and you wish to clone(track it). You can do that using

```terminal
git branch --track <remote_branch_name> origin/<remote_branch_name>
```

You can also do the same using

```terminal
git checkout --track origin/<remote_branch_name>
```

Here git will automatically use the **<remote_branch_name>** as the name of the local branch as well.

### Checking variations between locak and remote branches

You may have cases where some updated done on the local repo are not reflected or pushed to the remote repo or vice versa. You can check the variation or differences by usinng:

```terminal
git branch -v
```
