# Well.. that's one way to name a file...
import data_manager
import formatter
import llm_function
from models import *


# Anyway, here we have all the function that directly interacts with User
# See, back then, I'd start with this and then the database
# Hence why it's a mess
# Now it's beautiful~

def create_user(name: str, desc: str):  # Every user will start here, this is important
    new_user = User(
        name=name,
        desc=desc
    )
    data_manager.create_user(new_user)
    # Well... that was easy...


async def combine_element(username: str, mat1: str, mat2: str) -> str:
    # I forgot something
    # If you forgot about it, then it's probably not  important
    # You're right
    # TODO: *Case Sensitivity*
    user = data_manager.get_user(username)
    if (mat1 not in user.materials):
        return f"You have not discovered {mat1}"
    if (mat2 not in user.materials):
        return f"You have not discovered {mat2}"

    new_mat = await llm_function.generate_material_from_two_items(mat1, mat2)
    if (new_mat not in user.materials):
        data_manager.create_material(new_mat)
        user.materials.append(new_mat.name)
        return f"Congrats, You've Created {new_mat.name}"
    else:
        return f"You have already created {new_mat.name}"


async def transmutate_material(username: str, mat: str) -> str:
    user = data_manager.get_user(username)
    if mat not in user.materials:
        return f"You have not discovered {mat}"
    else:
        creature = await llm_function.generate_creature_from_material(mat)
        data_manager.create_creature(creature)
        while creature.name in user.creature:
            creature.name = creature.name + "*"

        user.creature.append(creature.name)
        data_manager.update_user(user)
        return f"You have created {creature.name}"


async def evolve_creature(username, creature_name) -> str:
    user = data_manager.get_user(username)
    if creature_name not in user.creature:
        return f"You have not discovered {creature_name}"
    else:
        waifu = await llm_function.generate_waifu(creature_name)
        data_manager.create_waifu(waifu)
        owned_waifu = await llm_function.generate_owned_waifu(waifu.name)
        data_manager.create_owned_waifu(owned_waifu)
        user.waifus.append(owned_waifu.id)
        data_manager.update_user(user)

        return f"Your {creature_name} has evolved into {owned_waifu.name}"


async def check_material(username)->str:
    user = data_manager.get_user(username)
    materials_list = data_manager.get_material(user.materials)
    return formatter.format_materials(materials_list)

async def check_creatures(username)->str:
    user = data_manager.get_user(username)
    creature_list = data_manager.get_creature(user.creature)
    return formatter.format_creatures(creature_list)


async def check_owned_waifu(username)->str:
    user = data_manager.get_user(username)
    owned_waifu_list = data_manager.get_owned_waifu(user.waifus)
    return formatter.format_owned_waifus(owned_waifu_list)

async def check_waifu_detail(waifu_uuid)->str:
    owned_waifu = data_manager.get_owned_waifu(waifu_uuid)
    return formatter.format_owned_waifu_detail(owned_waifu)


def show_help():
    return "This is where I put a simple guide to use the bot"