import os,sys
curr_dir = os.path.abspath(os.path.dirname(__file__))

#Add all external dependencies
for path in [path for path in os.listdir(os.path.join(curr_dir, 'externals')) if path != '.svn']:
    sys.path.insert(0,os.path.join(curr_dir, 'externals', path))
#Add the django-recipes project
sys.path.insert(0, curr_dir)
