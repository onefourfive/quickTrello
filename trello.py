#trello.py
#intended to streamline creating ANA load requests to trello

import requests
import json
import configparser, os

cfgFile = "trelloApi.cfg"

config = configparser.RawConfigParser()
config.read(cfgFile)

apikey = config.get('id', 'key')
apitoken = config.get('id', 'token')

def getBoards(key,token):
	reqUrl = 'https://api.trello.com/1/members/me/boards?fields=name,url'
	payload = {'key':key, 'token':token}
	boards = requests.get(reqUrl, params=payload)
	#print boards.text
	return boards.json()

def getBoardID(boardJson, reqBoard):
	for board in range(len(boards)):
		if boards[board]["name"] == reqBoard:
			return boards[board]["id"]
		elif board == max(range(len(boards))):
			return 0

	
boards = getBoards(apikey,apitoken)

print(getBoardID(boards, "ANA Media"))