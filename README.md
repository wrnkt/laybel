### Ebay Listing Logger

Pull and store at given interval:
- title
- current auction price
- buy it now price
- watchers
- number of bids
given an eBay listing URL

Generate a graph of the pricing.
Draw correlation between time until listing end and current highest bid.

### Usage
```console
$ python3 loglisting.py <url> <interval>
```
*<interval>: multiple of 2 <= 24*
