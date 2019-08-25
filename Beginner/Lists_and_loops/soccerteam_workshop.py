# TODO Create an empty list to maintain the player names

players = []

# TODO Ask the user if they'd like to add players to the list.

question = input("Would you like to add a player to the team?  (Y/N):     ")

# If the user answers "Yes", let them type in a name and add it to the list.
while question == "y":
    new_player = input("Please enter a player you'd like to enter to the team:    " )
    players.append(new_player)
    question = input("Would you like to add another player?  (Y/N):     ")
    
# If the user answers "No", print out the team 'roster'  
# TODO print the number of players on the team
# TODO Print the player number and the player name
# The player number should start at the number one

player_number = 1
for player in players:
    print("Player {}: {}".format(player_number, player))
    player_number += 1
    
    
goal = int(input("Please select a goalkeeper for the team (enter player number 1-{}):     ".format(len(players))))
goal -= 1
print("You have selected {} as goalkeeper".format(players[goal]))




# TODO Select a goalkeeper from the above roster


# TODO Print the goal keeper's name
# Remember that lists use a zero based index

