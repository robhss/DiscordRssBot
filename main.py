from discord_webhook import DiscordWebhook, DiscordEmbed
from rss_check import rss_check
from configManager import ConfigManager
import time

config_manager = ConfigManager("config.ini")


def post():
    """
    Takes a List of Discord Webhook Urls and gets the newest News form Crunchyroll to post on your Discord Server
    :param urls:
    :return:
    """

    feeds = config_manager.get_urls_from_section("feeds")

    for feedKey in feeds:

        entries = rss_check(feeds[feedKey], feedKey)

        for item in entries:
            webhook = DiscordWebhook(url='')
            content = DiscordEmbed()
            content.set_title(item['title'])
            content.set_author(item['author'])
            content.set_url(item['link'])
            content.set_image(item['media_thumbnail'][0]['url'])
            content.set_timestamp()

            webhook.add_embed(content)

            webhooks = config_manager.get_urls_from_section('webhooks')
            for key in webhooks:
                webhook.url = webhooks[key]
                webhook.execute()

            print(f'\n{time.strftime('%H:%M', time.localtime())} {item['title']} was posted')

        if len(entries) == 0:
            print(f'\n{time.strftime('%H:%M', time.localtime())}  RSS-feed was checked, there is nothing new to post')


while True:
    post()
    time.sleep(300)
