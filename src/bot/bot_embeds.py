from settings import discord

class BotEmbeds:
  # Embed Quote and Send to Channel
  async def UFS_cmd_quote(interaction, quote):
    # Embed Quote
    quote_embed = discord.Embed() # Embed object
    quote_embed.set_author(name=quote.members()) # Add members as author
    quote_embed.add_field(name="\u200b", value=quote.quotes(), inline=False) # Add quote
    quote_embed.add_field(name="\u200b", value=quote.date(), inline=False) # Add date
    
    # Send Quote
    await interaction.response.send_message(embed=quote_embed)

  # Embed Letterboxd Quote and Send to Channel
  async def UFS_cmd_lbquote(interaction, lbquote, poster):
    # Embed Quote
    lbquote_embed = discord.Embed() # Embed object
    lbquote_embed.set_thumbnail(url=poster) # Add poster jpeg
    lbquote_embed.set_author(name=lbquote.film() + " (" + lbquote.year() + ")") # Add film name and year as author
    lbquote_embed.add_field(name="\u200b", value=lbquote.members(), inline=True) # Add members
    lbquote_embed.add_field(name="\u200b", value=lbquote.date(), inline=False) # Add date
    lbquote_embed.add_field(name="\u200b", value=lbquote.quotes(), inline=False) # Add quote

    # Send Quote
    await interaction.response.send_message(embed=lbquote_embed)

  # Embed Selected MotW/AotW Nominees and Send to Channel
  async def UFS_cmd_nominate(interaction, nominees, nominee_type):
    # Initialize empty pings and embed object
    ping_users = ""
    embed = discord.Embed()

    # Determine author from nomine type
    if nominee_type:
      embed.set_author(name="Movie Nominees")
    else:
      embed.set_author("Music Winner")

    # Embed to Message and Ping
    for i, nominee in enumerate(nominees, 1):
      embed.add_field(name="Nominee #{}".format(i), value=nominee.name(), inline=False) # Add member
      ping_users += "<@" + nominee.discord_ID() + ">" + " " # Add to ping

    # Send Winners
    await interaction.response.send_message(embed=embed, content=ping_users)

  async def UFS_cmd_roll(interaction, sides, n):
    # Display invalid input
    if n is None:
      await interaction.response.send_message(
        "What kind of die are you rolling?", ephemeral=True)
    # Display roll
    else:
      await interaction.response.send_message(
        f"Input: {sides}\nYou rolled a {n}!")