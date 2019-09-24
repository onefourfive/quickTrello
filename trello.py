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

def getBoards():
	reqUrl = 'https://api.trello.com/1/members/me/boards?fields=name,url'
	payload = {'key':apikey, 'token':apitoken}
	boards = requests.get(reqUrl, params=payload)
	#print boards.text
	return boards.json()

def getBoardID(boardJson, reqBoard):
	for board in range(len(boards)):
		if boards[board]["name"] == reqBoard:
			return boards[board]["id"]
		elif board == max(range(len(boards))):
			return 0

def getBoardLists(boardID):
	reqUrl = "https://api.trello.com/1/boards/" + boardID + "/lists?&filter=open&fields=all"
	payload = {
		'fields': 'name,id', 
		'card_fields': 'name,id', 
		'cards': 'all', 
		'key':apikey, 
		'token':apitoken
		}
	lists = requests.get(reqUrl, params=payload)
	return lists.json()

def addCard(listId, cardName, cardDesc):
	reqUrl = "https://api.trello.com/1/cards"
	payload = {
		'name': cardName,
		'desc': cardDesc,
		'idList': listId,
		'key':apikey, 
		'token':apitoken
	}
	cardAdd = requests.post(reqUrl, params=payload)
	return cardAdd.json()

boards = getBoards()
print(json.dumps(boards, indent=4))
print(boards[3]["name"])

#print(getBoardLists(boards[3]["id"]))
print(json.dumps(getBoardLists(boards[3]["id"]), indent=4))

#print(getBoardID(boards, "ANA Media"))