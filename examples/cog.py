import discord
from discord import app_commands
from discord.ext import commands
from utils import cfg, CosmoContext, transform_context
from utils.framework import whisper


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # up here you can define permission checks
    # i.e mod_and_up()
    # declare guilds this command can be used in
    @app_commands.guilds(cfg.guild_id)
    # add command to the tree
    @app_commands.command(description="Says hello to the user")
    # add description to arguments
    @app_commands.describe(message="The message to send back")
    # this is to turn the interaction object d.py gives into a Context object (ORDER IS IMPORTANT!)
    @transform_context
    @whisper  # make response ephemeral for non mods (ORDER IS IMPORTANT!
    async def say(self, ctx: CosmoContext, message: str):
        await ctx.send_success(message)

    # note: we no longer need a command handler in each cog, this is done globally


async def setup(bot: commands.Bot):
    await bot.add_cog(Greetings(bot))
