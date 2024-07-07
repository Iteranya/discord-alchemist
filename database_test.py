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
        # Create a test database
        self.db = TinyDB('main_database.json')

        # Clear all tables before each test
        self.db.drop_tables()

    def tearDown(self):
        # Clean up the test database after each test
        self.db.close()

    def test_user_operations(self):
        user = User(display_name="TestUser")
        user_id = create_user(user)
        self.assertIsNotNone(user_id)

        retrieved_user = get_user("TestUser")
        self.assertEqual(retrieved_user.display_name, "TestUser")

        user.desc = "Updated User"
        update_user(user)
        updated_user = get_user("TestUser")
        self.assertEqual(updated_user.desc, "Updated User")

    def test_material_operations(self):
        material = Material(name="TestMaterial", desc="Test Description")
        material_id = create_material(material)
        self.assertIsNotNone(material_id)

        retrieved_material = get_material("TestMaterial")
        self.assertEqual(retrieved_material.desc, "Test Description")

    def test_creature_operations(self):
        creature = Creature(name="TestCreature", desc="Test Description", appearance="Test Appearance",
                            behavior="Test Behavior", evolve="TestEvolution")
        creature_id = create_creature(creature)
        self.assertIsNotNone(creature_id)

        retrieved_creature = get_creature("TestCreature")
        self.assertEqual(retrieved_creature.desc, "Test Description")

    def test_waifu_operations(self):
        waifu = Waifu(name="TestWaifu", desc="Test Description", face="Test Face", body="Test Body",
                              clothing="Test Clothing", archetype=["TestArchetype"], personality="Test Personality",
                              quirk="Test Quirk", origin="TestOrigin")
        waifu_id = create_waifu(waifu)
        self.assertIsNotNone(waifu_id)

        retrieved_waifu = get_waifu("TestWaifu")
        self.assertEqual(retrieved_waifu.desc, "Test Description")

        waifu.personality = "Updated Personality"
        update_waifu(waifu)
        updated_waifu = get_waifu("TestWaifu")
        self.assertEqual(updated_waifu.personality, "Updated Personality")

    def test_archetype_operations(self):
        archetype = Archetype(name="TestArchetype", desc="Test Description")
        archetype_id = create_archetype(archetype)
        self.assertIsNotNone(archetype_id)

        retrieved_archetype = get_archetype("TestArchetype")
        self.assertEqual(retrieved_archetype.desc, "Test Description")

    def test_recipe_check(self):
        item1 = "TestItem1"
        item2 = "TestItem2"
        result = "TestResult"
        recipe_id = create_recipe(Recipe(item1=item1,item2=item2,result=result))
        self.assertIsNotNone(recipe_id)

        create_recipe(Recipe(item1="TestItem3",item2="TestItem2",result="Result2"))

        check = check_recipe(item1,item2)
        self.assertEqual(result,check)

        item1 = "TestItem2"
        item2 = "TestItem1"
        check = check_recipe(item1, item2)
        self.assertEqual(result, check)

        item1 = "TestItem1"
        item2 = "TestItem1"
        check = check_recipe(item1, item2)
        self.assertNotEquals(result,check)

        item1 = "TestItem2"
        item2 = "TestItem2"
        check = check_recipe(item1, item2)
        self.assertNotEquals(result, check)

        item1 = "TestItem1"
        item2 = "TestItem3"
        check = check_recipe(item1, item2)
        self.assertNotEquals(result, check)

        item1 = "TestItem3"
        item2 = "TestItem2"
        check = check_recipe(item1, item2)
        self.assertNotEquals(result, check)

    # def test_owned_creature_operations(self):
    #     user = User(display_name="TestUser")
    #     create_user(user)
    #
    #     creature = Creature(name="TestCreature", desc="Test Description", appearance="Test Appearance",
    #                         behavior="Test Behavior", evolve="TestEvolution")
    #     create_creature(creature)
    #
    #     creature_id = add_creature_to_user(user, creature, nickname="TestNickname")
    #     self.assertIsNotNone(creature_id)
    #
    #     owned_creature = get_owned_creature(creature_id)
    #     self.assertEqual(owned_creature.nickname, "TestNickname")
    #
    #     owned_creature.level = 5
    #     update_owned_creature(owned_creature)
    #     updated_creature = get_owned_creature(creature_id)
    #     self.assertEqual(updated_creature.level, 5)
    #
    #     user_creatures = get_user_creatures(user)
    #     self.assertEqual(len(user_creatures), 1)
    #     self.assertEqual(user_creatures[0].creature_name, "TestCreature")

    def test_get_all_operations(self):
        # Create some test data
        create_user(User(display_name="TestUser1"))
        create_user(User(display_name="TestUser2"))
        create_material(Material(name="TestMaterial1", desc="Test Description 1"))
        create_material(Material(name="TestMaterial2", desc="Test Description 2"))
        create_creature(Creature(name="TestCreature1", desc="Test Description 1", appearance="Test Appearance 1",
                                 behavior="Test Behavior 1", evolve="TestEvolution1"))
        create_creature(Creature(name="TestCreature2", desc="Test Description 2", appearance="Test Appearance 2",
                                 behavior="Test Behavior 2", evolve="TestEvolution2"))
        create_waifu(
            Waifu(name="TestWaifu1", desc="Test Description 1", face="Test Face 1", body="Test Body 1",
                      clothing="Test Clothing 1", archetype=["TestArchetype1"], personality="Test Personality 1",
                      quirk="Test Quirk 1", origin="TestOrigin1"))
        create_waifu(
            Waifu(name="TestWaifu2", desc="Test Description 2", face="Test Face 2", body="Test Body 2",
                      clothing="Test Clothing 2", archetype=["TestArchetype2"], personality="Test Personality 2",
                      quirk="Test Quirk 2", origin="TestOrigin2"))
        create_archetype(Archetype(name="TestArchetype1", desc="Test Description 1"))
        create_archetype(Archetype(name="TestArchetype2", desc="Test Description 2"))

        # Test get_all functions
        self.assertEqual(len(get_all_users()), 2)
        self.assertEqual(len(get_all_materials()), 2)
        self.assertEqual(len(get_all_creatures()), 2)
        self.assertEqual(len(get_all_waifus()), 2)
        self.assertEqual(len(get_all_archetypes()), 2)


if __name__ == '__main__':
    unittest.main()