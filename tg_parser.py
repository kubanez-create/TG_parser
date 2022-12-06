"""Parcer for all your telegram chats.

It takes user-provided phrase as a command line argument 
in a string format or no argument
(in this case the default one is used) and searches this phrase
in all telegram's chats you follow.
Perfoms fuzzy search every 20 minutes (you can change this figure as you like).
Must be stopped manually because of an infinite loop.

Works only given your personal bot API!

Needs Telethon library for work so follow its installation 
instructions https://docs.telethon.dev/en/stable/basic/installation.html

Global args:
    TIME_TO_SLEEP (int): period between updates
    session_name (str): anything you like, default "anon"
    api_id (int): your api_id
    api_hash (str): your api_hash
"""

import logging
import os
import sys
import time

from dotenv import load_dotenv
from telethon.sync import TelegramClient
from telethon.utils import get_display_name

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

load_dotenv()

TIME_TO_SLEEP: int = 600 * 2
session_name: str = "anon"
api_id: int = int(os.getenv("api_id"))
api_hash: str = str(os.getenv("api_hash"))


def main(lookup: str = "сдам квартиру") -> None:
    """Search for smth in all your TG chats.

    Args:
        lookup (str): python string
    """
    base_message: str = ""
    client: TelegramClient = TelegramClient(session_name, api_id, api_hash)
    client.start()

    while True:

        message = client.get_messages(None, search=lookup)
        if message[0].message != base_message:
            group_name: str = get_display_name(message[0].chat)
            text: str = (
                f"New message: {message[0].message}."
                f"Date & time: {message[0].date}."
                f"Group: {group_name}."
            )
            client.send_message("me", text)
            base_message = text
        time.sleep(TIME_TO_SLEEP)


if __name__ == "__main__":
    # Ensure correct usage
    if len(sys.argv) > 2:
        sys.exit("Usage: python message_parser_bot.py FILENAME")
    elif len(sys.argv) == 1:
        main()
    lookup: str = str(sys.argv[1])
    main(lookup)
