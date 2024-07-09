import unittest
from tinydb import TinyDB
from dataclasses import asdict
from data_manager import (
    User, Material, Creature, Waifu, Archetype, Recipe,
    create_user, get_user, update_user,
    create_material, get_material,
    create_creature, get_creature,
    create_waifu, get_waifu, update_waifu,
    create_archetype, get_archetype, create_recipe, get_all_recipe, check_recipe,
    get_all_users, get_all_materials, get_all_creatures, get_all_waifus, get_all_archetypes
)


class TestDataManager(unittest.TestCase):
    def setUp(self):
        print("Test Start")

    def tearDown(self):
        # Clean up the test database after each test
        print("Test Done")


if __name__ == '__main__':
    unittest.main()