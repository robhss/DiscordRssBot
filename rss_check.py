import feedparser
import os
import requests


def rssCheck(url: str, index) -> set:
    """
    sources new rss feed form designated website
    :return: set of rss items
    """

    if os.path.exists("legacyFeed_{}.xml".format(index)):
        currentChannel = feedparser.parse(url)
        legacyChannel = feedparser.parse("legacyFeed_{}.xml".format(index))
        result = []

        
        for item in currentChannel['entries']:
            tracker = False
            for legacyitem in legacyChannel['entries']:
                if item['title'] == legacyitem['title']:
                    tracker = True
            if tracker == False:
                 result.append(item)

        saveFeed(url, index)
        return result
            
    else:
        saveFeed(url, index)
        return []

def saveFeed(url, index):
    feed = requests.get(url)
    with open("legacyFeed_{}.xml".format(index), "wb") as f:
                f.write(feed.content)

rssCheck("https://cr-news-api-service.prd.crunchyrollsvc.com/v1/de-DE/rss")

