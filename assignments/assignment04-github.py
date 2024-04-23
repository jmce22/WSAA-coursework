# In this assignment, I was asked to write a program in python that will read a file from a repository.
# The program should replace all the instances in the file of the text "Andrew" with my name (James)
# It should then commit those changes and push the file back to the repository 

# This required the setting up of an API key on GitHub; when using the API key in the programme,
# I saved it in a configuration file on my local machine, rather than the code which I have pushed to GitHub.

# Note: To run this programme, the user must download the PyGithub package which allows Python to interact with Github.
# This can be done using the command pip install PyGithub

from github import Github
from config import config as cfg
import requests

apikey = cfg["githubkey"]

g = Github(apikey)

repo = g.get_repo("jmce22/WSAA-coursework")
# print(repo.clone_url)

file_info = repo.get_contents("assignments/assignment4.txt")
url_of_file = file_info.download_url
# print(url_of_file)

response = requests.get(url_of_file)
file_content = response.text
# print(file_content)

# Used replace function on the original file contents to replace the name 'Andrew' with the name 'James' in the text
new_file_content = file_content.replace("Andrew", "James")

# print(new_file_content)

# I used the update_file method to push the changes to the file to GitHub and include a commit message (inputted through 
# the second parameter). 
# SHA here refers to the Secure Hash Algorithm, whis is an id Github assigns to each commit.
# https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
gitHubResponse=repo.update_file(file_info.path,"Changed the name 'Andrew' in assignment4.txt with my name (James)", new_file_content, file_info.sha)
print(gitHubResponse)