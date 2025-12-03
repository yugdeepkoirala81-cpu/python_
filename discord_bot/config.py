"""
Discord Bot Configuration
Store sensitive data like tokens in environment variables
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Bot Token - Keep this SECRET!
# Add your token to a .env file: DISCORD_TOKEN=your_token_here
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Bot prefix for commands
BOT_PREFIX = '!'

# Bot intents (what the bot can do)
INTENTS = {
    'message_content': True,      # Read message content
    'members': True,               # Access member info
    'guilds': True,                # Access guild info
    'messages': True,              # Send/receive messages
}

# Logging configuration
LOG_LEVEL = 'INFO'
