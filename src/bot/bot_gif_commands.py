from settings import discord, tree, random, UFS_GUILD_ID

class BotGifs:
  # UFS discord GIF commands
  
  ##### 2023 RELATED GIFS #####
  @tree.command(name="m3gan", 
                description="M3GAN (2023)", 
                guild=discord.Object(id=UFS_GUILD_ID))
  async def m3gan(interaction):
    chance = str(random.randint(1, 2))
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/M3GAN/M3GAN' + chance + '.gif'))
  
  
  ##### 2022 RELATED GIFS #####
  @tree.command(name="rrr", 
                description="RRR (2022)", 
                guild=discord.Object(id=UFS_GUILD_ID))
  async def RRR(interaction):
    chance = str(random.randint(1, 4))
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/RRR/RRR' + chance + '.gif'))
  
  
  @tree.command(name="sorcerers",
                description="Wong fortifies your mind",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def sorcerers(interaction):
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/sorcerers.gif'))
  
  
  @tree.command(name="minions",
                description="Minions: Rise of Gru (2022)",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def minions(interaction):
    chance = str(random.randint(1, 4))
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/minions/minions' + chance + '.gif'))
  
  
  @tree.command(name="elvis",
                description="Elvis (2022)",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def elvis(interaction):
    chance = str(random.randint(1, 4))
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/elvis/elvis' + chance + '.gif'))
  
  
  @tree.command(name="everything",
                description="It has everything to do with us",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def everything(interaction):
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/elvis/elvisEverything.gif'))
  
  
  @tree.command(name="puss",
                description="Puss in Boots: The Last Wish (2022)",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def puss(interaction):
    chance = str(random.randint(1, 5))
    await interaction.response.send_message(
      file=discord.File('Gifs/Releases/pussnboots/puss' + chance + '.gif'))
  
  
  ##### REACTION GIFS #####
  @tree.command(name="pizza",
                description="Pizza time",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def pizza(interaction):
    await interaction.response.send_message(
      file=discord.File('Gifs/pizzaTime.gif'))
  
  
  @tree.command(name="bait",
                description="Mad Max calls out bait",
                guild=discord.Object(UFS_GUILD_ID))
  async def bait(interaction):
    await interaction.response.send_message(
      file=discord.File('Gifs/MadMaxBait.gif'))