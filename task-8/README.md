# **(Task - 8)** Perceval's Quest

I actually found this task quite confusing. until a few days ago, I was completely sure that the task had to be accomplished in terminal (*Bash*). However it was only after a gym-trainer hinted that this is quite easy and has to be done in python, was I completely blown off.

I spent days learning to use awk, grep and RegEx to print the list of repo name and then use for loop to iterate through each item in the repo name list to find commits using perceval command.

As it turned out, the task was actually pretty easy. I used python packages like ***os*** and ***PyGitHub*** to do the task. The ***os*** was used to run the shell scripts in the system, ***PyGitHub*** was used to get the repos.

The list containing repository names is first created and then a similar loop is used to fetch commits of the repos via *perceval*.