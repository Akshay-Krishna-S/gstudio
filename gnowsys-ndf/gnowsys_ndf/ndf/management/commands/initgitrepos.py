from django.core.management.base import BaseCommand, CommandError

import os

# from django_mongokit import document

from gnowsys_ndf import settings
from gnowsys_ndf.ndf import models

from git import Repo

# os.path.join( PROJECT_ROOT, "static/ndf/git-repo" )

class Command(BaseCommand):
    help = 'Creates required git repositories for each collection'

    def handle(self, *args, **options):
    	git_repo_path = settings.GIT_REPO_PATH
    	
    	print("\n Importing classes from models file, successfully done...\n")
    	
    	print(" PROJECT_ROOT  : " + settings.PROJECT_ROOT + "\n")
    	print(" GIT_REPO_PATH : " + git_repo_path + "\n")
  	
    	dir_exists = os.path.isdir(git_repo_path)
    	print(" GIT_REPO_PATH Doesn't Exists!!\n", " GIT_REPO_PATH Exists..\n")[dir_exists]
    	
    	if not dir_exists:
    		os.system("mkdir -p " + git_repo_path)
    		print(" GIT_REPO_PATH created successfully..." + "\n")

    	for model in settings.VERSIONING_COLLECTIONS:
    		model_repo = Repo.init( os.path.join( git_repo_path, model ), True )
    		print(" " + str(model_repo) + " -- git repository created")
    	
    	print("\n")


