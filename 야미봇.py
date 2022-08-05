import discord,os

client = discord.Client()

@client.event
async def on_ready(): # 봇 온라인 전환시 실행
    print("봇 온라인")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("야미"))

@client.event #도움말(임베드) - https://youtu.be/SKFEAi9ViEM
async def on_message(message):
   
    if message.content == "안녕": #3 인사
        await message.channel.send ("{}, 안녕".format(message.author.mention))

access_token = os.environ["BOT_TOKEN"]
client.run('access_token') #봇 토큰

#이거 좀 지리는데? https://youtu.be/KJWaL7X2tgU
#24시간 구동 후보 1 https://youtu.be/rgVfIrGTavc
#노래봇 소스코드 1 https://github.com/Penguinhing/PengUinBot/commit/18b98df655529476ddac6f9e0522110812a41f29#diff-98b6e574f6423c1e60da0a2cc6710218fb68387e24ea2ebbec14925e1bc753ad
#코드모음 https://www.codegrepper.com/code-examples/python/discord+how+to+make+a+bot+join+voice+channel+in+python
#유튜브 재생 https://webolutions.tistory.com/132.
