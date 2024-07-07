# This is where we do Databasing and Jsoning
# I will use TinyDB for this
from typing import *
from tinydb import *
from models import *


## And ask AI's help to write it down for me
db = TinyDB('main_database.json')

# Tables
users_table = db.table('users')
materials_table = db.table('materials')
creatures_table = db.table('creatures')
waifus_table = db.table('waifus')
archetypes_table = db.table('archetypes')
recipe_table = db.table('recipes')

# User functions
def create_user(user: User) -> int: # Used when User uses the bot for the first time
    return users_table.insert(asdict(user))

def get_user(display_name: str) -> Optional[User]: # Used whenever User uses the bot
    User_query = Query()
    result = users_table.get(User_query.display_name == display_name)
    return User(**result) if result else None

def update_user(user: User) -> List[int]: # Used whenever User finishes an action and something change
    User_query = Query()
    return users_table.update(asdict(user), User_query.display_name == user.display_name)

# Material functions
def create_material(material: Material) -> int: # Used to add material into the list of discovered materials
    return materials_table.insert(asdict(material))

def get_material(name: str) -> Optional[Material]: # Get an already discovered material instead of generating
    Material_query = Query()
    result = materials_table.get(Material_query.name == name)
    return Material(**result) if result else None

def create_recipe(recipe: Recipe):
    return recipe_table.insert(asdict(recipe))

def check_recipe(item1: str, item2: str) -> Optional[str]:
    recipes = get_all_recipe()
    for recipe in recipes:
        # Check if the recipe matches exactly (order doesn't matter)
        if (recipe.item1 == item1 and recipe.item2 == item2) or (recipe.item1 == item2 and recipe.item2 == item1):
            return recipe.result
    return None

# Creature functions
def create_creature(creature: Creature) -> int:
    return creatures_table.insert(asdict(creature))

def get_creature(name: str) -> Optional[Creature]:
    Creature_query = Query()
    result = creatures_table.get(Creature_query.name == name)
    return Creature(**result) if result else None

# Waifu functions
def create_waifu(waifu: Waifu) -> int:
    return waifus_table.insert(asdict(waifu))

def get_waifu(name: str) -> Optional[Waifu]:
    Waifu_query = Query()
    result = waifus_table.get(Waifu_query.name == name)
    return Waifu(**result) if result else None

def update_waifu(waifu: Waifu) -> List[int]:
    Waifu_query = Query()
    return waifus_table.update(asdict(waifu), Waifu_query.name == waifu.name)

# Archetype functions
def create_archetype(archetype: Archetype) -> int:
    return archetypes_table.insert(asdict(archetype))

def get_archetype(name: str) -> Optional[Archetype]:
    Archetype_query = Query()
    result = archetypes_table.get(Archetype_query.name == name)
    return Archetype(**result) if result else None

# Utility functions
def get_all_users() -> List[User]:
    return [User(**user) for user in users_table.all()]

def get_all_materials() -> List[Material]:
    return [Material(**material) for material in materials_table.all()]

def get_all_creatures() -> List[Creature]:
    return [Creature(**creature) for creature in creatures_table.all()]

def get_all_waifus() -> List[Waifu]:
    return [Waifu(**waifu) for waifu in waifus_table.all()]

def get_all_archetypes() -> List[Archetype]:
    return [Archetype(**archetype) for archetype in archetypes_table.all()]

def get_all_recipe()-> List[Recipe]:
    return [Recipe(**recipe) for recipe in recipe_table]