"""
Um comando para criar o id da url encurtada
    program --shorten / -s <url>
Um comando que recebe um id e devolve a url original
    program --resolve / -r <id>
"""

import argparse
import core

parser = argparse.ArgumentParser(
    prog='Program',
    description='Url shorter CLI interface'
)

group = parser.add_mutually_exclusive_group()

group.add_argument('-s', '--shorten')
group.add_argument('-r', '--resolve')

args = parser.parse_args()

if args.shorten:
    print(core.create_url(args.shorten))
elif args.resolve:
    print(core.search_url(args.resolve))
