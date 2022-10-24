import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument("interval",type=int, help="The number of times to pull data per
            day. 1 or an even number between 2 and 24.")
    parser.add_argument("listing_url", type=url, help='The ebay listing url.')
    return parser

parser = argparse.ArgumentParser()

if __name__ == "__main__":
    arg_parser = create_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    print(f"{parsed_args = }")
