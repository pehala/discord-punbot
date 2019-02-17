import re
from html import unescape

import requests
from disco.bot import Plugin


class PunBot(Plugin):

    def __init__(self, bot, config):
        super().__init__(bot, config)
        bot.config.commands_require_mention = False
        self.pattern = re.compile('(?<=&quot;).*(?=&quot)')

    # Which includes command argument parsing
    @Plugin.command('pun!')
    def on_echo_command(self, event):
        r = requests.get('https://www.punoftheday.com/cgi-bin/arandompun.pl')
        msg = self.pattern.findall(r.text)[0]
        event.msg.reply(unescape(msg))
