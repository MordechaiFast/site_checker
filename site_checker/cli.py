from argparse import ArgumentParser, Namespace
from typing import List
from .checker import site_online


def parse_args(args: str) -> Namespace:
    parser = ArgumentParser(
        prog='site on-line checker (site_checker)',
        description='A command-line script for checking '
        'if multiple websites are on-line or not'
    )
    parser.add_argument(
        '-u', '--urls',
        metavar='urls',
        nargs='+',
        type=str,
        default=[],
        help='enter one or more site URLs',
    )
    return parser.parse_args(args)

def display_result(url) -> None:
    print(f'The site "{url}" is:', end=' ')
    try:
        if site_online(url):
            print('online!')
    except Exception as err:
        print('not accessable', err)