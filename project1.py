# Dice Game
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
#value = roll()
#print(value)

while True:
    players = input("Enter the Numbers of Players (2 - 5): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Must be Between 2 - 5 Players!!")
    else:
        print("Invalid, Try Again!!!")
#print(players)

max_score = 70
player_score = [0 for i in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer Number", player_idx + 1, "turn has just started!")
        print("Your score is:", player_score[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y)?: ")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("You rolled a 1!, Your turn is done...")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            print("Your Score is: ", current_score)
        player_score[player_idx] += current_score
        print("Your Total Score is: ", player_score[player_idx])
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number", winning_idx + 1, "is the winner with the score of", max_score)