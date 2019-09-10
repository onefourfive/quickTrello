#trello.py
#intended to streamline creating ANA load requests to trello

import requests
import json

apikey = "ccb8143fdd68c3e43ba4e98d1eabfd62"
apitoken = "5264495a70ef1da99f8907626a5235c5650c516284853af2160fab8d1ca184c3"

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