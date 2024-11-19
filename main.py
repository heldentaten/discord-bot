import discord
from discord.ext import commands
from commands.search import search
from commands.info import info
from config.settings import TOKEN
from dotenv import load_dotenv

load_dotenv()  # Load .env file containing the bot token

# Create intents and make sure message_content intent is enabled
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Initialize bot with the correct intents
bot = commands.Bot(command_prefix="/mybot ", intents=intents)

# Register commands from the separate files
bot.add_command(search)
bot.add_command(info)

@bot.event
async def on_ready():
    # Set the bot's activity status to 'Listening' to "/mybot info"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/mybot info"))
    print(f'Logged in as {bot.user}')

# Run the bot with the token
bot.run(TOKEN)
