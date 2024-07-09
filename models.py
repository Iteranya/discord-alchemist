# This is where I define the Data Class for the Alchemy Bot
from dataclasses import *
from uuid import UUID, uuid4


@dataclass
class User:
    display_name: str
    desc: str = "Standard User"
    materials = ["Fire", "Water", "Wind", "Earth"]
    creature = [] # Owned Creatures ID
    waifus = []  # Owned Waifus ID

@dataclass
class Recipe: # To keep track of existing Recipe
    item1:str
    item2:str
    result:str

@dataclass
class Material: # You know, the thing you use to combine stuff???
    name: str
    desc: str
    evolve: str | None = None  # The Creature it will evolve to, None by default

@dataclass
class Creature: # a creature that can be born
    name: str
    desc: str
    appearance: str
    behavior: str
    evolve: str | None # The waifu it will evolve to

# Due to staged Generation, I will try to Initialize everything with None
# TODO: Make an extra check at Data Manager to make sure that all field is not none
# Except for picture
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
class Archetype: # an archetype that the waifu can have (Not Auto Generated-ish)
    name: str
    desc: str


# These are Unused for Now, Will Implement Later
@dataclass
class OwnedCreature:
    waifu_name: str
    nickname: str = ""
    level: int = 1
    experience: int = 0


@dataclass
class OwnedWaifu:
    creature_name: str
    nickname: str = ""
    level: int = 1
    experience: int = 0
    # Stage 3 Generation (Even More Randomly Generated Stuff, separated because archetype)
    archetype:list[str]|None=None
    personality:str|None=None
    quirk:str|None=None
    fetish:str|None=None # I have a chance to turn this from my first game to my first eroge. Of course I'm doing it.
    # Stage 4 Generation (Planned Feature)
    avatar_picture: str|None = None
    full_picture:str|None = None



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