# This list represents the Calories of the food carried by five Elves:

# The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
# The second Elf is carrying one food item with 4000 Calories.
# The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
# The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
# The fifth Elf is carrying one food item with 10000 Calories.
# In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

def process_elfcals(string):
    elflist = [eval(i) for i in string.split('\n')]
    sum_elflist = sum(elflist)
    return sum_elflist
    

with open("AoC_1.txt", "r") as f:
    fulltext = f.read().split('\n\n')
    sumlist = []
    for elements in fulltext:
        sumlist.append(process_elfcals(elements))

    max_elf_cals = max(sumlist)


index = 1
for num in sumlist:
    if num == max_elf_cals:
        print("The elf with {} cals is {}".format(max_elf_cals, index))
    
    else:
        index += 1

top_three = []

for i in range(3):
    top_three.append(max(sumlist))
    sumlist.remove(max(sumlist))

print("The sum of the most calories is {}".format(sum(top_three)))
