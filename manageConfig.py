from configManager import ConfigManager
config_manager = ConfigManager("config.ini")

while(True):
    mode = input('Select mode: add_webhook, remove_webhook, show_active_webhooks, add_feed, show_active_feeds, remove_feed, exit')

    if mode == 'add_webhook':
        input_url = input('enter new url --->')
        if len(input_url) > 33 and input_url[:33] == 'https://discord.com/api/webhooks/':
            if config_manager.get_objects_from_section('webhook_urls').count(input_url) == 0:
                config_manager.add_object_to_section('webhook_urls', input_url)
                print('webhook has been added')
            else:
                print('Error: webhook is already active')
        else:
            print('input isn´t a valid Discord webhook url')

    elif mode == 'remove_webhook':
        print('currently active webhooks:')
        for i in config_manager.get_objects_from_section('webhook_urls'):
            print(i)
        input_url = input('enter url to remove --->')
        if not config_manager.get_objects_from_section('webhook_urls').count(input_url) == 0:
            config_manager.remove_object_from_section('webhook_urls', input_url)
            print('webhook has been removed successfully')
        else:
            print('Error: there is no active Webhook with the url: ' + input_url)

    elif mode == 'show_active_webhooks':
        print('currently active webhooks:')
        for i in config_manager.get_objects_from_section('webhook_urls'):
            print(i)
    
    elif mode == 'exit':
        break

    else:
        print('please enter valid mode')