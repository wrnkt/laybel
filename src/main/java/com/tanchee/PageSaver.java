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

            System.out.println("Got page.");
        }

        return content;
    }

    public void saveListing(String url, Path path) throws IOException {
            writeToFile(getListing(url), path);
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
