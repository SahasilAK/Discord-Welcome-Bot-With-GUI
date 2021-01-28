import discord
import os
from keep_alive import keep_alive
import json
# from my_token import token


SERVER_ID = 'Your server id'
CHANNEL_ID = 'welcome channel id'
ROLE_ID = "role to assign id"


class MyBot:
	def run_the_bot(self):
				
		intents =  discord.Intents.default()
		intents.members = True
		client = discord.Client(intents=intents)

		with open('data.json','r') as data_file:
			data = json.load(data_file)
		welcome_data = data['welcome']
		activity_data =  data['activity']
			


		@client.event
		async def on_ready():

			# ________________bot activity section__________
			await client.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = activity_data))
			print(f'We have logged in as {client.user}')


		@client.event
		async def on_member_join(member):
			guild = client.get_guild(SERVER_ID)
			welcome_channel = guild.get_channel(CHANNEL_ID)

			#_____assigning initial roles______
			# role = guild.get_role(ROLE_ID)
			# await member.add_roles(role)

			await welcome_channel.send(f'{welcome_data} {member.mention} ! :partying_face:') #channel welcome message
			await member.send(f'{welcome_data} {member.mention} ! :partying_face:') #pm welcome message

	#message response section		
		# @client.event
		# async def on_message(message):
		# 	if not message.author.bot:
		# 		if message.content == 'hi':

		# 			await message.channel.send('hellow frend') 




		keep_alive()
		client.run(os.getenv('TOKEN'))
# 		client.run(token)
