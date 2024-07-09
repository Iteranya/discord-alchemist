import random
from typing import Optional

import alchemy_prompts
import data_manager
import llm_api
import response_parser
from models import *


# These are the LLM Function

async def generate_material_from_two_items(mat1_name : str,  mat2_name: str)->None|Material:
    # Get the material desc etc
    mat1 = data_manager.get_material(mat1_name)
    mat2 = data_manager.get_material(mat2_name)

    # Find if this combination is already dicovered
    existing_material:str = data_manager.check_recipe(mat1.name,mat2.name)

    if existing_material:
        # If existing material exists, just grab em
        return data_manager.get_material(existing_material)
    else:
        # If don't exist yet, generate new one
        prompt = alchemy_prompts.fusion_material_prompt(mat1,mat2)
        result = await llm_api.send_to_llm(prompt)
        new_material = response_parser.extract_material(result)
        new_recipe = Recipe(
            mat1.name,mat2.name,new_material.name
        )
        data_manager.create_material(new_material)
        data_manager.create_recipe(new_recipe)
        return new_material

async def generate_creature_from_material(mat_name:str):
    mat = data_manager.get_material(mat_name)
    if mat.evolve:
        return data_manager.get_creature(mat.evolve)
    else:
        # If don't exist make new creature
        prompt = alchemy_prompts.creature_from_material_prompt(mat)
        result = await llm_api.send_to_llm(prompt)
        new_creature = response_parser.extract_generated_creature(result)
        data_manager.create_creature(new_creature)
        mat.evolve = new_creature.name
        data_manager.update_material(mat)
        return new_creature

async def generate_waifu(creature_name:str):
    creature = data_manager.get_creature(creature_name)
    waifu:Waifu
    if creature.evolve:
        return data_manager.get_waifu(creature.evolve)
    else:
        # Two Stage Waifu Species Creation
        prompt = alchemy_prompts.waifu_stage_one_prompt(creature)
        result = await llm_api.send_to_llm(prompt)
        new_waifu:Waifu = response_parser.extract_waifu_gen1(result)
        prompt = alchemy_prompts.waifu_stage_two_prompt(new_waifu)
        result = await llm_api.send_to_llm(prompt)
        new_waifu = response_parser.extract_waifu_gen2(result,new_waifu)
        # Like putting a ducktape over a gaping hole...
        # Wait, wait, I have a better idea
        while data_manager.get_waifu(new_waifu.name):
            new_waifu.name = new_waifu.name + "(*)"

        # Update creature so that it contains waifu evolution
        creature.name = new_waifu.name
        # Insert new waifu and updated creature into database
        data_manager.create_waifu(new_waifu)
        data_manager.update_creature(creature)
        return new_waifu


async def generate_owned_waifu(waifu_name:str):
    # Stage 3 Waifu Creation, the Personality and such part.
    waifu = data_manager.get_waifu(waifu_name)
    archetypes:list[Archetype] = data_manager.get_all_archetypes()
    arch: list[Archetype] = random.sample(archetypes, 2)
    prompt = alchemy_prompts.waifu_stage_three_prompt(waifu=waifu,arch1=arch[0],arch2=arch[1])
    result = await llm_api.send_to_llm(prompt)
    owned_waifu:OwnedWaifu = response_parser.extract_waifu_gen3(result,waifu,arch[0],arch[1])
    return owned_waifu
