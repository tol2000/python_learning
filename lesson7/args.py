# https://devdocs.io/python~3.9/library/argparse#action

import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.version = "Version 1.0"
parser.add_argument(
    "-p", "--dir", "--path",
    dest='path_for_list',
    action="store",
    type=str,
    help="directory for list",
    required=True
)
parser.add_argument(
    "-V", "--verbose"
    , action="store_true"
    , help="Show more info"
)
parser.add_argument(
    "-v", "--version"
    , action="version"
    , help="Show version info"
)
parser.add_argument(
    "-a",
    action="append_const",
    const=1
)
parser.add_argument(
    "-c",
    action="count"
)

args = parser.parse_args()
print(args)

print(f"List of {args.path_for_list}:")
i_dir = Path(args.path_for_list).iterdir()
if args.verbose:
    for p in i_dir:
        print(f'  {p}')
else:
    print(list(i_dir))
