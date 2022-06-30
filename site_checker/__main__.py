from .cli import display_result, parse_args
import sys

def main():
    args = parse_args(sys.argv[1:])
    urls = build_list(args)
    if not urls:
        print('No sites entered. See help.')
        exit()
    for url in urls:
        display_result(url)

def build_list(args) -> list:
    urls = args.urls
    # add urls from a file
    return urls

if __name__ == '__main__': main()