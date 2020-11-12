import discord
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('===============')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('&새리야 라고 불러줘!'))


@client.event
async def on_message(message):
    if message.content == "&새리야 안뇽":
        await message.channel.send("안뇨오오오옹")
    if message.content == "&새리 바보":
        await message.channel.send("ㅎ 나한테 참수당하고싶니?")
    if message.content == "&불가새리":
        await message.channel.send("(와작와작)파오웁 쿰척쿰척 맛있당 헤헤")
    if message.content == "&이느 샵샹뇬":
        await message.channel.send("내 사랑 건들면 X진다 ㅡㅡ")
    if message.content == "&새리야":
        await message.channel.send("웅웅!")
    if message.content == "&새리야 자기소개":
        await message.channel.send("안녕? 난 새리봇이야 2020.11.1 alpha bata버전으로 내가 만들어졌고 난 파이썬으로 만들어져있어!(추가적으로 새리봇에게 궁금한게 있으면 &이스터에그 를 적어봐")
    if message.content == "&이스터에그":
        await message.channel.send("사실 주박사는 자바스크립트로 날 만들려고했지만 이 빡대가리가 C언어 밖에 쓸 줄 몰라서 그나마 아는 파이썬으로 날 만든거임 ㅋㅋㄹㅃㅃ")

    if message.content == "&명령어 알려줘":
        await message.channel.send("&새리야 안뇽 : 새리봇과 인사를 합니다\n")
        await message.channel.send("&새리 바보 : 새리봇한테 바보라고 합니다\n")
        await message.channel.send("&불가새리 : 새리가 만들어 달라고 한 명령어임\n")
        await message.channel.send("&이느 샵샹뇬 : 새리의 남친\n")
        await message.channel.send("&새리야 : 새리봇을 부릅니다.\n")
        await message.channel.send("&새리야 자기소개 : 새리봇이 스스로 자신을 소개합니다.\n")


async def on_member_join(member):
    await member.send("님 새리해서버에 오신 것을 환영합니다")


access_token = os.environ['BOT_TOKEN']
client.run("access_token")
