from requests import Session
from bs4 import BeautifulSoup
import logging

def logging_setup():
    logging.basicConfig(filename="log.log", level=logging.INFO)

def print_to_file(content, file_name: str):
    with open(file_name, 'w') as output_file:
        print(content, file=output_file)

def get_verify_screen():
    with Session() as s:
        site = s.get("https://www.ebay.com/signin/")
        site_soup = BeautifulSoup(site.content, 'html.parser')
        # WARNING: Fix this output location.
        print_to_file(site_soup.prettify(), "output.txt")

if __name__ == "__main__":
    #logging_setup()
    soup_test()
