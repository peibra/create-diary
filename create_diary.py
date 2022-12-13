import sys
import os
import pathlib
import datetime

date = datetime.datetime.now().date()

cwd_path = os.getcwd()
cwd_name = cwd_path.split('/')[-1]

try:
    directory = sys.argv[1]
    filename = f'{date}.md'
    path = f'{directory}/{filename}'
    if not os.path.exists(directory):
        os.mkdir(directory)
    if os.path.isfile(path):
        print(f'{filename} already exists in {cwd_name}/{directory}/')
    else:
        f = pathlib.Path(f'{path}')
        f.touch()
        print(f'{filename} successfully created in {cwd_name}/{directory}/')
except IndexError:
    raise TypeError('directory not specified')
