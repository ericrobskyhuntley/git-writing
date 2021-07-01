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
parser.add_argument("-n", "--reponame", help="Name of new repository.", default=DEFAULT_TYPE)
parser.add_argument("-p", "--repopath", help="Path to repo.", default=CWD)
parser.add_argument("-g", "--genre", help="Genre of writing.", choices=['article'])
parser.add_argument("-d", "--draft", help="Include this flag to automatically create draft branch.", action='store_true')
args = parser.parse_args()

def git_init(name, repo_path=CWD, genre='article', draft=False):
    """
    Initializes a git repo
    """
    repo_dir = path.join(repo_path, name)
    r = Repo.init(repo_dir)
    readme = path.join(repo_dir, 'README.md')
    with open(readme, 'w+') as rm:
        rm.write(f'# {name} \n')
        rm.close()
    template_path = path.join(FILEPATH, 'assets', 'templates', DEFAULT_TYPE)
    md_glob = glob(path.join(template_path, '*.md'))
    yaml_glob = glob(path.join(template_path, '*.yaml'))
    file_list = md_glob + yaml_glob
    for file in file_list:
        shutil.copy(file, repo_dir)
    
    repo_file_list = glob(path.join(repo_dir, '*'))
    r.index.add(repo_file_list)
    head = r.active_branch
    r.index.commit('initial commit')
    # Rename primary branch to 'main'.
    head.rename('main')
    if draft:
        head.checkout(b='draft')
    return None

if __name__ == '__main__':
    git_init(args.reponame, args.repopath, args.genre, args.draft)