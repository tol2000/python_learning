import argparse

# -d --hello /par2=3 --opt 4

parser = argparse.ArgumentParser()
parser.add_argument(
    "d",
    metavar="dir",
    type=str,
    help="directory for list"
)
# parser.add_argument(
#     "hello",
#     metavar="dir",
#     required=False
# )
# parser.add_argument(
#     "par2",
#     metavar="par2",
#     required=False
# )
# parser.add_argument(
#     "opt",
#     metavar="opt",
#     required=False
# )

args = parser.parse_args()
print(args)
