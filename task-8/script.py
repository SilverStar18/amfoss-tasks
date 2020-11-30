import os
from github import Github

org = Github().get_user('amfoss')

for repo in org.get_repos() :
    print(repo.name)

for repo in org.get_repos() :    
    os.system('perceval git --json-line https://github.com/amfoss/'+repo.name+' >> task-8.json')

os.system('cat commits.json')