import re
from html import unescape

import requests
from disco.bot import Plugin


class PunBot(Plugin):

    def __init__(self, bot, config):
        super().__init__(bot, config)
        bot.config.commands_require_mention = False
        self.pun_pattern = re.compile(r'(?<=&quot;).*(?=&quot)')

    # Which includes command argument parsing
    @Plugin.command('pun!')
    def on_echo_command(self, event):
        request = requests.get('https://www.punoftheday.com/cgi-bin/arandompun.pl')
        text = request.text
        msg = self.pun_pattern.findall(text)[0]
        event.msg.reply(unescape(msg))

    @Plugin.command('punsource!')
    def on_echo_command(self, event):
        event.msg.reply("https://www.punoftheday.com/")
