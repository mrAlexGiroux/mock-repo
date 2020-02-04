import git
from git_contributions_importer import *
# Your private repo or Bitbucket repo
repo = git.Repo("C:\BitBucket\sofe")
# Your mock repo
mock_repo = git.Repo("C:\Mock_GitHub\mock-repo")

importer = Importer([repo], mock_repo)

# I use both my personal email and work email here,

# Since the private repo uses work email, and Github profiles uses

# my work email

importer.set_author(['giroux.dion@gmail.com'])

importer.import_repository()
