from models import *


async def materials_from_description_prompt(item1:Material,item2:Material):
    request = GenerationRequest()
    grammar = "root ::= \"Name: [\" words+ \"]\\nDescription: [\" words+ \"]\\n###\"\n\nwords ::= ([^\u03b3\\n\\]\\[])\n"
    prompt = f"Note: [{item1.name}: {item1.desc}]\n\nBelow is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nMaterial Combiner will combine the 2 items given by User given their description.\n\nMaterial Combiner can combine items into other item or substance that already exist in the world.\n\nMaterial Combiner uses [ ] for formatting.\n### Instruction:\nUser: [Water] + [Fire]\n\n### Response:\nMaterial Combiner: Name: [Steam]\nDescription: [A hot, gaseous form of water. It's a misty, ethereal substance that rises in swirling patterns. Steam can be used for various purposes, from powering engines to cooking food. It's less visible than smoke but can be felt as warm, moist air.]\n\n### Instruction:\nUser: [Earth] + [Fire]\n\n### Response:\nMaterial Combiner: Name: [Lava]\nDescription: [Lava is molten rock expelled from the Earth's surface during volcanic eruptions. It's an intensely hot, viscous fluid formed when Earth's rocky material is heated to extreme temperatures by geological processes.]\n\n### Instruction:\nUser: [Water] + [Fire]\n\n### Response:\nMaterial Combiner: Name: [Steam]\nDescription: [Steam is the vapor form of water, created by the application of heat. It's a colorless, odorless gas composed of water molecules. Steam is used in various applications like power generation, cooking, and even in medical settings. When cooled, it condenses back into liquid water. Steam can be hot and humid, often felt as a misty, warm air.]\n\n### Instruction:\nUser: [Earth] + [Water]\n\n### Response:\nMaterial Combiner: Name: [Mud]\nDescription: [Mud is a mixture of water and soil. It's a soft, damp earth material that can range in consistency from a thick, gooey paste to a loose, crumbly mixture. Mud often forms in wet areas or when soil gets saturated with rainwater. It's commonly used for art projects, building structures, and even as a natural remedy for skin issues.]\n\n### Instruction:\nUser: [Earth] + [Fire]\n\n### Response:\nMaterial Combiner: Name: [Magma]\nDescription: [Magma is a mixture of molten rock, minerals, and gases from the Earth's interior. It's a hot, semi-liquid to liquid state of the Earth's mantle and crust. Magma can rise through the crust, solidifying as igneous rock, or it can erupt as lava during a volcanic eruption. The temperature of magma ranges from about 700\u00b0C to 1,300\u00b0C]\n\n### Instruction:\nUser: [Water] + [Wind]\n\n### Response:\nMaterial Combiner: Name: [Spray]\nDescription: [Spray refers to a fine mist or droplets of a liquid, typically propelled into the air by a force like wind or a device. In the context of water and wind, spray can describe the ocean's foamy surface after a strong gust, or the fine droplets of water blown off the surface of a pond. Spray can also be created artificially, such as by a sprinkler or a high-pressure hose. The droplets in a spray can be small enough to evaporate quickly, leaving no residue behind.]\n\n### Instruction:\nUser: [Earth] + [Wind]\n\n### Response:\nMaterial Combiner: Name: [Dust]\nDescription: [Dust is a fine powder or particles of earth material, often created by the weathering and erosion of rocks or soil. When wind picks up and blows across land, it can lift up and carry these particles, dispersing them into the air. Dust can range in composition, from pure mineral particles to a mixture of soil, clay, and other organic materials.]\n\n### Instruction:\nUser: [Fire] + [Fire]\n\n### Response:\nMaterial Combiner: Name: [Flame]\nDescription: [Flame is the visible, fiery part of a fire. It's a sustained chemical reaction where fuel, typically a combustible material, reacts with oxygen to produce heat, light, and various combustion products. Flames can range from small, flickering sparks to towering infernos, varying in color from blue to orange to red depending on the temperature and chemical composition of the fire.]\n\n### Instruction:\nUser: [{item1.name}]  + [{item2.name}]\n\n### Response(length=short): \nMaterial Combiner:"
    request.prompt = prompt
    request.stop_sequence = ["###"]
    request.grammar = grammar
    request.grammar_string = grammar
    request.max_length = 150
    request.max_tokens = 150

    return request

async def creature_from_material_prompt(item: Material):
    request = GenerationRequest()
    grammar = "root ::= \"Name: [\" words+ \"]\\nDescription: [\" words+ \"]\\n###\"\n\nwords ::= ([^\u03b3\\n\\]\\[])\n"
    prompt = f""
    request.prompt = prompt
    request.stop_sequence = ["###"]
    request.grammar = grammar
    request.grammar_string = grammar
    request.max_length = 150
    request.max_tokens = 150

    return request