import discord, random
from discord.ext import tasks
from itertools import cycle

client = discord.Client()

client.stock_value = 100
client.balance = 10000
client.shares = 0

bot_status = cycle(['Status 1', 'Status 2', 'Status 3'])


async def return_args(*args):
    stock_channel = client.get_channel(970034712783511593)
    await stock_channel.send(args)


@client.event
async def on_ready():
    # stocks.start()
    # companies.start()
    update_stock.start()
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message, *args):
    if message.author == client.user:
        return

    # await return_args(message.content)
    if message.content.startswith("!buy"):
        client.shares += 1
    if message.content.startswith("!shares"):
        await message.channel.send(client.shares)
    if message.content.startswith("!purge"):
        await message.channel.purge(limit=100)












@tasks.loop(seconds=15)
async def update_stock():
    client.stock_price = 100
    client.stock_dict = {
                         "Tesla": "https://g.foolcdn.com/art/companylogos/square/tsla.png",
                         "Apple": "https://media.idownloadblog.com/wp-content/uploads/2018/07/Apple-logo-black-and-white.png",
                         "Google": "https://blog.hubspot.com/hubfs/image8-2.jpg"
                         }

    client.stock_channel = client.get_channel(970034712783511593)
    await client.stock_channel.purge(limit=len(client.stock_dict))

    for key, value in client.stock_dict.items():

        # GET THE STOCK PRICE INCREASE OR DECREASE
        client.inc_dec = random.randint(1, 2)
        client.inc_dec_amount = random.randint(5, 25)

        if client.inc_dec == 1:
            client.stock_price += client.inc_dec_amount
        else:
            client.stock_price -= client.inc_dec_amount
            if client.stock_price <= 0:
                client.stock_price = 0


        embed = discord.Embed(title=key, url="",
                              description="",
                              color=0x109319)

        embed.set_author(name="Joshua1N", url="https://www.twitch.tv/c9cheeto", icon_url="")
        embed.set_thumbnail(url=value)
        embed.add_field(name=f"Stock Price: {client.stock_price}", value="\u200b")
        embed.set_footer(text=f"Shares owned: {client.shares}")
        await client.stock_channel.send(embed=embed)










BOT_TOKEN = 'OTcwMDM0ODUxOTQ2MzMyMTcw.Ym2FWw.KKbG8rI6OCH1b48vOkQHJpCX6K4'
client.run(BOT_TOKEN)
