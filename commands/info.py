import discord
from discord.ext import commands

@commands.command()
async def info(ctx):
    """Displays available commands."""
    info_message = """
    **Available Commands:**
    - /mybot search <item> : Search for an item on Wowhead (e.g., "/mybot search leichtes leder")
    - /mybot info : Displays this message with available commands.
    """
    await ctx.send(info_message)

    # Delete the user's command message after responding
    await ctx.message.delete()
