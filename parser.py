"""Parcer for all your telegram chats.

Accepts command-line parameters. It should be string.
Perfoms fuzzy search every 20 minutes.

Works only given your personal bot API!

Needs Telethon library for work so follow its installation 
instructions https://docs.telethon.dev/en/stable/basic/installation.html

Global args:
    TIME_TO_SLEEP (int): period between updates
    session_name (str): anything you like, default "anon"
    api_id (int): your api_id
    api_hash (str): your api_hash
"""

import time
import os
import sys

import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from dotenv import load_dotenv

from telethon.sync import TelegramClient
from telethon.utils import get_display_name

load_dotenv()

TIME_TO_SLEEP: int = 600 * 2
session_name: str = 'anon'
api_id: int = int(os.getenv('api_id'))
api_hash: str = str(os.getenv('api_hash'))

def main(lookup: str='сдам квартиру') -> None:
    """Search for smth in all you TG chats.

    Args:
        lookup (str): python string
    """
    base_message: str = ''
    client: TelegramClient = TelegramClient(session_name, api_id, api_hash)
    client.start()

    while True:
                
        message = client.get_messages(None, search=lookup)
        if message[0].message != base_message:
            group_name: str = get_display_name(message[0].peer_id)
            text = (f'New message: {message[0].message}'
                    f'{message[0].date}'
                    f'{group_name}')
            client.send_message('me', text)
            base_message = text
        time.sleep(TIME_TO_SLEEP)

if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) > 2:
        sys.exit("Usage: python message_parser_bot.py FILENAME")
    elif len(sys.argv) == 1:
        main()
    lookup = str(sys.argv[1])
    main(lookup)