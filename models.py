# This is where I define the Data Class for the Alchemy Bot
from dataclasses import *
from uuid import UUID, uuid4


@dataclass
class Player:
    name: str|None =None
    desc: str|None =None
    materials:list|None =None
    creature:list|None =None # Owned Creatures NAME
    waifus:list|None =None  # Owned Waifus UUID

@dataclass
class Recipe: # To keep track of existing Recipe
    item1:str|None =None
    item2:str|None =None
    result:str|None =None

@dataclass
class Material: # You know, the thing you use to combine stuff???
    name: str|None =None
    desc: str|None =None
    evolve: str | None = None  # The Creature it will evolve to, None by default

@dataclass
class Creature: # a creature that can be born
    name: str|None =None
    desc: str|None =None
    appearance: str|None =None
    behavior: str|None =None
    evolve: str | None = None # The waifu it will evolve to

# Due to staged Generation, I will try to Initialize everything with None
# TODO: Make an extra check at Data Manager to make sure that all field is not none
@dataclass
class Waifu: # a waifu that can be born from the thing... Or evolve from creature???
    # Stage 1 Generation (The Default Stuff)
    name: str|None=None
    desc: str|None=None
    appearance: str|None=None
    # Stage 2 Generation (The Randomly Generated Stuff, separated because might use tags)
    face: str|None=None
    body: str|None=None
    clothing: str|None=None
    ero:str|None=None # Please let no one notice this... I just can't help it.

@dataclass
class OwnedWaifu:
    id: str = ""
    name: str|None =None
    nickname: str = ""
    desc: str | None = None
    appearance: str | None = None
    # Stage 2 Generation (The Randomly Generated Stuff, separated because might use tags)
    face: str | None = None
    body: str | None = None
    clothing: str | None = None
    ero: str | None = None
    # Stage 3 Generation (Even More Randomly Generated Stuff, separated because archetype)
    archetype:list[str]|None=None
    personality:str|None=None
    quirk:str|None=None
    fetish:str|None=None # I have a chance to turn this from my first game to my first eroge. Of course I'm doing it.
    # Stage 4 Generation (Planned Feature)
    avatar_picture: str|None = None
    full_picture:str|None = None
    # Misc Stuff
    gifts:list[str]|None=None # Stuff you've given to your waifu
    affection: int=0 # How much your waifu loves you
    lewd: int=0 # How lewd your waifu is (Again, this is an eroge, I don't care)

    # Also, I can slap this to RenPy if I want
    # That could be pretty interesting, Steam Worthy I say!

@dataclass
class Archetype: # an archetype that the waifu can have (Not Auto Generated-ish)
    name: str|None =None
    desc: str|None =None


# These are Unused for Now, Will Implement Later
@dataclass
class OwnedCreature:
    name:str|None =None
    nickname:str|None =None
    description:str|None =None

# I just found the perfect use for this...
@dataclass
class Base:
    name: str|None=None
    desc: str|None=None
    facilities: list[str]|None=None # "Upgrades" for the alchemy and transmutation table
    pens: list[str]|None=None # Where you put your creatures to interact
    dorms: list[str]|None=None # Where you put your waifu (you can put a few creatures there too as a pet)

@dataclass
class Pen:
    name:str|None=None
    desc:str|None=None
    furnitures: list[str]|None=None
    creatures: list[str]|None=None
    history: list[str]|None=None # Okay, imma keep it real with you chief, I don't think this part is possible

@dataclass
class Dorm:
    name:str|None=None
    desc:str|None=None
    furnitures: list[str]|None=None
    waifus: list[str]|None=None
    creature: list[str]|None=None # These are pets








# Some Util Dataclass for API use

@dataclass
class GenerationRequest: # This is the default Generation Request for LLM API
    prompt: str = ""
    stop_sequence: list = field(default_factory=list)
    add_bos_token: bool = True
    ban_eos_token: bool = True
    do_sample: bool = False
    max_length: int = 1024
    max_tokens: int = 1024
    max_context_length: int = 8192
    genamt: int = 1095
    temp: float = 1.20
    top_k: int = 0
    top_p: float = 0.75
    top_a: int = 0
    typical: int = 1
    tfs: float = 1.0
    rep_pen: int = 1
    rep_pen_range: int = 0
    rep_pen_slope: float = 0.9
    use_default_badwordsids: bool = True
    early_stopping: bool = True
    sampler_order = [6, 0, 1, 3, 4, 2, 5]
    grammar: str = ""
    grammar_string: str = ""

@dataclass
class Result:
    text: str = ""
    finish_reason: str = ""


@dataclass
class Response:
    results: list[Result] = field(default_factory=list)