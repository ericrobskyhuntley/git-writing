from git import Repo
import pypandoc
from os import path, getcwd
from glob import glob
from datetime import datetime
import argparse
import shutil

CWD = getcwd()
FILEPATH = path.dirname(path.abspath(__file__))
DEFAULT_TYPE = 'article'

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--genre", help="Genre of writing.", choices=['article'])
parser.add_argument("-n", "--name", help="Name of new repository.", default=DEFAULT_TYPE)
args = parser.parse_args()

def git_init(name, type='article'):
    repo_path = path.join(CWD, name)
    r = Repo.init(repo_path)
    readme = path.join(repo_path, 'README.md')
    with open(readme, 'w') as rm:
        rm.write(f'# {name} \n')
        rm.close()
    template_path = path.join(FILEPATH, 'assets', 'templates', DEFAULT_TYPE)
    md_glob = glob(path.join(template_path, '*.md'))
    yaml_glob = glob(path.join(template_path, '*.yaml'))
    file_list = md_glob + yaml_glob
    
    for file in file_list:
        shutil.copy(file, repo_path)
    
    repo_file_list = glob(path.join(repo_path, '*'))
    r.index.add(repo_file_list)
    r.index.commit('initial commit')
    return None

if __name__ == '__main__':
    git_init(args.name)