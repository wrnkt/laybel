package com.tanchee;

import java.io.Serializable;
import java.math.BigDecimal;
import java.time.LocalDateTime;
/*
*   [LOG]: VALID URL
*   [LOG]: Printing to 
*   sampleoutputs/houston-astros-fitted-hat-size-seven-one-four-courdory-Thu-Dec--1-22:37:32-2022
*   
*   [LOG]:
*   Scrape result:
*   {'access_date': 'Thu Dec  1 22:37:33 2022',
*    'buy_it_now': None,
*    'current_auction': '$47.00',
*    'number_bids': '0',
*    'title': 'Houston Astros Fitted Hat Size 7 1/4 Courdory',
*    'url': 'https://www.ebay.com/itm/144835035160?hash=item21b8d74018:g:YFoAAOSw3XFjiGi6',
*    'watchers': '1'}
**/

public record EbayListing(String url,
                          String title,
                          BigDecimal currentAuctionPrice,
                          int bids,
                          BigDecimal buyItNowPrice,
                          int watchers,
                          LocalDateTime localAccessDateTime) implements Serializable
{
    public static EbayListing test()
    {
        return new EbayListing(
                "https://www.ebay.com/itm/144835035160?hash=item21b8d74018:g:YFoAAOSw3XFjiGi6",
                "Houston Astros Fitted Hat Size 7 1/4 Courdory",
                new BigDecimal(47.00),
                0,
                new BigDecimal(0),
                1,
                LocalDateTime.now());
    }
}




