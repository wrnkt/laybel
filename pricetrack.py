#!/usr/bin/python3
import sys
import argparse


def log_info(debugmode:bool = False):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if (debugmode):
                print(f"[LOG] calling {func.__name__}")
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outer_wrapper

@log_info(debugmode=True)
def create_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
            "-i",
            "--interval", 
            type=int,
            help="""The number of times to pull data per day. 1 or an even
            number between 2 and 24.""")
    parser.add_argument("listing_url", type=str, help='The ebay listing url.')
    return parser


if __name__ == "__main__":

    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    interval = 1

    if parsed_args.interval:
        interval = parsed_args.interval

    url = parsed_args.listing_url

    

