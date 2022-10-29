players = {}

playerId = input("Enter player id: ")
playerName = input("Enter name: ")
playerBirthDate = input("Enter the birth date: ")
playerNationality = input("Enter the nationality: ")
playerTeam = input("Enter the team: ")
playerHistory = input("Enter the history: ")


players[playerId] = {
    "playerName": playerName,
    "playerBirthDate": playerBirthDate,
    "playerNationality": playerNationality,
    "playerTeam": playerTeam,
    "playerHistory": playerHistory,           # you can use split method like playerHistory.split(",")
}

playerId = input("Enter player id: ")
playerName = input("Enter name: ")
playerBirthDate = input("Enter the birth date: ")
playerNationality = input("Enter the nationality: ")
playerTeam = input("Enter the team: ")
playerHistory = input("Enter the history: ")


players[playerId] = {
    "playerName": playerName,
    "playerBirthDate": playerBirthDate,
    "playerNationality": playerNationality,
    "playerTeam": playerTeam,
    "playerHistory": playerHistory,
}

print(players)

# Q2 > Find the player based on the Id

playersDictionary={
    '1': {'playerName': 'Ronaldo', 'playerBirthDate': '1985', 'playerNationality': 'Portugal', 'playerTeam': 'Portugal', 'playerHistory': 'Juventus, Real Madrid, Portugal'}, 
    '2': {'playerName': 'Messi', 'playerBirthDate': '1987', 'playerNationality': 'Argentina', 'playerTeam': 'Barcelona', 'playerHistory': 'Barcelona, Argentina, Portugal'}
    }

playerId = input("Enter an id: ")
player = playersDictionary[playerId]

print(player)

# Q3 > Delete the player basd on Id
playerId = input("Enter an id: ")

playerId = input("Enter an id: ")
del playersDictionary[playerId]
print(playersDictionary)
