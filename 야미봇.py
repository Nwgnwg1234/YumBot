import discord,datetime,pytz,os

client = discord.Client()

@client.event
async def on_ready(): # 봇 온라인 전환시 실행
    print("봇 온라인")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("야미"))

@client.event #도움말(임베드) - https://youtu.be/SKFEAi9ViEM
async def on_message(message):
    if message.content == "야미봇 도움말": #1 도움말(임베드) - https://youtu.be/SKFEAi9ViEM
        embed = discord.Embed(title="명령어 목록", description="맛없다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="안녕", value="야미봇이 인사합니다", inline=False)
        embed.add_field(name="야미봇 도움말", value="방금 너가 쓴 명령어", inline=False)
        embed.add_field(name="명령어", value="야미봇이 자기소개를 합니다", inline=False)

        embed.set_footer(text="개야미 불개야미")
        await message.channel.send (embed=embed)
    
    if message.content == "야미봇 자기소개": #2 자기소개(임베드) - https://youtu.be/SKFEAi9ViEM
        embed = discord.Embed(title="야미봇", description="맛있다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="생일", value="2022년 7월 30일", inline=False)
        embed.add_field(name="제작자", value="너만을위한갱킹 #6957", inline=False)
        embed.add_field(name="명령어", value="야미봇 도움말", inline=False)

        embed.set_footer(text="개야미 불개야미")
        await message.channel.send (embed=embed)
    
    if message.content == "안녕": #3 인사
        await message.channel.send ("{}, 안녕".format(message.author.mention))
    
    if message.content == "야미봇 상점": #4 상점 열기
        embed = discord.Embed(title="상점", description="야미한게 많다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)

        embed.add_field(name="비타500", value="500코인", inline=False)

        embed.set_footer(text="야미야미마트")
        await message.channel.send (embed=embed)
    
    if message.content == "야미봇 들어와": #5 음성채널 입장
        channel1 = message.author.voice.channel
        await channel1.connect()

    if message.content == "야미봇 나가": #6 음성채널 퇴장
        channel = message.author.voice.channel
        await channel.guild.voice_client.disconnect()
    
    #if message.content.startswith("!음악"): #음성채널에 봇을 추가 및 음악 재생

access_token = os.environ["BOT_TOKEN"]
client.run('access_token') #봇 토큰

#이거 좀 지리는데? https://youtu.be/KJWaL7X2tgU
#24시간 구동 후보 1 https://youtu.be/rgVfIrGTavc
#노래봇 소스코드 1 https://github.com/Penguinhing/PengUinBot/commit/18b98df655529476ddac6f9e0522110812a41f29#diff-98b6e574f6423c1e60da0a2cc6710218fb68387e24ea2ebbec14925e1bc753ad
#코드모음 https://www.codegrepper.com/code-examples/python/discord+how+to+make+a+bot+join+voice+channel+in+python
#유튜브 재생 https://webolutions.tistory.com/132.
