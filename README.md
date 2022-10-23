### PriceTracker

Pull and store at given interval:
- current price
- watchers
- sell price
given an eBay listing URL

Generate a graph of the pricing.
Draw correlation between time until listing end and current highest bid.

### Usage
```console
$ ./pricetrack <url> <interval>
```
*<interval>: multiple of 2 <= 24*
