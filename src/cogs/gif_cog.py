import random
from discord import File
from discord.ext import commands

class GifCog(commands.Cog, name="Gifs"):
  # UFS discord GIF commands
  def __init__(self, bot):
    self.gif_path = "src/data/gifs/"
    self.M3GAN_path = self.gif_path + "releases/M3GAN/M3GAN"
    self.RRR_path = self.gif_path + "releases/RRR/RRR"
    self.sorcerers_path = self.gif_path + "releases/sorcerers"
    self.minions_path = self.gif_path + "releases/minions/minions"
    self.elvis_path = self.gif_path + "releases/elvis/elvis"
    self.puss_path = self.gif_path + "releases/pussnboots/puss"
    self.pizza_path = self.gif_path + "pizzaTime"
    self.bait_path = self.gif_path + "MadMaxBait"

    self.bot = bot
    
  
  ##### 2023 RELATED GIFS #####
  @commands.hybrid_command(name="m3gan", 
                description="M3GAN (2023)")
  async def m3gan(self, ctx):
    chance = str(random.randint(1, 2))
    await ctx.send(
      file=File(self.M3GAN_path + chance + '.gif'))
  
  
  ##### 2022 RELATED GIFS #####
  @commands.hybrid_command(name="rrr", 
                description="RRR (2022)")
  async def RRR(self, ctx):
    chance = str(random.randint(1, 4))
    await ctx.send(
      file=File(self.RRR_path + chance + '.gif'))
  
  
  @commands.hybrid_command(name="sorcerers",
                description="Wong fortifies your mind")
  async def sorcerers(ctx, self):
    await ctx.send(
      file=File(self.sorcerers_path + '.gif'))
  
  
  @commands.hybrid_command(name="minions",
                description="Minions: Rise of Gru (2022)")
  async def minions(self, ctx):
    chance = str(random.randint(1, 4))
    await ctx.send(
      file=File(self.minions_path + chance + '.gif'))
  
  
  @commands.hybrid_command(name="elvis",
                description="Elvis (2022)")
  async def elvis(ctx, self):
    chance = str(random.randint(1, 4))
    await ctx.send(
      file=File(self.elvis_path + chance + '.gif'))
  
  
  @commands.hybrid_command(name="everything",
                description="It has everything to do with us")
  async def everything(self, ctx):
    await ctx.send(
      file=File(self.elvis_path + 'Everything.gif'))
  
  
  @commands.hybrid_command(name="puss",
                description="Puss in Boots: The Last Wish (2022)")
  async def puss(self, ctx):
    chance = str(random.randint(1, 5))
    await ctx.send(
      file=File(self.puss_path + chance + '.gif'))
  
  
  ##### REACTION GIFS #####
  @commands.hybrid_command(name="pizza",
                description="Pizza time")
  async def pizza(self, ctx):
    await ctx.send(
      file=File(self.pizza_path + '.gif'))
  
  
  @commands.hybrid_command(name="bait",
                description="Mad Max calls out bait")
  async def bait(self, ctx):
    await ctx.send(
      file=File(self.bait_path + '.gif'))