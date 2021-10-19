# Hindi_language_web_scraper

This repository contains code for various scraping algorithms used for collecting Hindi language text data for the [RESPIN](https://respin.iisc.ac.in/) project at [SPIRE Lab](https://spire.ee.iisc.ac.in/spire/index.php), IISc Bangalore.

Each of the folders contains Python scripts for the particular method used and the text files:

- ***manual_collection_scraping*** : Text from links that were collected manually and then scraped using the scrape_text.py script.
- ***scrapy_collection_scraping*** : Text from links that were collected using the [Scrapy](https://scrapy.org/) framework, and then scraped using the scrape_text.py script.

***text_statistics_saving*** contains scripts for counting the number of words, number of sentences collected, frequency of each word, and other such statistics.
