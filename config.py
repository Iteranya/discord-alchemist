import asyncio
import json
from typing import *
import data_manager
import aiofiles
import discord
import requests
from models import Material

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

async def initialize():
    data_manager.create_material(Material("Fire","Fierce and unbridled, Fire is the element of transformation, passion, and raw energy. Each flame tells a story of creation and annihilation, a dance of light that consumes and renews."))
    data_manager.create_material(Material("Water","Water is the element of memory, adaptation, and hidden depths. Mercurial and wise, it speaks in the language of rivers and oceans, carrying the whispers of ancient civilizations in its currents. Unpredictable as the tides, water magic reflect the dual nature of life itself—nurturing yet potentially overwhelming."))
    data_manager.create_material(Material("Earth","Solid and unyielding, Earth is the element of stability, protection, and ancient wisdom. They stand immovable as mountain ranges, their magic a testament to endurance and protection. Earth remains—a steady anchor in the tempest of magical forces."))
    data_manager.create_material(Material("Wind","Ethereal and untouchable, Wind is the element of freedom, intellect, and constant motion. Invisible yet everywhere, wind magic whispers secrets of distant lands and carries the breath of change. They dance between physical and magical realms, as swift as thought and as unpredictable as a hurricane. Where other elements seek to control, wind simply moves—unrestricted, unbound, eternal."))