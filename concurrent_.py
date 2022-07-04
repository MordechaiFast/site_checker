from site_checker.cli import parse_args, display_result
from pathlib import Path
import asyncio
import sys


def main(args):
    args = parse_args(args)
    urls = build_list(args)
    if not urls:
        print('No sites entered. See help.')
        exit()
    asyncio.run(asynchronous_check(urls))

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

async def asynchronous_check(urls):
    async def check(url):
        error = None
        try:
            online = await site_online(url)
        except Exception as err:
            online = False
            error = err
        display_result(url, online, error)
    
    await asyncio.gather(*(check(url) for url in urls))

from urllib.parse import urlparse
import aiohttp

async def site_online(url, timeout=2) -> bool:
    """Returns True if the target url is online.
    
    If the target is not online, the request's error is passed along.
    """
    parser = urlparse(url)
    host = parser.netloc or parser.path.split('/')[0]
    error = None
    for scheme in ('http', 'https'):
        url = scheme + '://' + host
        async with aiohttp.ClientSession() as session:
            try:
                await session.head(url, timeout=timeout)
                return True
            except Exception as err:
                error = err
    if error:
        raise error

if __name__ == '__main__': main(sys.argv[1:])