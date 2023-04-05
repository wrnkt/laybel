### Ebay Listing Tracker

#### ANALYSIS  
> :warning: **eBay changes HTML structure regularly. Will require too much upkeep to
maintain code to get info by element.**    
To verify this and possibly find a workaround:  
1. Scrape listings over and over.  
2. Simplify them to their base tag structure without item specifics.  
3. Analyze them to see the rate that the page setup changes and how.  

> ****Using AI to process a screenshot of the page may work, as the page
appearance is generally the same no matter the elements.****


#### Overview

Given an eBay listing URL  
Pull and store at given interval:  
- title
- current auction price
- buy it now currently active?
- buy it now price
- watchers
- number of bids

Generate a graph of the pricing.  
Draw correlation between time until listing end and current highest bid.  

