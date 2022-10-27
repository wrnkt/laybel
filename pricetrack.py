#!/usr/bin/python3
import sys
import argparse

from pprint import pprint

import cProfile
import pstats

import urllib
import requests
from bs4 import BeautifulSoup

from threading import Timer


# DEBUG
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

# SETUP

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
    """Get necessary time delay between polling based on interval."""
    seconds_in_day = 86400
    second_delay = 0
    if interval == 1:
       second_delay = seconds_in_day
    elif (1 < interval < 24) and (interval % 2 == 0):
        second_delay = seconds_in_day // interval 
    else:
        raise NotImplementedError("Interval has to be 1 or an even number between 2 and 24.")

    return second_delay


########
# OUTPUT
def log_to_file(printable: str, file_path: str="output.txt"):
    """Clear file and write to it"""
    print(f"Printing to {file_path}")
    with open(file_path, "w") as file:
        print(printable, file=file)

###################
# QUERY DEFINITIONS
# *reference by dictionary entry
# soup object -> string or number

def query_not_implemented(query):
    def wrapper(*args, **kwargs):
        return query(*args, **kwargs) + f"ERROR: {query.__name__} not implemented."
    return wrapper

def get_listing_title(soup: BeautifulSoup) -> str:
    """Get title from eBay listing page"""
    output = str(soup.find("div", {"class": "vim x-item-title"}))
    return output

@query_not_implemented
def get_current_auction(soup: BeautifulSoup) -> str:
    output=""
    """Get current auction price from eBay listing page"""
    return output


#################
# QUERY DICTIONARY
QUERY_DICTIONARY = {
        "title": get_listing_title,
        "current-auction": get_current_auction
}

##########
# GET INFO

def get_info_from_url(
    url: str="https://www.ebay.com/itm/265954994896?hash=item3dec272ad0:g:eLUAAOSwYARjWDNd",
    info_requests: list[str]=["title","current-auction"]):
    """Performs a list of queries given listing URL"""

    listing_html = requests.get(url)
    listing_soup = BeautifulSoup(listing_html.content, 'html.parser')

    output = ""

    for request in info_requests:
        query_result = QUERY_DICTIONARY[request](listing_soup)
        output += f"{request = }\n{query_result = }\n\n"

    log_to_file(output)


def is_url(url: str):
    return True

    
def log_price(interval: int):
     pass

######
# MAIN
if __name__ == "__main__":

    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])

    url = parsed_args.listing_url

    if parsed_args.interval:
        interval = parsed_args.interval
    else:
        interval = 1    # default

    if is_url(url):
        print("VALID URL")
        get_info_from_url(url)
    else:
        raise Exception("INVALID URL")
    

