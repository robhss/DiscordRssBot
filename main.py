from discord_webhook import DiscordWebhook, DiscordEmbed
from rss_check import rssCheck
from configManager import ConfigManager
import time

config_manager = ConfigManager("config.ini")

def post_webhook(feedUrl):
    """
    Takes a List of Discord Webhook Urls and gets the newest News form Crunchyroll to post on your Discord Server
    :param urls:
    :return:
    """


    entries = rssCheck(feedUrl, config_manager.get_objectindex('feed_urls', i))

    for item in entries:
        webhook = DiscordWebhook(url='')
        content = DiscordEmbed()
        content.set_title(item['title'])
        content.set_author(item['author'])
        content.set_url(item['link'])
        content.set_image(item['media_thumbnail'][0]['url'])
        content.set_timestamp()

        webhook.add_embed(content)
        for url in config_manager.get_objects_from_section('webhook_urls'):
            webhook.url = url
            webhook.execute()

        print('\n' + time.strftime('%H:%M', time.localtime()) +'  ' + item['title'] + ' was posted')

    if len(entries) == 0:
        print('\n' + time.strftime('%H:%M', time.localtime()) + '  RSS-feed was checked, there is nothing new to post')


while True:
    for i in config_manager.get_objects_from_section('feed_urls'):
        post_webhook(i)
    time.sleep(300)
