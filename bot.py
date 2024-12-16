# This is the Discord Bot Part
# I will see to it that I only need to import model and user action
import asyncio
import os
import data_manager
from discord import app_commands
from dotenv import load_dotenv
import discord
from tinydb import TinyDB

import config
import main
from models import *
import user_actions



def setup_rpg_commands():
    group = app_commands.Group(name="rpg", description="RPG Commands!!!")

    @group.command(name="help", description="Show Game Tutorial!")
    async def rpg_help(interaction: discord.Interaction):
        rpg_help = user_actions.show_help()
        await interaction.response.send_message(rpg_help, ephemeral=True)

    @group.command(name="register", description="Register Yourself!")
    async def rpg_register(interaction: discord.Interaction, desc: str):
        rpg_register = user_actions.create_user(interaction.user.display_name, desc)
        await interaction.response.send_message("Character Created~", ephemeral=True)

    @group.command(name="elements", description="Check Elements!")
    async def rpg_elements(interaction: discord.Interaction):
        elements = user_actions.check_material(interaction.user.display_name)
        await interaction.response.send_message(elements, ephemeral=True)

    @group.command(name="creature", description="Check Creatures!")
    async def rpg_creatures(interaction: discord.Interaction):
        creatures = user_actions.check_creatures(interaction.user.display_name)
        await interaction.response.send_message(creatures, ephemeral=True)

    @group.command(name="creature_detail", description="Check Creature Detail!")
    async def rpg_creature_detail(interaction: discord.Interaction, creature_name: str):
        creature_detail = user_actions.check_creature_detail(creature_name)
        await interaction.response.send_message(creature_detail, ephemeral=True)

    @group.command(name="waifu", description="Check Waifus!")
    async def rpg_waifus(interaction: discord.Interaction):
        waifus = user_actions.check_owned_waifu(interaction.user.display_name)
        await interaction.response.send_message(waifus, ephemeral=True)

    @group.command(name="waifu_detail", description="Check Waifu Detail!")
    async def rpg_waifu_detail(interaction: discord.Interaction, waifu_uuid:str):
        waifu_detail = user_actions.check_waifu_detail(waifu_uuid)
        await main.send_webhook_message(interaction.channel,waifu_detail)

    @group.command(name="fusion", description="Combine Elements!")
    async def rpg_fusion(interaction: discord.Interaction, mat1: str, mat2: str):
        task = {
            'interaction':interaction,
            'mat1': mat1,
            'mat2': mat2,
            'task': "fusion"
        }
        config.rpg_queue.put_nowait(task)
        await interaction.response.send_message("Processing Materials...", ephemeral=True)

    @group.command(name="transmutation", description="Create Creature!")
    async def rpg_transmutate(interaction: discord.Interaction, mat: str):
        task = {
            'interaction': interaction,
            'mat': mat,
            'task': "transmutate"
        }
        config.rpg_queue.put_nowait(task)
        await interaction.response.send_message("Processing Material...", ephemeral=True)

    @group.command(name="evolution", description="Create Waifu!")
    async def rpg_evolve(interaction: discord.Interaction, creature_name: str):
        task = {
            'interaction': interaction,
            'creature': creature_name,
            'task': "evolution"
        }
        config.rpg_queue.put_nowait(task)
        await interaction.response.send_message("Processing Creature...", ephemeral=True)

    tree.add_command(group)




load_dotenv()
discord_token: str | None = os.getenv("DISCORD_TOKEN")
if discord_token is None:
    raise RuntimeError("$DISCORD_TOKEN env variable is not set!")

client = config.client

tree = app_commands.CommandTree(client)



@client.event
async def on_ready():
    # Let owner known in the console that the bot is now running!
    print(f'Discord Bot is Loading...')

    # await data_manager.write_attribute_data(await data_manager_json.read_attribute_data())
    # Setup the Connection with API
    db = TinyDB('main_database.json')
    await config.initialize()
    await config.setup()
    # attribute_info: AttributeInfo = await data_manager.read_attribute_data()
    # format_attribute_info(attribute_info)
    
    setup_rpg_commands()
    asyncio.create_task(main.dungeon_action())
    await tree.sync(guild=None)
    print(f'Discord Bot is up and running.')


# Run the Bot
client.run(discord_token)
