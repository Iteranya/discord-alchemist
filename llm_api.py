import json

from aiohttp import *

import data_manager
from models import *
from data_manager import *
import config



async def send_to_llm(prompt: GenerationRequest) -> str | None:
    # Get the queue item that's next in the list
    timeout = ClientTimeout(total=600)
    connector = TCPConnector(limit_per_host=10)
    async with ClientSession(timeout=timeout, connector=connector) as session:
        try:
            async with session.post(
                    config.text_api["address"] + config.text_api["generation"],
                    headers=config.text_api["headers"],
                    json=prompt.__dict__
            ) as response:
                if response.status == 200:
                    try:
                        json_response = await response.json()
                        print("JSON response get")
                        print(json_response)
                        return read_results_from_json(json_response)
                    except json.decoder.JSONDecodeError as e:
                        print(f"JSON decode error: {e}")
                        return None
                else:
                    # Handle non-200 responses here
                    print(f"HTTP request failed with status: {response.status}")
                    return None
        except Exception as e:
            # Handle any other exceptions
            print(f"An error occurred: {e}")
            return None

def read_results_from_json(json_data) -> str:
    response = Response()
    for result in json_data['results']:
        response.results.append(Result(
            text=result['text'],
            finish_reason=result['finish_reason']
        ))

    return response.results[0].text