from models import *


def format_materials(materials: list[Material]) -> str:
    output = "**Material List:**\n\n"

    for material in materials:
        output += f"**{material.name}**\n"
        output += f"{material.desc}\n"

        if material.evolve:
            output += f"Evolves into: {material.evolve}\n"
        else:
            output += "This material has never been used for Transmutation.\n"

        output += "\n"

    return output.strip()


def format_creatures(creatures: list[Creature]) -> str:
    output = "**Creature List:**\n\n"

    for creature in creatures:
        output += f"**{creature.name}**\n"
        output += f"Description: {creature.desc}\n"
        output += f"Appearance: {creature.appearance}\n"
        output += f"Behavior: {creature.behavior}\n"

        if creature.evolve:
            output += f"Evolves into: {creature.evolve}\n"
        else:
            output += "This creature does not have a known evolution.\n"

        output += "\n"

    return output.strip()


def format_owned_waifus(waifus: list[OwnedWaifu]) -> str:
    output = "**Waifu List:**\n\n"

    for waifu in waifus:
        output += f"**{waifu.name}**\n"
        output += f"Description: {waifu.desc}\n"
        output += f"Appearance: {waifu.appearance}\n"
        output += f"Behavior: {waifu.personality}\n"

        output += "\n"

    return output.strip()


def format_owned_waifu_detail(waifu:OwnedWaifu,nsfw:bool = False)->str:
    output = f"**{waifu.nickname}**\n\n"
    output += f"Description: {waifu.desc}\n"
    output += f"Appearance: {waifu.appearance}\n"
    output += f"Personality: {waifu.personality}\n"
    output += f"Face: {waifu.face}\n"
    output += f"Body: {waifu.body}\n"
    output += f"Clothing: {waifu.clothing}\n"
    if nsfw:
        output += f"Erogenous: {waifu.ero}\n"
        output += f"Fetish: {waifu.fetish}\n"

    return output.strip()