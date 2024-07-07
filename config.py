import json
from typing import *

import aiofiles
import requests


global text_api

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
    text_api = await set_api("text-default.json")
    await api_status_check(text_api["address"] + text_api["model"],headers=text_api["headers"])

