package com.tanchee;

import java.nio.file.*;
import java.nio.charset.*;

import java.util.logging.Logger;


import java.io.IOException;
import com.gargoylesoftware.htmlunit.*;
import com.gargoylesoftware.htmlunit.html.*;

import org.apache.hc.client5.http.auth.CredentialsProvider;

public class PageSaver {
    
    public String getListing(String url) throws IOException
    {
        Logger.getLogger("com.gargoylesoftware.htmlunit").setLevel(java.util.logging.Level.OFF);
        Logger.getLogger("org.apache.http").setLevel(java.util.logging.Level.OFF);

        String content = null;

        try(WebClient webClient = new WebClient(BrowserVersion.CHROME))
        {
            webClient.getOptions().setThrowExceptionOnScriptError(false);
            webClient.getOptions().setThrowExceptionOnFailingStatusCode(false);

            HtmlPage page = webClient.getPage(url);

            WebResponse response = page.getWebResponse();
            content = response.getContentAsString();

            //Path path = Paths.get("tests/output.html");

            //writeToFile(content, path);

            //System.out.println(getListingTitle(page));

            System.out.println("Got page.");

            // System.out.println(getListingTitle(page));
        }

        return content;
    }

    public static void writeToFile(String content, Path path)
    {
        try {
            Files.writeString(path, content, StandardCharsets.UTF_8);
        } catch (IOException e)
        {
            System.out.println("Invalid path.");
        }
    }
}
