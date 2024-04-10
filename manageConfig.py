import os

from configManager import ConfigManager

config_manager = ConfigManager("config.ini")

while True:
    mode = input(
        'Select mode: add_webhook, remove_webhook, show_active_webhooks, add_feed, remove_feed, show_active_feeds, '
        'exit \n -->')

    if mode == 'add_webhook':
        input_url = input('enter new url \n -->')

        if len(input_url) > 33 and input_url[:33] == 'https://discord.com/api/webhooks/':

            if not config_manager.is_url_in_section("webhooks", input_url):
                config_manager.add_url_to_section('webhooks', input_url)
                print('webhook has been added')

            else:
                print('Error: webhook is already active')

        else:
            print('input isn´t a valid Discord webhook url')

    elif mode == 'remove_webhook':
        print('currently active ç:')
        webhooks = config_manager.get_urls_from_section('webhooks')

        for key in webhooks:
            print(f"[{key}] {webhooks[key]}")

        input_key = input('enter key to remove \n -->')

        if input_key in webhooks.keys():
            config_manager.remove_url_from_section('webhooks', input_key)
            print('webhook has been removed successfully')

        else:
            print('Error: there is no active webhook with the url: ' + input_key)

    elif mode == 'show_active_webhooks':
        print('currently active webhooks:')
        webhooks = config_manager.get_urls_from_section('webhooks')

        for key in webhooks:
            print(f"[{key}] {webhooks[key]}")

    elif mode == 'add_feed':
        input_url = input('enter url to add \n -->')
        if not config_manager.is_url_in_section("feeds", input_url):
            config_manager.add_url_to_section('feeds', input_url)
            print('feed has been added')
        else:
            print('Error: feed is already active')

    elif mode == 'remove_feed':
        print('currently active feeds:')
        feeds = config_manager.get_urls_from_section('feeds')

        for key in feeds:
            print(f"[{key}] {feeds[key]}")

        input_key = input('enter key to remove \n -->')

        if input_key in feeds.keys():
            config_manager.remove_url_from_section('feeds', input_key)

            if os.path.exists(f"legacyFeed_{input_key}.xml"):
                os.remove(f"legacyFeed_{input_key}.xml")

            print('feed has been removed successfully')

        else:
            print('Error: there is no active feed with the url: ' + input_key)

    elif mode == 'show_active_feeds':
        print('currently active feeds:')
        feeds = config_manager.get_urls_from_section('feeds')

        for key in feeds:
            print(f"[{key}] {feeds[key]}")

    elif mode == 'exit':
        break

    else:
        print('please enter valid mode')
