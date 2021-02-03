#!/usr/bin/env python3

from os import chdir
from pathlib import Path

chdir("docs/")
blog = Path("Tech Blog")
for md in sorted(blog.glob('**/*.md'), reverse=True):
    print(f'        "{md.name[11:]}": "{md}"')
