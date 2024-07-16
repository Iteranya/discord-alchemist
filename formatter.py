from models import *


def format_materials(materials: list[Material]) -> str:
    output = "**Material List:**\n\n"

    for material in materials:
        output += f"{material.name}, "

    return output.strip()


def format_creature_detail(creature: Creature) -> str:
    output = "**Creature Detail:**\n\n"
    if creature:
            output += f"**{creature.name}**\n"
            output += f"Description: {creature.desc}\n"
            output += f"Appearance: {creature.appearance}\n"
            output += f"Behavior: {creature.behavior}\n"

            if creature.evolve:
                output += f"Evolves into: {creature.evolve}\n"
            else:
                output += "This creature does not have a known evolution.\n"

            output += "\n"
    else:
        output = "You don't have a creature~"

    return output.strip()

def format_creatures(creatures: list[Creature]) -> str:
    output = "**Creature List:**\n\n"
    if creatures:
        for creature in creatures:
            output += f"{creature.name}"
            output += ", "
        output += "\n Use /creature_detail <name> to see the full description"
    else:
        output = "You don't have a creature~"

    return output.strip()

def format_owned_waifu(waifus: list[OwnedWaifu]) -> str:
    output = "**Waifu List:**\n\n"

    if waifus:

        for waifu in waifus:
            output += f"**{waifu.name}**: {waifu.id}\n"
            output += "\n"
        output += "Use /waifu_detail <id> for detail"
    else:
        output = "You are waifuless"

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
        output += f"Erogenous Zones: {waifu.ero}\n"
        output += f"Fetish: {waifu.fetish}\n"

    return output.strip()