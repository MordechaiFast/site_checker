from argparse import ArgumentParser, Namespace


def parse_args(args: str) -> Namespace:
    parser = ArgumentParser(
        prog='site_checker',
        description='A command-line script for checking '
        'if multiple websites are on-line or not.'
    )
    parser.add_argument(
        '-u', '--urls',
        metavar='URLS',
        nargs='+',
        type=str,
        default=[],
        help='enter one or more URLs of sites to check',
    )
    parser.add_argument(
        '-f', '--file',
        metavar='FILE',
        type=str,
        default='',
        help='enter the name of a file listing URLs of sites to check',
    )
    return parser.parse_args(args)

def display_result(url: str, online: bool, err: Exception = None) -> None:
    print(f'The site "{url}" is:', 'online!' 
            if online else 'not accessable: ' + str(err))