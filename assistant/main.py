from bot import Bot

Bot = Bot("Priscila")
while True:
    phrase = Bot.bot_listener()
    resp = Bot.bot_tinker(phrase)
    Bot.bot_speaker(resp)
    if resp == 'tchau':
        break