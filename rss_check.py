from typing import List, Any

import feedparser
import os
import requests


def rss_check(url: str, feed_index: str) -> list[Any]:
    """
    sources new rss feed form designated website
    :return: set of rss items
    """

    if os.path.exists("legacyFeed_{}.xml".format(feed_index)):
        current_channel = feedparser.parse(url)
        legacy_channel = feedparser.parse("legacyFeed_{}.xml".format(feed_index))
        result = []

        for item in current_channel['entries']:
            tracker = False
            for legacy_item in legacy_channel['entries']:
                if item['title'] == legacy_item['title']:
                    tracker = True
            if not tracker:
                result.append(item)

        save_feed(url, feed_index)
        return result

    else:
        save_feed(url, feed_index)
        current_channel = feedparser.parse(url)
        return [current_channel['entries'][0]]


def save_feed(url, index):
    feed = requests.get(url)
    with open("legacyFeed_{}.xml".format(index), "wb") as f:
        f.write(feed.content)