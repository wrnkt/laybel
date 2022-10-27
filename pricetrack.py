#!/usr/bin/python3
import sys
import argparse

import cProfile
import pstats

import bs4 as bs4
import requests

from threading import Timer

def time_me(func):
    def wrapper(*args, **kwargs):
        with cProfile.Profile() as pr:
            res = func(*args, **kwargs)
        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        stats.dump_stats(filename=f"[LOG]: profiling {func.__name__}")
        return res
    return wrapper


def log_info(debugmode:bool = False):
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            if (debugmode):
                print(f"[LOG] calling {func.__name__}")
            res = func(*args, **kwargs)
            return res
        return wrapper
    return outer_wrapper

# @time_me
# @log_info(debugmode=True)
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

def get_sleep_delay(interval: int) -> int:
    seconds_in_day = 86400
    second_delay = 0
    if interval == 1:
       second_delay = seconds_in_day
    elif (1 < interval < 24) and (interval % 2 == 0):
        second_delay = seconds_in_day // interval 
    else:
        raise NotImplementedError("Interval has to be 1 or an even number between 2 and 24.")

    return second_delay

def grab_price_from_url(url: str="https://www.ebay.com/itm/265954994896?hash=item3dec272ad0:g:eLUAAOSwYARjWDNd"):
    if is_url(url):
        pass
        print("valid url")
    else:
        raise Exception("INVALID URL PASSED TO {grab_price_from_url.__name__}")

def is_url(url: str):
    return True
    
    
def log_price(interval: int):
     pass


if __name__ == "__main__":

    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    interval = 1

    if parsed_args.interval:
        interval = parsed_args.interval

    url = parsed_args.listing_url

    print(f"{url = } {interval = }")
    print(get_sleep_delay(2))
    grab_price_from_url()

    


