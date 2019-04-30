## switch to branch
git checkout branc
git checkout -b branch 


## have git map in bash
1) nano /home/username/.gitconfig 

2) type this below
[alias]
        lg1 = log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' --all

3) to see it: git lg1

## after all not commit file and delete changes made since last commit
git checkout filename

## 
