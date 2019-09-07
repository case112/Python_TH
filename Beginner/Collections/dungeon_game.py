# P, but the monster, the door, and the shrine (explained below) are displayed also as M, D, and S respectively.
#The player and monster hp are displayed as numbers, and their hp bars are displayed as Xs and Ys respectively which decrease every -20 hp.
#If the player makes an invalid move, they lose 5 hp.
#If the player encounters the monster, the game will randomly generate 0 or 1. If the number is 0, the player loses 10 hp. If the number is 1, the monster loses 10 hp unless killed.
#If the player's hp reaches 0, the player loses. If the monster's hp reaches 0 the monster dies, and the player is prompted to get to the door.
#The monster moves 1 tile in a random direction every 5 valid moves unless it has been killed.
#The monster heals itself 5 hp every 10 valid moves unless killed or has maximum hp (100).
#The player gets healed 5 hp if they move to the shrine unless they have maximum hp (100). If the monster moves to the shrine, the monster does not get healed.
#If the monster reaches the door, the player loses automatically.
#If the player reaches the door and the monster has not been killed, the player is prompted to kill the monster first.
#If the player reaches the door and the monster has been killed, the player wins.


import random

import os

CELLS = [(c%10, c//10) for c in range(10**2)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 5)

def move_player(player, move):
    x, y = player
    if move == "W":
        x, y = x, y
    elif move == "L" and x > 0:
        x -= 1
    elif move == "R" and x < 9:
        x += 1
    elif move == "U" and y > 0:
        y -= 1
    elif move == "D" and y < 9:
        y += 1
    else:
        print("\n ** A wall is blocking your way! ** \n")
    return x, y

def move_monster(monster, num):
    x, y = monster
    if num == 0:
        if x > 0:
            x -= 1
        elif x == 0:
            x += 1
    elif num == 1:
        if x < 9:
            x += 1
        elif x == 9:
            x -= 1
    elif num == 2:
        if y > 0:
            y -= 1
        elif y == 0:
            y += 1
    elif num == 3:
        if y < 9:
            y += 1
        elif y == 9:
            y -= 1
    return x, y

def get_moves(player):
    moves = ["L", "R", "U", "D", "W"]
    return moves

def draw_map(monster, door, player, shrine, difficulty, monster_found, door_found, shrine_found):
    print(" _" * 10)
    tile = "|{}"
    for cell in CELLS:
        x, y = cell
        if x < 9:
            line_end = ""
            if cell == player:
                output = tile.format("P")
            elif cell == monster and (difficulty != "H" or monster_found):
                output = tile.format("M")
            elif cell == door and (difficulty != "H" or door_found):
                output = tile.format("D")
            elif cell == shrine and (difficulty != "H" or shrine_found):
                output = tile.format("S")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("P|")
            elif cell == monster and (difficulty != "H" or monster_found):
                output = tile.format("M|")
            elif cell == door and (difficulty != "H" or door_found):
                output = tile.format("D|")
            elif cell == shrine and (difficulty != "H" or shrine_found):
                output = tile.format("S|")
            else:
                output = tile.format("_|")
        print(output, end = line_end)

def display_player_hp_bar(player_hp):
    if 80 < player_hp <= 100:
        print("Player:", "X" * 5, player_hp)
    elif 60 < player_hp <= 80:
        print("Player:", "X" * 4, player_hp)
    elif 40 < player_hp <= 60:
        print("Player:", "X" * 3, player_hp)
    elif 20 < player_hp <= 40:
        print("Player:", "X" * 2, player_hp)
    elif 0 < player_hp <= 20:
        print("Player:", "X", player_hp)
    return player_hp

def display_monster_hp_bar(monster_hp):
    if 80 < monster_hp <= 100:
        print("Monster:", "Y" * 5, monster_hp)
    elif 60 < monster_hp <= 80:
        print("Monster:", "Y" * 4, monster_hp)
    elif 40 < monster_hp <= 60:
        print("Monster:", "Y" * 3, monster_hp)
    elif 20 < monster_hp <= 40:
        print("Monster:", "Y" * 2, monster_hp)
    elif 0 < monster_hp <= 20:
        print("Monster:", "Y", monster_hp)
    return monster_hp

def display_message(player):
    moves = ["(L)EFT", "(R)IGHT", "(U)P", "(D)OWN"]
    x, y = player
    if 0 <= x <= 9 and 0 <= y <= 9:
        print("You're currently in room {}.".format(player))
    if x == 0:
        moves.remove("(L)EFT")
    if x == 9:
        moves.remove("(R)IGHT")
    if y == 0:
        moves.remove("(U)P")
    if y == 9:
        moves.remove("(D)OWN")
    print("You can move {}.".format(", ".join(moves)), "or you can (W)AIT.")
    print("Enter Q to quit. Enter C to clear your screen.")

def game_loop():
    monster, door, player, shrine, trap = get_locations()
    num_moves = 0
    player_hp = 100
    monster_hp = 100
    monster_alive = True
    playing = True
    shrine_found = False
    door_found = False
    monster_found = False
    difficulty = input("Choose difficulty: (E)asy (N)ormal, or (H)ard. ")
    while difficulty.upper() != "E" and difficulty.upper() != "N" and difficulty.upper() != "H":
        print("Invalid input.")
        difficulty = input("Choose difficulty: (E)asy, (N)ormal, or (H)ard. ")
    difficulty = difficulty.upper()
    while playing:
        draw_map(monster, door, player, shrine, difficulty, monster_found, door_found, shrine_found)
        valid_moves = get_moves(player)
        display_message(player)
        if difficulty != "E":
            if num_moves > 0 and num_moves % 5 == 0 and monster_alive:
                num = random.randint(0, 3)
                print("\n ** The monster has moved! **\n")
                monster = move_monster(monster, num)
                monster_found = False
            if num_moves > 0 and num_moves % 10 == 0:
                if monster_alive and monster_hp < 100:
                    monster_hp += 5
                    print("\n ** The monster has healed itself 5 hp! **\n")
        if monster == door:
            print("\n ** The monster has escaped! You lose! **\n")
            playing = False
            break
        if display_player_hp_bar(player_hp) <= 0:
            print("\n ** You're dead! **\n")
            playing = False
            break
        if display_monster_hp_bar(monster_hp) <= 0:
            print("\n ** You've killed the monster! Now get to the door! **\n")
            monster_alive = False
        print("{} moves.".format(num_moves))
        move = input("> ")
        move = move.upper()
        if move == "Q":
            print("\n ** See you next time! **\n")
            break
        if move == "C":
            clear_screen()
            continue
        if move in valid_moves:
            player = move_player(player, move)
            num_moves += 1
            if player == monster:
                monster_found = True
                number = random.randint(0, 1)
                if number == 0:
                    player_hp -= 10
                    print("\n ** You've been damaged by the monster! You've lost 10 hp! **\n")
                elif number == 1 and monster_alive:
                    monster_hp -= 10
                    print("\n ** You've damaged the monster! It's lost 10 hp! **\n")
            elif player == shrine:
                shrine_found = True
                if player_hp < 100:
                    player_hp += 5
                    print("\n ** You've been healed 5 hp! **\n")
                else:
                    print("\n ** You're already at full hp! **\n")
            elif player == trap:
                if difficulty == "E":
                    player_hp -= 5
                    print("\n ** You've activated a trap! You've lost 5 hp! **\n")
                elif difficulty == "N":
                    player_hp -= 10
                    print("\n ** You've activated a trap! You've lost 10 hp! **\n")
                elif difficulty == "H":
                    player_hp -= 20
                    print("\n ** You've activated a trap! You've lost 20 hp! **\n")
            elif player == door:
                door_found = True
                if not monster_alive:
                    print("\n ** You've escaped! Congratulations! **\n")
                    playing = False
                    break
                elif monster_alive:
                    print("\n ** You must kill the monster before you can escape! **\n")
        else:
            print("Invalid move.")
    if playing == False:
        game_end()

def game_end():
    play_again = input("Play again? (y/n) ")
    while play_again.lower() != 'y' and play_again.lower() != 'n':
        print("Invalid input.")
        play_again = input("Play again? (y/n) ")
    if play_again.lower() == 'y':
        game_loop()

clear_screen()
print("Welcome to the dungeon!")
input("Press return to start!")
clear_screen()
game_loop()
