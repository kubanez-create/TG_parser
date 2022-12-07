# TG_parser

Given you have a user's bot you can follow some particular topic rather
then group or person, get periodic updates on it.
It takes user-provided phrase as a command line argument 
in a string format or no argument
(in this case the default one is used) and searches this phrase
in all telegram's chats you follow.
It perfoms fuzzy search every 20 minutes (you can change this figure as you like)
and sends result into your saved messages or doesn't send anything if
there wasn't any new one.
Currently this program retreives only one last message on a followed topic.
This behavior might change in the future or you may do it yourself, it's easy.
Must be stopped manually because of an infinite loop.

Works only given your personal bot API!

Needs Telethon library for work so follow its [installation 
instructions](https://docs.telethon.dev/en/stable/basic/installation.html).

Global args:
- TIME_TO_SLEEP (int): period between updates
- session_name (str): anything you like, default "anon"
- api_id (int): your api_id
- api_hash (str): your api_hash

## TODO
Turn the program into an actual tg bot with instuctions and prompts so
everyone can use it and not only python-proficient crowd.
