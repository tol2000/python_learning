import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    "path",
    metavar="path",
    type=str,
    help="directory for list"
)
parser.add_argument(
    "-v", "--verbose"
    , action="store_true"
    , help="Show more info"
)

args = parser.parse_args()
print(args)

print(f"List of {args.path}:")
i_dir = Path(args.path).iterdir()
if args.verbose:
    for p in i_dir:
        print(f'  {p}')
else:
    print(list(i_dir))
