# This is the Discord Bot Part
# I will see to it that I only need to import model and user action
import asyncio
import os

from discord import app_commands
from dotenv import load_dotenv
import discord

import config
from models import *
import user_actions

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
    await config.setup()
    # attribute_info: AttributeInfo = await data_manager.read_attribute_data()
    # format_attribute_info(attribute_info)

    setup_rpg_commands()

    await tree.sync(guild=None)
    print(f'Discord Bot is up and running.')


# Run the Bot
client.run(discord_token)


def setup_rpg_commands():
    group = app_commands.Group(name="rpg", description="RPG Commands!!!")

    @group.command(name="help", description="Show Game Tutorial!")
    async def rpg_help(interaction: discord.Interaction):
        rpg_help = user_actions.show_help()
        await interaction.response.send_message(rpg_help, ephemeral=True)

    @group.command(name="register", description="Register Yourself!")
    async def rpg_register(interaction: discord.Interaction, desc: str):
        rpg_register = user_actions.create_user(interaction.user.display_name, desc)
        await interaction.response.send_message(rpg_register, ephemeral=True)

    @group.command(name="elements", description="Check Elements!")
    async def rpg_elements(interaction: discord.Interaction):
        elements = user_actions.check_material(interaction.user.display_name)
        await interaction.response.send_message(elements, ephemeral=True)

    @group.command(name="creature", description="Check Creatures!")
    async def rpg_creatures(interaction: discord.Interaction):
        elements = user_actions.check_creatures(interaction.user.display_name)
        await interaction.response.send_message(elements, ephemeral=True)

    @group.command(name="waifu", description="Check Waifus!")
    async def rpg_waifus(interaction: discord.Interaction):
        elements = user_actions.check_owned_waifu(interaction.user.display_name)
        await interaction.response.send_message(elements, ephemeral=True)

    @group.command(name="fusion", description="Combine Elements!")
    async def rpg_fusion(interaction: discord.Interaction, mat1: str, mat2: str):
        config.rpg_queue.put_nowait(
            user_actions.combine_element(interaction.user.display_name, mat1, mat2)
        )
        await interaction.response.send_message("Processing Materials...", ephemeral=True)

    @group.command(name="transmutation", description="Create Creature!")
    async def rpg_transmutate(interaction: discord.Interaction, mat: str):
        config.rpg_queue.put_nowait(
            user_actions.transmutate_material(interaction.user.display_name, mat)
        )
        await interaction.response.send_message("Processing Material...", ephemeral=True)

    @group.command(name="evolution", description="Create Waifu!")
    async def rpg_evolve(interaction: discord.Interaction, creature_name: str):
        config.rpg_queue.put_nowait(
            user_actions.evolve_creature(interaction.user.display_name, creature_name)
        )
        await interaction.response.send_message("Processing Creature...", ephemeral=True)

    tree.add_command(group)
