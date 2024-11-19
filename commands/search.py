import discord
from discord.ext import commands

@commands.command()
async def search(ctx, item):
    """Search for an item on Wowhead and return the link."""
    print(f"Search command triggered with item: {item}")

    # Form the URL for the search
    base_url = "https://www.wowhead.com/cata/de/search"
    search_url = f"{base_url}?q={item.replace(' ', '+')}"

    # Send the response with the search link
    await ctx.send(f"Here is the link for your search: {search_url}")

    # Delete the user's command message after responding
    await ctx.message.delete()
