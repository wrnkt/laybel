package com.tanchee;

import java.nio.file.*;
import java.nio.charset.*;

import java.util.logging.Logger;


import java.io.IOException;
import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;

import org.apache.hc.client5.http.auth.CredentialsProvider;

public class ListingRetriever
{ 
    public static String testUrl = "https://www.ebay.com/itm/304733347369?hash=item46f385de29:g:YWoAAOSwI0Zjk6PT";

    public static EbayListing getListing(String url) throws IOException
    {
        Logger.getLogger("com.gargoylesoftware.htmlunit").setLevel(java.util.logging.Level.OFF);
        Logger.getLogger("org.apache.http").setLevel(java.util.logging.Level.OFF);

        try(WebClient webClient = new WebClient(BrowserVersion.CHROME))
        {
            webClient.getOptions().setThrowExceptionOnScriptError(false);
            webClient.getOptions().setThrowExceptionOnFailingStatusCode(false);

            HtmlPage page = webClient.getPage(url);

            WebResponse response = page.getWebResponse();
            String content = response.getContentAsString();

            Path path = Paths.get("tests/output.html");

            writeToFile(content, path);

            //System.out.println(getListingTitle(page));

            System.out.println("Got page.");

            // System.out.println(getListingTitle(page));
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

    public static void writeToFile(String content, Path path)
    {
        try
        {
            Files.writeString(path, content, StandardCharsets.UTF_8);
        }
        catch (IOException e)
        {
            System.out.println("Invalid path.");
        }
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
