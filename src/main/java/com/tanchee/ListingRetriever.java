package com.tanchee;

import java.io.IOException;
import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;

import org.apache.hc.client5.http.auth.CredentialsProvider;

public class ListingRetriever
{ 
    public static String testUrl = "https://www.ebay.com/itm/165813852256?hash=item269b469860:g:b~YAAOSwpcVjjLAo";

    public static EbayListing getListing(String url) throws IOException
    {
        try(WebClient webClient = new WebClient())
        {
            HtmlPage page = webClient.getPage(url);

            System.out.println(getListingTitle(page));
        }


        return EbayListing.test();
    }

    public static String getListingTitle(HtmlPage page)
    {
        final String divIdentifier = "vim x-item-title";
        HtmlDivision titleDiv = page.getHtmlElementById(divIdentifier);
        String text = titleDiv.getTextContent();

        return text;
    }

    public static void main(String[] args)
    {
        try
        {
            getListing(testUrl);
        }
        catch (IOException e)
        {
            System.out.println("Could not retrieve page");
        }
    }
}
