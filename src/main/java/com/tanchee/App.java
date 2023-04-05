package com.tanchee;

import java.nio.file.*;

import java.io.IOException;

import java.math.BigDecimal;
import java.time.LocalDateTime;


public class App 
{
    public static void main(String[] args)
    {
        PageSaver ps = new PageSaver();
        try {
            ps.saveListing("https://www.ebay.com/p/5054515552?iid=225512246897",
                            Paths.get("tests/output.html"));
        } catch (IOException e) {
            System.out.println(e);
        }
        /*
        EbayListing testListing = EbayListing.test();
        System.out.println("Hello World!");
        System.out.println(testListing);
        */
    }
}
