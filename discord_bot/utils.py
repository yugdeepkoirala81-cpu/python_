"""
Utility functions for the Discord bot
"""

import discord
from discord.ext import commands
import random

def get_random_color():
    """Generate a random Discord embed color"""
    return discord.Color.from_rgb(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

def create_embed(title, description, color=None):
    """Create a standardized embed"""
    return discord.Embed(
        title=title,
        description=description,
        color=color or get_random_color()
    )

def format_user_mention(user):
    """Format a user mention"""
    return f"<@{user.id}>"

def get_member_status(member):
    """Get member's current status"""
    return str(member.status).capitalize()
