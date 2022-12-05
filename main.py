import nextcord
from nextcord.ext import commands
from craiyon import Craiyon
from PIL import Image
from io import BytesIO
import time
import base64
import keep_alive

keep_alive.keep_alive()

bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())
bot.remove_command("help")


@bot.event
async def on_ready():
  print("I am ready")


@bot.command()
async def help(ctx):
  embed = nextcord.Embed(title="Hatsune Miku v3 指令",
                         description="!generate + 你想要的图片(越详细越好)",
                         color=0x00D2FF)
  await ctx.send(embed=embed)


@bot.command()
async def generate(ctx: commands.Context, *, prompt: str):
  ETA = int(time.time() + 60)
  msg = await ctx.send(f"你的图片大概在1分钟后完成 ||**<t:{ETA}:R>**||")
  generator = Craiyon()
  result = generator.generate(prompt)
  images = result.images
  for i in images:
    image = BytesIO(base64.decodebytes(i.encode("utf=8")))
    return await msg.edit(content="完成!",
                          file=nextcord.File(image, "generatedImage.png"))


bot.run(
  "Your mom")
