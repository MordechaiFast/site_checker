from .cli import display_list, parse_args
import sys

args = parse_args(sys.argv[1:])
display_list(args.urls)