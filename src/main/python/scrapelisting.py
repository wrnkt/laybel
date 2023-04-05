#!/usr/bin/python3
import sys
import argparse

from pprint import pprint

import cProfile
import pstats

import time

import re

import urllib
import requests
from bs4 import BeautifulSoup

from threading import Timer

#######
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

#######
# SETUP

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


def sleep_delay(interval: int) -> int:
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
    print(f"[LOG]: Printing to \n{file_path}")
    with open(file_path, "w") as file:
        print(printable, file=file)

#################
# QUERY DICTIONARY

QUERY_DICTIONARY = {
}

###################
# QUERY DEFINITIONS
# *reference by dictionary entry
# soup object -> string or number

def add_query(query_fn):
    fn_ref_name = query_fn.__name__.replace("get_", "")
    QUERY_DICTIONARY[fn_ref_name] = query_fn
    def wrapper(*args, **kwargs):
        return query_fn(*args, **kwargs)
    return wrapper

def query_not_implemented(query):
    def wrapper(*args, **kwargs):
        return query(*args, **kwargs) + f"ERROR: {query.__name__} not implemented."
    return wrapper

@add_query
def get_title(soup: BeautifulSoup) -> str:
    """Get title from eBay listing page"""
    output = str(soup.find("div", {"class": "vim x-item-title"}).text)
    output = output.strip()
    return output

@add_query
def get_current_auction(soup: BeautifulSoup) -> str:
    """Get current auction price from eBay listing page"""
    output = str(soup.find("span", {"itemprop": "price"}).text)
    output = output[3:]
    return output

@add_query
def get_buy_it_now(soup: BeautifulSoup) -> str:
    """Get Buy It Now price if it exists"""
    try:
        output = str(soup.find("span", {"id": "prcIsum"}).text)
    except:
        return None
    return output

@add_query
def get_number_bids(soup: BeautifulSoup) -> str:
    """Get current number of bids on the listing"""
    try:
        output = str(soup.find("span", {"id": "qty-test"}).text)
    except:
        return "0"
    return output

@add_query
def get_watchers(soup: BeautifulSoup) -> str:
    """Get current number of listing watchers"""
    try:
        notification = soup.find("div", {"id":
                                         "vi_notification_new"})
        notification_span_tag_list = notification.findChildren("span")
        for span in notification_span_tag_list:
            if "watch" in span.text:
                match = re.search(r'\d+', span.text)
                output = match.group()
    except:
        return "0"
    return output


##########
# GET INFO

def int_to_word(number: int):
    mapping = {
            "1":"one",
            "2":"two",
            "3":"three",
            "4":"four",
            "5":"five",
            "6":"six",
            "7":"seven",
            "8":"eight",
            "9":"nine"}
    return mapping[number]

def send_scrape_to_file(url: str, info_requests: list[str], output_dir: str):
    """Sends scrape to output file"""
    results = scrape_to_dict(url, info_requests)
    
    file_input = ""

    def construct_file_path(results, output_dir):
        date_accessed = time.ctime(time.time())
        date_accessed = date_accessed.replace(" ", "-")
        title = results["title"].lower()
        for character in title:
            if character.isdigit():
                title = title.replace(character, int_to_word(character))
            if character == " ":
                title = title.replace(character, "-")
            if character == "/":
                title = title.replace(character, "-")


        return output_dir + title + "-" + date_accessed

    file_path = construct_file_path(results, output_dir)

    for key in sorted(results.keys()):
        #print(key, type(results[key]))
        query_result = results[key]
        if query_result == None:
            query_result = "None"
        file_input = file_input + key + ": " + query_result + "\n"

    log_to_file(file_input, file_path)



def scrape_to_dict(url: str, info_requests: list[str]=["title"]) -> dict:
    """performs a list of queries given ebay listing url and returns a
    dictionary"""

    results = {}

    listing_html = requests.get(url)
    listing_soup = BeautifulSoup(listing_html.content, 'html.parser')

    date_accessed = time.ctime(time.time())
    results["url"] = url
    results["access_date"] = date_accessed

    for request in info_requests:
        query_result = QUERY_DICTIONARY[request](listing_soup)
        results[request] = query_result

    return results


def is_url(url: str):
    """validate a URL"""
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
        print()
        print("[LOG]: VALID URL")
        query_list = ["title", "current_auction", "buy_it_now", "watchers", "number_bids"]
        # WARNING: "sampleoutputs/" reference is now broken.
        send_scrape_to_file(url, query_list, "sampleoutputs/") 
        print("\n[LOG]:")
        print("Scrape result:")
        pprint(scrape_to_dict(url, query_list))
    else:
        raise Exception("INVALID URL")
    
