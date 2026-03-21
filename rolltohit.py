#This simulates rolling to hit in Warhammer 40,000
#Prompt the user how many dice are being rolled, and what the hit target is
#Roll the correct number of dice, then display the results
#This is a guided practice. Either follow with the video or your instructor will
#go over this in class.

num_dice = int(input("How many dice? "))
hit_target = int(input("What do you need to hit? "))
hits = 0
count = 0

while count < num_dice:
    roll = random.randint(1, 6)
    print("You rolled:", roll)
    if roll >= hit_target:
        print("Hit!")
        hits = hits + 1
    else:
        print("Miss!")
    count = count + 1
print("Total hits:", hits)