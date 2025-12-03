# Discord Bot

A fully functional Discord bot built with Python using discord.py

## Features

✨ **Core Features:**
- Command system with prefix (`!`)
- User information commands
- Server information
- Status updates
- Error handling
- Embed messages with color
- Member join events

🎮 **Available Commands:**
- `!hello` - Greet the bot
- `!ping` - Check bot latency
- `!info` - Bot information
- `!help` - List all commands
- `!echo [message]` - Repeat a message
- `!user [@user]` - Get user information

## Setup Instructions

### 1. Create Discord Bot Application

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application"
3. Go to "Bot" section and click "Add Bot"
4. Copy the **TOKEN** (keep it SECRET!)
5. Enable these **Intents** under "Privileged Gateway Intents":
   - Message Content Intent
   - Server Members Intent

### 2. Create .env File

Create a `.env` file in the `discord_bot` folder:

```
DISCORD_TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with your actual bot token.

### 3. Install Dependencies

```powershell
cd c:\Users\LENOVO\Desktop\sybau\discord_bot
pip install -r requirements.txt
```

Or manually:
```powershell
pip install discord.py python-dotenv
```

### 4. Run the Bot

```powershell
python main.py
```

You should see:
```
bot_name#1234 has connected to Discord!
Bot is in X guild(s)
```

## Inviting the Bot to Your Server

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to "OAuth2" → "URL Generator"
4. Select scopes: `bot`
5. Select permissions: `Send Messages`, `Read Messages`, `Manage Messages`, `Embed Links`
6. Copy the generated URL and open it in browser
7. Select your server and authorize

## File Structure

```
discord_bot/
├── main.py              # Main bot file with commands
├── config.py            # Configuration & settings
├── utils.py             # Utility functions
├── requirements.txt     # Dependencies
├── .env                 # Bot token (keep SECRET!)
└── README.md            # This file
```

## Security Tips

⚠️ **IMPORTANT:**
- Never share your bot token
- Never commit `.env` file to Git
- Use environment variables for sensitive data
- Use `.gitignore` to exclude `.env`:
  ```
  .env
  __pycache__/
  *.pyc
  ```

## Troubleshooting

**Bot won't start:**
- Check if `DISCORD_TOKEN` is set in `.env`
- Verify token is valid and not expired
- Make sure bot has required permissions in server

**Commands not working:**
- Check command prefix (default: `!`)
- Verify bot has message permissions
- Make sure Message Content Intent is enabled

**Bot goes offline:**
- Check internet connection
- Verify token is still valid
- Check Discord API status

## Next Steps

Add more features:
- Moderation commands (kick, ban, mute)
- Music player
- Welcome messages
- Auto-moderation
- Custom roles
- Database integration (SQLite, PostgreSQL)

## Resources

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Discord.py Examples](https://github.com/Rapptz/discord.py/tree/master/examples)
