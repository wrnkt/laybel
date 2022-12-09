package com.tanchee;

import java.io.IOException;
import com.gargoylesoftware.htmlunit.WebClient;
import com.gargoylesoftware.htmlunit.html.HtmlPage;

public class ListingRetriever
{ 
    public EbayListing getListing(String url) throws IOException
    {
        try(WebClient webClient = new WebClient())
        {
            HtmlPage page = webClient.getPage(url);
        }

        return EbayListing.test();
    }
}
