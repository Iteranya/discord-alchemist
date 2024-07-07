# This is where I define the Data Class for the Alchemy Bot
from dataclasses import *


@dataclass
class User:
    display_name: str
    desc: str = "Standard User"
    materials = ["Fire", "Water", "Wind", "Earth"]
    creature = [] # Owned Creatures
    waifus = []  # Owned Waifus

@dataclass
class Material: # You know, the thing you use to combine stuff???
    name: str
    desc: str

@dataclass
class Creature: # a creature that can be born
    name: str
    desc: str
    appearance: str
    behavior: str
    evolve: str # Waifu it evolved to

@dataclass
class Waifu: # a waifu that can be born from the thing... Or evolve from creature???
    # Stage 1 Generation
    name: str
    desc: str
    # Stage 2 Generation
    face: str
    body: str
    clothing: str
    # Stage 3 Generation
    archetype:list[str]
    personality:str
    quirk:str
    origin: str # Creature it Evolved From


@dataclass
class Archetype: # an archetype that the waifu can have (Not Auto Generated-ish)
    name: str
    desc: str


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


