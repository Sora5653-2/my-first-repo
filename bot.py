# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'OTc1Mjk2OTM3MjMyMzA2MTk2.GQs4Mc.D2Z7jjRFhcUkSNGX0pytgYuiwDgxTw-mc57ODo'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

@client.event
async def on_message(message):
    if message.content == '/clean':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
        else:
            await message.channel.send('庶民の分際で削除とか図るな')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)