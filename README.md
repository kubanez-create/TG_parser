# TG_parser

Parcer for all your telegram chats.
It takes user-provided phrase as a command line argument 
in a string format or no argument
(in this case the default one is used) and searches this phrase
in all telegram's chats you follow.
Perfoms fuzzy search every 20 minutes (you can change this figure as you like).
Must be stopped manually because of an infinite loop.

Works only given your personal bot API!

Needs Telethon library for work so follow its [installation 
instructions](https://docs.telethon.dev/en/stable/basic/installation.html).

Global args:
- TIME_TO_SLEEP (int): period between updates
- session_name (str): anything you like, default "anon"
- api_id (int): your api_id
- api_hash (str): your api_hash
