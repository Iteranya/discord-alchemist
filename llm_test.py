import asynctest
from tinydb import TinyDB
from dataclasses import asdict

import config
import data_manager
import llm_function
import response_parser
from data_manager import (
    User, Material, Creature, Waifu, Archetype, Recipe,
    create_user, get_user, update_user,
    create_material, get_material,
    create_creature, get_creature,
    create_waifu, get_waifu, update_waifu,
    create_archetype, get_archetype, create_recipe, get_all_recipe, check_recipe,
    get_all_users, get_all_materials, get_all_creatures, get_all_waifus, get_all_archetypes
)


class TestDataManager(asynctest.TestCase):
    async def setUp(self):
        print("Test Start")
        await config.setup()

    def tearDown(self):
        # Clean up the test database after each test
        print("Test Done")

    async def testCreateMaterial(self):

        mat1 = "Fire"
        mat2 = "Earth"
        new_material:Material = await llm_function.generate_material_from_two_items(mat1,mat2)
        result = data_manager.get_material(new_material.name)
        print(new_material.name)
        print(new_material.desc)
        self.assertEqual(result, new_material)

    async def testCreateCreature(self):
        mat = "Wind"
        new_creature:Creature = await llm_function.generate_creature_from_material(mat)
        print(new_creature.name)
        print(new_creature.desc)
        print(new_creature.behavior)
        print(new_creature.appearance)
        data_manager.create_creature(new_creature)
        saved_creature = data_manager.get_creature(new_creature.name)
        self.assertEqual(saved_creature,new_creature)

    async def testCreateWaifu(self):
        creature = "Aerospirit"
        new_waifu:Waifu = await llm_function.generate_waifu(creature)
        print(new_waifu.name)
        print(new_waifu.desc)
        print(new_waifu.appearance)
        print(new_waifu.body)
        print(new_waifu.face)
        print(new_waifu.clothing)
        print(new_waifu.ero)
        data_manager.create_waifu(new_waifu)
        saved_waifu = data_manager.get_waifu(new_waifu.name)
        self.assertEqual(saved_waifu,new_waifu)



if __name__ == '__main__':
    asynctest.main()