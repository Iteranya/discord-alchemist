import re
from typing import Optional

from models import *


# REGEX LAIR!!!!
# ...
# As in like, yknow, to parse LLM Strings and such into Data Class
# Yeah, I think that's it...
# Imma go and make a universal function that captures all the [] first
# By that I mean, I'm gonna ask AI to make one for me.

#

def extract_bracketed_content(text):
    pattern = r'\[(.*?)\]'
    matches = re.findall(pattern, text, re.DOTALL)
    return [match.strip() for match in matches]

# Aight, done, now I just have to format everything to use Bracket for anything relevant
# Oh The Beauty of GBNF!!!

# Okay, first, Creature Response

example_creature = """
    Name: [Train Abomination]
    Description: [Literally A Gigantic Spider Train Abomination]
    Appearance: [Big, Much Legs, Scary]
    Behavior: [Eats Humans]
    Evolve: [Train Arachne]
"""

def extract_generated_creature(text)->Optional[Creature]:
    extraction =extract_bracketed_content(text)
    try:
        name = extraction[0]
        description = extraction[1]
        appearance = extraction[2]
        behavior = extraction[3]
        evolve = extraction[4]
        creature = Creature(
            name=name,
            desc=description,
            appearance=appearance,
            behavior=behavior,
            evolve=evolve
        )
        return creature
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

example_generated_material= """
    Name: [Cloud]
    Description: [Soft and fluffy and cloudy~]
"""

def extract_material(text)->Optional[Material]:
    ex = extract_bracketed_content(text)
    try:
        name = ex[0]
        desc = ex[1]
        mat = Material(
            name = name,
            desc = desc
        )
        return mat
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

# Hmmm... How do I do this?
# I don't want to separate each of these...
# Should  I just do a 'join' and then Regex it?
# No... I need this... Hmm...
# Init Everything with None??? That sounds Dangerous, but might work
example_waifu_gen1 = """
    Name:   [Train Arachne]
    Desc:   [A shockingly beautiful woman wearing a train conductor uniform with the lower body
            of a giant spider.] 
"""
def extract_waifu_gen1(text)->Optional[Waifu]:
    ex = extract_bracketed_content(text)
    try:
        name = ex[0]
        desc = ex[1]
        waifu = Waifu(
            name = name,
            desc = desc
        )
        return waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

example_waifu_gen2 = """
    Face:   [Black Eyes, Blue Hair, Short Hair, Cute]
    Body:   [Tall, Voluptous, Spider Leg, Human Arms and Hands] 
    Clothing: [uniform, formal, train conductor, cleavage, hat]
"""
def extract_waifu_gen2(text,waifu)->Optional[Waifu]:
    ex = extract_bracketed_content(text)
    try:
        waifu.face = ex[0]
        waifu.body = ex[1]
        waifu.clothing = ex[2]
        return waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

example_waifu_gen3 = """
    Archetype:   [Gentle Giant],[Dandere],[Office Woman]
    Personality:   [Cute and adorable and nice and such] 
    Quirk: [Likes whistle, zoomies on tracks, snacks on coal]
"""

def extract_waifu_gen3(text,waifu)->Optional[Waifu]:
    ex = extract_bracketed_content(text)
    try:
        waifu.archetype = ex[0]+ex[1]+ex[2]
        waifu.personality = ex[3]
        waifu.quirk = ex[4]
        return waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None
