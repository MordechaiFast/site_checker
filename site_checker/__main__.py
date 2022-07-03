from pathlib import Path
from .cli import display_result, parse_args
import sys


def main(args):
    args = parse_args(args)
    urls = build_list(args)
    if not urls:
        print('No sites entered. See help.')
        exit()
    for url in urls:
        display_result(url)

def build_list(args) -> list:
    urls = args.urls
    if args.file:
        urls += read_file(args.file)
    return urls

def read_file(file) -> list:
    if not Path(file).is_file():
        print(f'Can\'t find file "{file}".')
        return []
    with open(file) as file:
        urls = [url.strip() for url in file]
    """ except OSError as err:
        print(f'Can\'t read from file "{file}" :(', err) """
    return urls

if __name__ == '__main__': main(sys.argv[1:])