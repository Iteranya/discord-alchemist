import asyncio
import json
from typing import *

import aiofiles
import discord
import requests

global text_api
rpg_queue = asyncio.Queue()
# FOR DISCORD
intents: discord.Intents = discord.Intents.all()
client: discord.Client = discord.Client(command_prefix='/', intents=intents)

async def set_api(config_file: str) -> dict[str, Any]:
    # Read the configuration file
    async with aiofiles.open(config_file, mode='r') as file:
        contents = await file.read()

    # Parse the JSON content
    api = json.loads(contents)

    # Return the API
    return api

# Check to see if the API is running (pick any API)
async def api_status_check(link: str, headers):

    try:
        response = requests.get(link, headers=headers)
        status = response.ok
    except requests.exceptions.RequestException as e:
        print("Error occurred Language model not currently running.")
        status = False

    return status

async def setup():
    global text_api
    text_api = await set_api("text-default.json")
    status = await api_status_check(text_api["address"] + text_api["model"], headers=text_api["headers"])
    return status