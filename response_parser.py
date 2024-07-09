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

def extract_bracketed_content(text:str):
    pattern = r'\[(.*?)\]'
    matches = re.findall(pattern, text, re.DOTALL)
    return [match.strip() for match in matches]

# Aight, done, now I just have to format everything to use Bracket for anything relevant
# Oh The Beauty of GBNF!!!

# Okay, first, Creature Response



def extract_generated_creature(text:str)->Optional[Creature]:
    extraction =extract_bracketed_content(text)
    try:
        name = extraction[0]
        description = extraction[1]
        appearance = extraction[2]
        behavior = extraction[3]
        creature = Creature(
            name=name,
            desc=description,
            appearance=appearance,
            behavior=behavior
        )
        return creature
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None



def extract_material(text:str)->Optional[Material]:
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
def extract_waifu_gen1(text:str)->Optional[Waifu]:
    ex = extract_bracketed_content(text)
    try:
        name = ex[0]
        desc = ex[1]
        appearance = ex[2]
        waifu = Waifu(
            name = name,
            desc = desc,
            appearance=appearance
        )
        return waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

def extract_waifu_gen2(text:str,waifu:Waifu)->Optional[Waifu]:
    ex = extract_bracketed_content(text)
    try:
        waifu.face = ex[0]
        waifu.body = ex[1]
        waifu.clothing = ex[2]
        waifu.ero = ex[3]
        return waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

def extract_waifu_gen3(text:str,waifu:Waifu,arch1:Archetype,arch2:Archetype)->Optional[OwnedWaifu]:
    ex = extract_bracketed_content(text)
    try:
        owned_waifu = OwnedWaifu(
            waifu.name,
            waifu.name + "-chan",
            1,
            0,
            [arch1.name,arch2.name],
            ex[0],
            ex[1],
            ex[2],
            None,
            None
        )
        return owned_waifu
    except(IndexError):
        print("Generation Failed, Try Again~")
        return None

