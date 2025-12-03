"""
Main Discord Bot File
Handles bot initialization, commands, and events
"""

import discord
from discord.ext import commands
import logging
from config import DISCORD_TOKEN, BOT_PREFIX

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create bot with intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=BOT_PREFIX, intents=intents)

# ============ BOT EVENTS ============

@bot.event
async def on_ready():
    """Called when the bot successfully logs in"""
    logger.info(f'{bot.user} has connected to Discord!')
    logger.info(f'Bot is in {len(bot.guilds)} guild(s)')
    
    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name=f"{BOT_PREFIX}help | Made with Python"
        )
    )

@bot.event
async def on_member_join(member):
    """Called when a member joins the server"""
    logger.info(f'{member} joined the server')
    # You can add welcome messages here

@bot.event
async def on_message(message):
    """Called when a message is sent"""
    # Ignore messages from bot
    if message.author == bot.user:
        return
    
    logger.info(f'{message.author}: {message.content}')
    
    # Process commands
    await bot.process_commands(message)

# ============ BOT COMMANDS ============

@bot.command(name='hello', help='Greets the user')
async def hello(ctx):
    """Simple greeting command"""
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command(name='ping', help='Shows bot latency')
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000)
    await ctx.send(f'Pong! 🏓 Latency: {latency}ms')

@bot.command(name='info', help='Shows bot info')
async def info(ctx):
    """Display bot information"""
    embed = discord.Embed(
        title="Bot Information",
        description="A simple Discord bot built with Python",
        color=discord.Color.blue()
    )
    embed.add_field(name="Bot Name", value=bot.user.name, inline=False)
    embed.add_field(name="Prefix", value=BOT_PREFIX, inline=False)
    embed.add_field(name="Servers", value=len(bot.guilds), inline=False)
    embed.add_field(name="Users", value=len(set(bot.get_all_members())), inline=False)
    
    await ctx.send(embed=embed)

@bot.command(name='help', help='Shows all commands')
async def help_command(ctx):
    """Display all available commands"""
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are all available commands:",
        color=discord.Color.green()
    )
    
    for cmd in bot.commands:
        embed.add_field(
            name=f"{BOT_PREFIX}{cmd.name}",
            value=cmd.help or "No description",
            inline=False
        )
    
    await ctx.send(embed=embed)

@bot.command(name='echo', help='Repeats your message')
async def echo(ctx, *, message):
    """Echo a message back"""
    await ctx.send(f"{ctx.author.name} says: {message}")

@bot.command(name='user', help='Shows user info')
async def user_info(ctx, user: discord.User = None):
    """Get information about a user"""
    user = user or ctx.author
    
    embed = discord.Embed(
        title=f"User Information: {user.name}",
        color=discord.Color.purple()
    )
    embed.add_field(name="Username", value=user.name, inline=False)
    embed.add_field(name="ID", value=user.id, inline=False)
    embed.add_field(name="Created", value=user.created_at.strftime("%Y-%m-%d"), inline=False)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    
    await ctx.send(embed=embed)

# ============ ERROR HANDLING ============

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'Missing required argument: {error.param}')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'Command not found. Type {BOT_PREFIX}help for available commands.')
    else:
        logger.error(f'Error: {error}')
        await ctx.send('An error occurred while processing your command.')

# ============ RUN BOT ============

def run_bot():
    """Start the bot"""
    if DISCORD_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        logger.error('Please set your DISCORD_TOKEN in the .env file!')
        return
    
    try:
        bot.run(DISCORD_TOKEN)
    except Exception as e:
        logger.error(f'Failed to start bot: {e}')

if __name__ == '__main__':
    run_bot()
