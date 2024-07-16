# This is where we do Databasing and Jsoning
# I will use TinyDB for this
from typing import *
from tinydb import *
from models import *
from response_parser import extract_bracketed_content

## And ask AI's help to write it down for me
db = TinyDB('main_database.json')

# Tables
users_table = db.table('users')
materials_table = db.table('materials')
creatures_table = db.table('creatures')
waifus_table = db.table('waifus')
archetypes_table = db.table('archetypes')
recipe_table = db.table('recipes')
owned_waifus_table = db.table('owned_waifus')


def extract_and_store_archetypes(text: str):
    # Extract all bracketed content
    contents = extract_bracketed_content(text)

    # Process pairs of contents (name and description)
    for i in range(0, len(contents), 2):
        if i + 1 < len(contents):
            name = contents[i]
            desc = contents[i + 1]

            # Create an Archetype instance
            archetype = Archetype(name=name, desc=desc)

            # Insert the archetype into the TinyDB table
            create_archetype(archetype)


# User functions
def create_user(user: Player) -> int:  # Used when User uses the bot for the first time
    return users_table.insert(asdict(user))


def get_user(display_name: str) -> Optional[Player]:  # Used whenever User uses the bot
    User_query = Query()
    result = users_table.get(User_query.name == display_name)
    return Player(**result) if result else None


def update_user(user: Player) -> List[int]:  # Used whenever User finishes an action and something change
    User_query = Query()
    return users_table.update(asdict(user), User_query.name == user.name)


# Material functions
def create_material(material: Material) -> int:  # Used to add material into the list of discovered materials
    return materials_table.insert(asdict(material))


def get_material(name: Union[str, List[str]]) -> Union[Optional[Material], List[Optional[Material]]]:
    Material_query = Query()

    print(f"get_material {name}")

    if isinstance(name, str):
        result = materials_table.get(Material_query.name == name)
        return Material(**result) if result else None

    elif isinstance(name, list):
        results = materials_table.search(Material_query.name.one_of(name))
        return [Material(**result) if result else None for result in results]

    else:
        raise ValueError("Input must be a string or a list of strings")


def update_material(material: Material) -> List[int]:
    Material_query = Query()
    return materials_table.update(asdict(material), Material_query.name == material.name)


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
    Creature_query = Query()
    existing_creature = creatures_table.get(Creature_query.name == creature.name)

    if existing_creature is None:
        return creatures_table.insert(asdict(creature))
    else:
        return -1  # Or any other value to indicate the creature wasn't inserted


def get_creature(name: Union[str, List[str]]) -> Union[Optional[Creature], List[Optional[Creature]]]:
    Creature_query = Query()

    if isinstance(name, str):
        result = creatures_table.get(Creature_query.name == name)
        return Creature(**result) if result else None

    elif isinstance(name, list):
        results = creatures_table.search(Creature_query.name.one_of(name))
        return [Creature(**result) if result else None for result in results]

    else:
        raise ValueError("Input must be a string or a list of strings")


def update_creature(creature: Creature) -> List[int]:
    Creature_query = Query()
    return creatures_table.update(asdict(creature), Creature_query.name == creature.name)


# Waifu functions
def create_waifu(waifu: Waifu) -> int:
    Waifu_query = Query()
    existing_waifu = waifus_table.get(Waifu_query.name == waifu.name)

    if existing_waifu is None:
        return waifus_table.insert(asdict(waifu))
    else:
        return -1


def get_waifu(name: Union[str, List[str]]) -> Union[Optional[Waifu], List[Optional[Waifu]]]:
    Waifu_query = Query()

    if isinstance(name, str):
        result = waifus_table.get(Waifu_query.name == name)
        return Waifu(**result) if result else None

    elif isinstance(name, list):
        results = waifus_table.search(Waifu_query.name.one_of(name))
        return [Waifu(**result) if result else None for result in results]

    else:
        raise ValueError("Input must be a string or a list of strings")


def update_waifu(waifu: Waifu) -> List[int]:
    Waifu_query = Query()
    return waifus_table.update(asdict(waifu), Waifu_query.name == waifu.name)


# Owned Waifu Function

def create_owned_waifu(waifu: OwnedWaifu) -> int:
    return owned_waifus_table.insert(asdict(waifu))


def get_owned_waifu(owned_waifu_id: Union[str, List[str]]) -> Union[Optional[OwnedWaifu], List[Optional[OwnedWaifu]]]:
    Waifu_query = Query()

    if isinstance(owned_waifu_id, str):
        result = owned_waifus_table.get(Waifu_query.id == owned_waifu_id)
        return OwnedWaifu(**result) if result else None

    elif isinstance(owned_waifu_id, list):
        results = owned_waifus_table.search(Waifu_query.id.one_of(owned_waifu_id))
        return [OwnedWaifu(**result) if result else None for result in results]

    else:
        raise ValueError("Input must be a string or a list of strings")


def update_owned_waifu(waifu: OwnedWaifu) -> List[int]:
    Waifu_query = Query()
    return owned_waifus_table.update(asdict(waifu), Waifu_query.name == waifu.name)


# Archetype functions
def create_archetype(archetype: Archetype) -> int:
    return archetypes_table.insert(asdict(archetype))


def get_archetype(name: str) -> Optional[Archetype]:
    Archetype_query = Query()
    result = archetypes_table.get(Archetype_query.name == name)
    return Archetype(**result) if result else None


# Utility functions
def get_all_users() -> List[Player]:
    return [Player(**user) for user in users_table.all()]


def get_all_materials() -> List[Material]:
    return [Material(**material) for material in materials_table.all()]


def get_all_creatures() -> List[Creature]:
    return [Creature(**creature) for creature in creatures_table.all()]


def get_all_waifus() -> List[Waifu]:
    return [Waifu(**waifu) for waifu in waifus_table.all()]


def get_all_archetypes() -> List[Archetype]:
    return [Archetype(**archetype) for archetype in archetypes_table.all()]


def get_all_recipe() -> List[Recipe]:
    return [Recipe(**recipe) for recipe in recipe_table]


# Trim Database
def trim():
    all_record = users_table.all()
    unique_names = set()
    duplicate_ids = []

    for record in all_record:
        name = record['name']
        if name in unique_names:
            duplicate_ids.append(record.doc_id)
        else:
            unique_names.add(name)

    for doc_id in duplicate_ids:
        users_table.remove(doc_ids=[doc_id])

    print(f"Trimmed materials table. Removed {len(duplicate_ids)} duplicates.")
