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

    [12:04 PM] Jose Martinez De Leon

Hey! Yeah I took 6.0001, 6.009, 6.006, and 6.832 (Underactuated). I didn't have the chance to take any others, but I have a friend who's finishing up her masters in CS focusing on robotics, I can ask her what classes she would recommend if you'd like. 

[12:05 PM] Jose Martinez De Leon

Yeah underactuated is sick, Russ' lectures are also really good and on YouTube, there's another one of his classes that I think is really good too https://manipulation.csail.mit.edu/

 like 1

https://www.appliedintuition.com/
https://www.figure.ai/  humanoid robotics
Robotic Manipulation
"""

win_points = 6
draw_points = 3
loss_points = 0
x_points = 1 # rock, A
y_points = 2 # paper, B
z_points = 3 # scissors, C


with open('AoC_2.txt', 'r') as f:
    print(f.read())
    pair_list = f.read().split('\n')
    print(pair_list)
    # opponent_plays = []
    # self_plays = []
    # for pair in pair_list:
    #     opponent_plays.append(pair.split(' ')[0])
    #     self_plays.append(pair.split(' ')[-1])
    # plays = list(zip(opponent_plays, self_plays))



# read and parse all data first

# score = 0
# i = 0
# print(plays)
# print(plays)

# for matches in range(len(plays)):
#     if (plays[0] == 'A') == (plays[1] == 'X'):
#         score += draw_points + x_points
#         i += 1
        
#     elif (plays[0] == 'B') == (plays[1] == 'Y'):
#         score += draw_points + y_points
#         i += 1    
        
#     elif (plays[0] == 'C') == (plays[1] == 'Z'):
#         score += draw_points + z_points
#         i += 1 
        
#     elif plays[0] == 'A' and plays[1] == 'Y':
#         score += win_points + y_points
#         i += 1
       
#     elif plays[0] == 'A' and plays[1] == 'Z':
#         score += loss_points + z_points
#         i += 1
        
#     elif plays[0] == 'B' and plays[1] == 'X':
#         score += loss_points + x_points
#         i += 1
        
#     elif plays[0] == 'B' and plays[1] == 'Z':
#         score += win_points + z_points
#         i += 1
        
#     elif plays[0] == 'C' and plays[1] == 'X':
#         score += win_points + x_points
#         i +=1
       
#     elif plays[0] == 'C' and plays[1] == 'Y':
#         score += loss_points + y_points
#         i += 1
        
#     else:
#         print("not a valid combination")


print(score)
