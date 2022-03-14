import discord
import os
from discord.ext import commands


#from botalive import botalive
#from botwhoami import botwhoami
#from botregister import botregister
#from isadmin import isadmin

class Bot:
    def __init__(self, logging:object, config:object) -> None:
        self.log = logging
        self.config = config
        
        #Configure bot
            #TODO set from configuration, any intents we might need. Can also set contexts in configuration and do it that way
        intents = discord.Intents(messages=True, guilds=True, members=True) 
            #TODO set description from configuration
        description = '''A placeholder bot description.'''

        self.bot = commands.Bot(command_prefix='!', description=description, intents=intents)

        @self.bot.event
        async def on_ready():
            self.log.info(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
            print('Bot has been started')
        
        @self.bot.command()
        async def load(ctx, extension, self):
            self.bot.load_extension(f'cogs.{extension}')

        @self.bot.command()
        async def unload(ctx, extension, self):
            self.bot.unload_extension(f'cogs.{extension}')

        os.chdir(r"/opt/bits/src")

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                self.bot.load_extension(f'cogs.{filename[:-3]}')

        #Initialize
        self.__start_bot()


    def __start_bot(self) -> None:
        token = self.config.data['bot_settings']['discord_token']
        self.bot.run(token)
