import config
import data_manager
import user_actions
import discord

# This is the overall Discord Bot Logic
# Only bot.py and discord.py can contain discord library

async def dungeon_action():
    while True:
        item = await config.rpg_queue.get()
        instruction:str = item['task']
        interaction:discord.Interaction= item['interaction']
        username = interaction.user.display_name
        user = data_manager.get_user(username)
        if user:
            if instruction == "fusion":
                message = await user_actions.combine_element(username,item['mat1'],item['mat2'])
            elif instruction == "transmutate":
                message = await user_actions.transmutate_material(username, item['mat'])
            elif instruction == "evolution":
                message = await user_actions.evolve_creature(username, item['creature'])
            else:
                message = "Yeah, it's not working..."

        else:
            message = "You haven't made an account yet, please register with /register"
        await send_webhook_message(interaction.channel,message)
        config.rpg_queue.task_done()


async def send_webhook_message(channel: discord.abc.GuildChannel, content: str,
                               avatar_url: str = "https://i.imgur.com/rpd75Pr.jpg", username: str = "RPG") -> None:
    # Check if the channel is a text channel or a thread
    if isinstance(channel, discord.TextChannel):
        webhook_list = await channel.webhooks()

        webhook = None
        for existing_webhook in webhook_list:
            if existing_webhook.name == "RPGAI":
                webhook = existing_webhook
                break

        if not webhook:
            webhook = await channel.create_webhook(name="RPGAI")

        # Split content into chunks of 2000 characters or less
        chunks = [content[i:i + 2000] for i in range(0, len(content), 2000)]

        for chunk in chunks:
            await webhook.send(chunk, username=username, avatar_url=avatar_url)
    else:
        print("The channel must be either a TextChannel or a Thread.")
    return