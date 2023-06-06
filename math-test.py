import random
import time

digit1 = random.randint(1, 12)

digit2 = int(input("What times tables are we working on today?(TYPE 0 FOR RANDOM NUMBER) "))
if digit2 == 0:
    digit2 = random.randint(1, 12)

pts = 0
turns = 0
start_time = time.time()
while pts < 10:

    print("%d X %d =? " % (digit1, digit2))
    ans = int(input("? "))

    if ans == digit1 * digit2:
        print("correct")
        pts = pts + 1
        digit1 = random.randint(1, 12)
        turns = turns + 1

    elif ans != digit1 * digit2:
        print("WRONG")
        correction = digit1 * digit2
        print(" The correct answer is " + str(correction))

        digit1 = random.randint(1, 12)
        turns = turns + 1


if pts == 10:
    timer = time.time() - start_time
    print("CONGRATS!!! You Passed!!!")
    print("It took you " + str(turns) + " turns to get to %d points!" % (pts))
    print("It took %d seconds to get to %s points!" % (timer, pts))
