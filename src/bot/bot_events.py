# Event if bot is ready
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await tree.sync(guild=discord.Object(id=UFS_GUILD_ID))