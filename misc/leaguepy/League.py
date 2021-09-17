import requests # module for https request to the League Server
import json
import collections

APIKEY = "RGAPI-7cbe79bb-e9ef-44db-a8ed-4eb28ca29645" # Riot will give you a key, key has to be renewed daily


def requestSummonerName(name):
	summonerName = getSummonerName(name) # Parse the name into correct format
	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s" %(summonerName, APIKEY)
	riotData = requests.get(URL).json() # Requests the data from riot and turn it into json format
	summonerName = riotData['name']
	return summonerName

#----------------------------------------------------------------#
def getSummonerName(name):
	if (' ' in name == True): # Case if summoner name has a space
		name = name.replace(" ", "%")
	return name

#----------------------------------------------------------------#
def requestSummonerAccountID(name):
	summonerName = requestSummonerName(getSummonerName(name))
	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s" %(summonerName, APIKEY)
	riotData = requests.get(URL).json()
	summonerID = riotData['accountId']
	return summonerID

#----------------------------------------------------------------#
def requestSummonerID(name):
	summonerName = requestSummonerName(getSummonerName(name))
	URL = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s?api_key=%s" %(summonerName, APIKEY)
	riotData = requests.get(URL).json()
	summonerID = riotData['id']
	return summonerID

#----------------------------------------------------------------#
def requestSummonerRank(name): 
	summonerID = (str) (requestSummonerID(name))
	URL = "https://na1.api.riotgames.com/lol/league/v3/positions/by-summoner/%s?api_key=%s" %(summonerID, APIKEY)

	riotData = requests.get(URL).json()
	if (bool(riotData)): # case to make sure the return json file is not empty
		tier = riotData[0]['tier']
		rank = riotData[0]['rank']
		lp = riotData[0]['leaguePoints']
		rankData = "{} | {} {} | {}LP".format(name, tier, rank, lp)
		return (rankData)
	else:
		return -1;

#----------------------------------------------------------------#
def requestChampion(championID):
	with open("championJson.json") as file:
		jsonFile = json.load(file)
	championList = {}
	for champion in jsonFile:
		champName = champion["id"]
		champID = champion["key"]
		championList[champID] = champName # Add it to the dictionary
	return (championList[championID])

#----------------------------------------------------------------#
def requestLastTwentyMatches(name): 
	summonerName = requestSummonerName(getSummonerName(name))
	summonerAccountID = (str) (requestSummonerAccountID(summonerName))
	URL = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/{}?api_key={}".format(summonerAccountID, APIKEY) 
	riotData = requests.get(URL).json()
	lastTwentyMatches = [] * 30 # initialize a list of 20
	i = 0
	for match in riotData["matches"]:
		if (i == 30):
			break
		lastTwentyMatches.append(match) 
		i = i + 1
	return lastTwentyMatches    

#----------------------------------------------------------------#
def requestMatchData(gameID, championID):

	URL = "https://na1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}".format(gameID, APIKEY)
	riotData = requests.get(URL).json()
	matchOutcome = {}
	team1ID = (riotData["teams"][0]["teamId"])
	team1MatchOutcome = (riotData["teams"][0]["win"])
	team2ID = (riotData["teams"][1]["teamId"])
	team2MatchOutcome = (riotData["teams"][1]["win"])
	matchOutcome[team1ID] = team1MatchOutcome
	matchOutcome[team2ID] = team2MatchOutcome

	winCondition = False
	for participant in riotData['participants']:
		if ((str)(participant["championId"])  == (championID)):
			if (matchOutcome[participant['teamId']] == 'Win'):
				winCondition = True
	return winCondition     

#----------------------------------------------------------------#  
def checkStatusOfPlayer(jsonData):
	if ('status' in jsonData): 
		return True
	return False

#----------------------------------------------------------------#
def getWinLossRatioOfChampions(championList, championListKey, win):
	for key in championListKey:
		count = championList.count(key)
		winRate = float(count/win) * (100.0)
		winRate = float("{0:.2f}".format(winRate))
		print ("{} : {}% WIN RATE | {} wins".format(key, winRate, count))


#----------------------------------------------------------------#                  
# def displayLastTwentyMatches(name):
#   matchList = requestLastTwentyMatches(name)
#   win = 0.0
#   lose = 0.0
#   i = 1
#   winChampList = [] * 30
#   winChampListkey = [] * 30

#   loseChampList = [] * 30
#   loseChampListKey = [] * 30

#   for match in matchList:
#       championID = (str)(match["champion"])
#       champion = requestChampion(championID)
#       role = (str) (match["role"])
#       gameID = match["gameId"]
#       winCondition = requestMatchData(gameID, championID)
#       if (winCondition == True):
#           win = win + 1
#           winChampList.append(champion)
#           winChampListkey.append(champion)
#       else:
#           lose = lose + 1
#           loseChampList.append(champion)
#       i = i+1 

#   URL = "https://na1.api.riotgames.com/lol/match/v3/matches/{}?api_key={}".format(gameID, APIKEY)
#   riotData = requests.get(URL).json()
#   matchOutcome = {}
#   team1ID = (riotData["teams"][0]["teamId"])
#   team1MatchOutcome = (riotData["teams"][0]["win"])
#   team2ID = (riotData["teams"][1]["teamId"])
#   team2MatchOutcome = (riotData["teams"][1]["win"])
#   matchOutcome[team1ID] = team1MatchOutcome
#   matchOutcome[team2ID] = team2MatchOutcome

#   winCondition = False
#   for participant in riotData['participants']:
#       if ((str)(participant["championId"])  == (championID)):
#           if (matchOutcome[participant['teamId']] == 'Win'):
#               winCondition = True
#   return winCondition
					
def displayLastTwentyMatches(name):
	matchList = requestLastTwentyMatches(name)
	win = 0.0
	lose = 0.0
	i = 1
	winChampList = [] * 30
	winChampListkey = [] * 30

	loseChampList = [] * 30
	loseChampListKey = [] * 30

	for match in matchList:
		championID = (str)(match["champion"])
		champion = requestChampion(championID)
		role = (str) (match["role"])
		gameID = match["gameId"]
		winCondition = requestMatchData(gameID, championID)
		if (winCondition == True):
			win = win + 1
			winChampList.append(champion)
			# print("{}. {} | {} | WIN".format(i,champion, role))
		else:
			lose = lose + 1
			loseChampList.append(champion)
			# print("{}. {} | {} | LOSE".format(i, champion, role))
		i = i+1

	# print (collections.Counter(winChampList))
	winChampListkey = list(set(winChampList))
	getWinLossRatioOfChampions(winChampList, winChampListkey, win)
	print ("Last 30 matches: {} WIN  {} Loss".format(win,lose)) 
	
	

#----------------------------------------------------------------#

def checkStatusOfPlayer(jsonData):
	if ('status' in jsonData):
		return True
	return False

def displaySummonerInfoNA(name):
	print(requestSummonerRank(name))

#----------------------------------------------------------------#
def displaySummonerCurrentMatch(name):
	summonerID = (str) (requestSummonerID(name))
	URL = "https://na1.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/%s?api_key=%s" %(summonerID, APIKEY)
	riotData = requests.get(URL).json()

	if (checkStatusOfPlayer(riotData)):
		print("This player is not active.")
	else: # Player is active
		team1 = [] * 5
		team2 = [] * 5
		for player in riotData['participants']:
			if (player['teamId'] == 100):
				team1.append(player['summonerName'])
			else:
				team2.append(player['summonerName'])
		for player in team1:
			rankData = requestSummonerRank(player)
			if(rankData != -1):
				print(rankData)
		print("----------------------------------")
		for player in team2:
			rankData = requestSummonerRank(player)
			if(rankData != -1):
				print(rankData)

#----------------------------------------------------------------#
def displayOptions():
	print("\nHello, what would you like to view? ")
	print("Find a summoner rank? Press 1")
	print("Find current match information? Press 2")
	print("Show the last 30 matches stats? Press 3")
	print("Quit Application? Press 4")

# ------------------------------------------------------------ #
def main(): 
	displayOptions()
	option = -1

	while (option != '4' ):
		option = (str) (input("My Choice: #"))
		if (option == '1'):
			name =  raw_input("\nWhat is your summonerName? ")
			displaySummonerInfoNA(name)
		elif(option == '2'):
			name = raw_input("\nWhat is your summonerName? ")
			displaySummonerCurrentMatch(name)
		elif(option == '3'):
			name = raw_input("\nWhat is your summonerName? ")
			displayLastTwentyMatches(name)      
		elif(option == '4'):
			print("See you soon!")
			break

		cont = raw_input("Continue (y/n)? ")
		if (cont == 'y' or cont == 'Y'):
			displayOptions()    
		else:
			print("See you soon!")
			break
	
	print("\nHello, what would you like to view? ")
	print("Find a summoner rank? Press 1")
	print("Find current match information? Press 2")
	print("Quit Application? Press 3")



if __name__ == "__main__":
	main()