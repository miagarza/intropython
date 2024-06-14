import random
rand_num = random.randint(1,6)
print(rand_num)

if (rand_num <= 2):
    print("You will lose money today")
if (rand_num>=2) and (rand_num<=4):
    print ("You will find a $20 bill on the ground")
if (rand_num>=4) and (rand_num<=6):
    print("You will win a free phone")


