import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# Get the bot token from environment variables
TOKEN = os.getenv("BOT_TOKEN")
