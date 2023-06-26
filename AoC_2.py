# Day 2
"""
Rules: 
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say 
will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and 
C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores 
for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).



Approach Strategy:
    1: Read in values from txt file and place left sided values (opponents play) into a list and the right side (my play) into another
    list

    2: Compare the values of the left and right through a loop in order to calculate total points

    3: Sum up total points
"""
x_points = 
y_points = 
z_points = 


with open('AoC_2.txt', 'r') as f:
    pair_list = f.read().split('\n')
    opponent_plays = []
    self_plays = []
    for pair in pair_list:
        opponent_plays.append(pair.split(' ')[0])
        self_plays.append(pair.split(' ')[-1])

