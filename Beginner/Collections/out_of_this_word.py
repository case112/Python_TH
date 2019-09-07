import random
import os

WORDS = (
    "treehouse",
    "python",
    "learner")


def prompt_for_words(challenge):
    guesses = set()

    print("What words can you find in the word '{}'".format(challenge))
    print("(Enter Q to Quit)")

    while True:
        guess = input("{} words >. ".format(len(guesses)))

        # Don't allow words of less than 2 chars
        if len(guess) < 2:
            if guess.upper() == "Q":
                break
            else:
                print ("Guesses must be at least two letters - try again.")
                continue

        if check_valid_word(guess):
            guesses.add(guess.lower())
        else:
            print("Sorry, '{}' is not in '{}' - try agian.".
                  format(guess, challenge))
            continue
    return guesses


def check_valid_word(word):
        """Check whether the chars exist in the word."""
        guess_chars = []
        for char in word:
            guess_chars.append(char.lower())

        # 1. make a copy of the challenge_chars list
        check_list = challenge_chars.copy()
        # 2. Loop through the copied list and remove any matches
        for letter in guess_chars:
            if letter not in check_list:
                return False
            else:
                check_list.remove(letter)
        return True


def output_results(results):
    for word in results:
        print("* " + word)


def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")


# The Game
clear_screen()
challenge_chars = []
challenge_word = random.choice(WORDS)
# Create a list of chars in the challenge word
for char in challenge_word:
    challenge_chars.append(char)

player1_name = input("\nPlayer 1, what is your name? ")
player1_words = prompt_for_words(challenge_word)
player2_name = input("\nPlayer 2, what is your name? ")
player2_words = prompt_for_words(challenge_word)


# The results
clear_screen()
print("Results for " + player1_name + ":")
player1_unique = player1_words - player2_words
print("{} guesses, {} unique".format(len(player1_words), len(player1_unique)))
output_results(player1_unique)
print("-" * 10 + "\n")
print("Results for " + player2_name + ":")
player2_unique = player2_words - player1_words
print("{} guesses, {} unique".format(len(player2_words), len(player2_unique)))
output_results(player2_unique)
print("-" * 10 + "\n")
print("Shared guesses:")
shared_words = player1_words & player2_words
output_results(shared_words)
print("-" * 10 + "\n")
