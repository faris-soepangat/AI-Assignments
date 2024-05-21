# Faris Soepangat 1001374988

import sys
import math

# Pick 2 red marble -> Pick 2 blue marble -> Pick 1 red marble -> Pick 1 blue marble
def cmp_turn_stan(piles):
    if piles["red"] >= 2:
        return "red", 2
    elif piles["blue"] >= 2:
        return "blue", 2
    elif piles["red"] >= 1:
        return "red", 1
    elif piles["blue"] >= 1:
        return "blue", 1

# Pick 1 blue marble -> Pick 1 red marble -> Pick 2 blue marble -> Pick 2 red marble
def cmp_turn_mise(piles):
    if piles["blue"] >= 1:
        return "blue", 1
    elif piles["red"] >= 1:
        return "red", 1
    elif piles["blue"] >= 2:
        return "blue", 2
    elif piles["red"] >= 2:
        return "red", 2

# Uses a prompt to get the move from the human user and perform the move
def human_turn(piles):
    while True:
        pile = input("select red/blue pile: ").lower()
        if pile not in piles.keys():
            print("try again...")
            continue

        num_marbles = int(input("select 1 or 2 marbles to remove: "))
        if num_marbles not in [1, 2] or piles[pile] < num_marbles:
            print("try again...")
            continue

        return pile, num_marbles

# Ends game if pile is 0
def game_ends(piles):
    return any(pile == 0 for pile in piles.values())

# Calculates the total points
def calculate_pts(piles, version):
    if version == "standard":
        return sum(piles.values()) * 2 + sum(piles.values()) * 3
    else:
        return 0

# MinMax function with Alpha-Beta Pruning
def minmax(piles, maximizing_player, version):
    if game_ends(piles):
        return calculate_pts(piles, version)

    if maximizing_player:
        max_eval = -math.inf
        for pile in ["red", "blue"]:
            for num_marbles in range(1, min(piles[pile], 3)):
                new_piles = piles.copy()
                new_piles[pile] -= num_marbles
                eval = minmax(new_piles, False, version)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for pile in ["red", "blue"]:
            for num_marbles in range(1, min(piles[pile], 3)):
                new_piles = piles.copy()
                new_piles[pile] -= num_marbles
                eval = minmax(new_piles, True, version)
                min_eval = min(min_eval, eval)
        return min_eval

# Main Code starts here
    
# Check if correct number of command line arguments are provided
if len(sys.argv) < 3:
    print("try again: red_blue_nim.py <num-red> <num-blue> [<version>] [<first-player>]")
    sys.exit(1)

# Parse command line arguments
num_red = int(sys.argv[1])
num_blue = int(sys.argv[2])
ver = "standard" if len(sys.argv) < 4 else sys.argv[3].lower()
first_player = "computer" if len(sys.argv) < 5 else sys.argv[4].lower()

# Initialize game state
piles = {"red": num_red, "blue": num_blue}
pts = {"computer": 0, "human": 0}

# Game loop
curr_player = first_player
while not game_ends(piles):
    print("\ncurrent piles:", piles, "\n")

    if curr_player == "computer":
        if ver == "standard":
            best_eval = -math.inf
            best_move = None
            for pile in ["red", "blue"]:
                for num_marbles in range(1, min(piles[pile], 3)):
                    new_piles = piles.copy()
                    new_piles[pile] -= num_marbles
                    eval = minmax(new_piles, False, ver)
                    if eval > best_eval:
                        best_eval = eval
                        best_move = (pile, num_marbles)
            pile, num_marbles = best_move
        else:
            best_eval = math.inf
            best_move = None
            for pile in ["red", "blue"]:
                for num_marbles in range(1, min(piles[pile], 3)):
                    new_piles = piles.copy()
                    new_piles[pile] -= num_marbles
                    eval = minmax(new_piles, True, ver)
                    if eval < best_eval:
                        best_eval = eval
                        best_move = (pile, num_marbles)
            pile, num_marbles = best_move

        piles[pile] -= num_marbles
        print("the computer selects {} {}(s)".format(num_marbles, pile))

        if game_ends(piles):
            pts["human"] = calculate_pts(piles, ver)
            print("the computer wins {} points.".format(pts["human"]))
            break
    else:
        pile, num_marbles = human_turn(piles)
        piles[pile] -= num_marbles

        if game_ends(piles):
            pts["computer"] = calculate_pts(piles, ver)
            print("you win {} points!".format(pts["computer"]))
            break
    curr_player = "computer" if curr_player == "human" else "human"