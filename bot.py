import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()

async def send_message(message, user_message, is_privete):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_privete else await message.channel.send(response)

    except Exception as e:
        print(e)

def run_discord_bot():
    # print("hello world")
    TOKEN = os.getenv('DISCORD_TOKEN')
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print("Hello world")
        print(f"{client.user} is running...")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        # is_privete = False
        # if message.channel.type == discord.ChannelType.private:
        #     is_privete = True

        # await send_message(message, message.content, is_privete)
        username = str(message.author.name)
        user_message = str(message.content)
        channel = str(message.channel.name)

        print(f"\n{username} said: `{user_message}` : {channel}")

        if user_message[0] == ">":
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)


    client.run(TOKEN)