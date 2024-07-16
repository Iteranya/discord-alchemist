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
    new_user = Player(
        name=name,
        desc=desc,
    )
    new_user.materials = ["Fire","Water","Earth","Wind"]
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
        user.materials = list(set(user.materials))
        data_manager.update_user(user)
        return f"Fusion {mat1} + {mat2} = {new_mat.name}: {new_mat.desc}"
    else:
        return f"You have already created {new_mat.name}"


async def transmutate_material(username: str, mat: str) -> str:
    user = data_manager.get_user(username)
    if mat not in user.materials:
        return f"You have not discovered {mat}"
    else:
        creature = await llm_function.generate_creature_from_material(mat)
        data_manager.create_creature(creature)
        if user.creature:
            user.creature.append(creature.name)
        else:
            user.creature = [creature.name]
        user.creature = list(set(user.creature))

        data_manager.update_user(user)
        creature_detail = formatter.format_creature_detail(creature)
        return f"Transmutation Result: {creature_detail}"


async def evolve_creature(username, creature_name) -> str:
    user = data_manager.get_user(username)
    if creature_name not in user.creature:
        return f"You have not discovered {creature_name}"
    else:
        waifu = await llm_function.generate_waifu(creature_name)
        data_manager.create_waifu(waifu)
        owned_waifu = await llm_function.generate_owned_waifu(waifu.name)
        data_manager.create_owned_waifu(owned_waifu)
        if user.waifus:
            user.waifus.append(owned_waifu.id)
        else:
            user.waifus =  [str(owned_waifu.id)]
        data_manager.update_user(user)
        waifu_detail = formatter.format_owned_waifu_detail(owned_waifu)
        return f"Your {creature_name} evolution result: {waifu_detail}:"


def check_material(username)->str:
    user = data_manager.get_user(username)
    if user:
        materials_list = data_manager.get_material(user.materials)
        print(f"check_material {materials_list}")
        return formatter.format_materials(materials_list)
    else:
        return "You don't have an account, please register"

def check_creatures(username)->str:
    user = data_manager.get_user(username)
    if user:
        if user.creature:
            creature_list = data_manager.get_creature(user.creature)
            return formatter.format_creatures(creature_list)
        else:
            return "You don't have any creature"
    else:
        return "You don't have an account, please register"

def check_owned_waifu(username)->str:
    user = data_manager.get_user(username)
    if user:
        if user.waifus:
            owned_waifu_list = data_manager.get_owned_waifu(user.waifus)
            return formatter.format_owned_waifu(owned_waifu_list)
        else:
            return "You are waifuless"
    else:
        return "You don't have an account, please register"

def check_waifu_detail(waifu_uuid:str)->str:
    owned_waifu = data_manager.get_owned_waifu(waifu_uuid)
    if owned_waifu:
        return formatter.format_owned_waifu_detail(owned_waifu)
    else:
        return "Wrong UUID~"

def check_creature_detail(creature_name)->str:
    creature = data_manager.get_creature(creature_name)
    if creature:
        return formatter.format_creature_detail(creature)
    else:
        return "Wrong Creature Name~ (It's case sensitive, sorry)"


def show_help():
    return """
    /rpg register -> Register Your Player Profile, uses your current server display name. Requires a short description about yourself.
    
    /rpg elements -> Check the elements you have, you can only do fusion/transmutation using elements you've discovered
    
    /rpg creatures -> Check the list of creatures you have, you can only do evolution on creatures you own
    
    /rpg creature_detail -> Check the detail of the creature you have, requires the name of the creature
    
    /rpg waifus -> Check the list of waifus you have and the UUID.
    
    /rpg waifu_detail -> Check the detail of the waifu you have, requires the waifu UUID.
    
    """