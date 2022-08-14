import discord
from discord.ext import commands

class Cogs_cmds(commands.Cog):
    """Commands for load, unload, and reload cogs"""
    def __init__(self, client):
        self.client = client

    # load cogs
    @commands.command()
    @commands.has_role("Moderators")
    async def load(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"`{extension}` has been loaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        self.client.load_extension(f'cogs.{extension}')
        print("Loading cogs...")

    # unload cogs
    @commands.command()
    @commands.has_role("Moderators")
    async def unload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"`{extension}` has been unloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        self.client.unload_extension(f'cogs.{extension}')
        print("Unloading cogs...")

    # reload cogs
    @commands.command()
    @commands.has_role("Moderators")
    async def reload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"`{extension}` has been reloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f"cogs.{extension}")
        print("Reloading cogs...")


def setup(client):
    client.add_cog(Cogs_cmds(client))