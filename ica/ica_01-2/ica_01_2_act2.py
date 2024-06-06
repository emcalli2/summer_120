import random
def random_rolls(s):
    random.seed(s)
    sums = 0
    # if randint == 1: return
    randint = 0
    while randint != 1:
        randint = random.randint(1,20)
        if int(randint) == 1:
            print("Rolled a 1, the loop will now terminate.")
            return sums
        elif int(randint) == 20:
            print("Rolled a " + str(randint) + ", I will add double the value to the running sum.")
            sums += (2 * randint)
            print("   Sum so far: " + str(sums))
        else:
            print("Rolled a " + str(randint) + ", I will add the value to the running sum.")
            sums += randint
            print("   Sum so far: " + str(sums))
    