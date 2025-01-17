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
    url = core.search_url(args.resolve)
    if url:
        print(url)
    else:
        print(f"ID '{args.resolve}' not found")
else:
    parser.print_help()