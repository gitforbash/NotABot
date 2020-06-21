import discord
import youtube_dl as youtube
import urllib.request
from bs4 import BeautifulSoup


disclosure_message = '''
> Here Are the Top 3 Results
'''
choice_message = '''
> Which Would You Like to Listen To?
     Please Choose a Number **1-3** :)
'''
now_playing_message = '''
> Now Playing %s
'''

client = discord.Client()

@client.event
async def on_message(message):
	if message.content.find(">play") != -1:
		message.content = message.content.replace('>play ', '')
		await message.channel.send('Searching For "%s"...' % (message.content))

		query = urllib.parse.quote(message.content)
		url = "https://www.youtube.com/results?search_query=" + query

		response = urllib.request.urlopen(url)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')

		await message.channel.send(disclosure_message)

		iteration = 0
		for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
			if 'channel' or 'googleadservices.com' in vid['href']:
				continue
			print('youtube.com/' + vid['href'])

			iteration = iteration + 1

			await message.channel.send('https://www.youtube.com' + vid['href'])
			results = [].append('https://www.youtube.com' + vid['href'])

			if iteration == 3:
				break
		await message.channel.send(choice_message)
		await message.channel.send('I am a work in progress. Report any bugs to https://github.com/gitforbash/NotABot/issues.')

token = 'ACCESS-TOKEN'
client.run(token)
