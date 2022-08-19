import discord

TOKEN = ''
EMOJI = ''

client = discord.Client(
    intents=discord.Intents.all()
)


@client.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent):
    if str(payload.emoji) != EMOJI:
        return

    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)

    await payload.member.send(
        f'Saved message from {message.author.name} in {message.guild.name}: https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}'
        )


if __name__ == '__main__':
    client.run(TOKEN)
