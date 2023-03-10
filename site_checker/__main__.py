from .cli import parse_args, display_result
from pathlib import Path
from .checker import site_online
import sys


def main(args):
    args = parse_args(args)
    urls = build_list(args)
    if not urls:
        print('No sites entered. See help.')
        exit()
    synchronous_check(urls)

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
    return urls

def synchronous_check(urls):
    for url in urls:
        error = None
        try:
            online = site_online(url)
        except Exception as err:
            online = False
            error = err
        display_result(url, online, error)

if __name__ == '__main__': main(sys.argv[1:])