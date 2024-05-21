Assignment 2 Game Playing 
README file

Due March 31, 2024

Student Name and Student ID: Faris Soepangat 1001374988
Programming Language Used: Python 3.12.0
This was not compiled on omega

imported libraries:
import sys
import math

How the code is structured: 

def cmp_turn_standard(piles):
- the program should use MinMax with Alpha Beta Pruning to determine the best move to make and perform the move

def cmp_turn_misere(piles):
- the program should use MinMax with Alpha Beta Pruning to determine the best move to make and perform the move

def human_turn(piles):
- the program should use a prompt to get the move from the human user and perform the move

def game_ends(piles):
- The function should alternate between these turns till the game ends (when the players run out of either red or blue marbles)

def calculate_pts(piles, version):
- calculate who won and their final score and display it to the user

def minmax(piles, maximizing_player, version):
- MinMax function with Alpha-Beta Pruning

How to run the code: 
1: install python3 if not already installed on your computer
2: go to the directory where the folder is located and open terminal
3: compile code by typing the following in the command line: 
   python3 red_blue_nim.py 10 10 standard human