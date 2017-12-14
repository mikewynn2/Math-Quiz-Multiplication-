import random

digit1 = random.randint(1,12)

digit2 = int(input("What times tables are we working on today?(TYPE 0 FOR RANDOM NUMBER)"))
if digit2 == 0:
    digit2 = random.randint(1,12)
        
pts = 0

turns = 0

while pts < 30:
    
    print(digit1)
    print("X")
    print(digit2)
    ans = int(input("=?"))

    if ans == digit1 * digit2:
        print("correct")
        pts = pts + 1
        digit1 = random.randint(1,12)
        turns = turns + 1

    elif ans != digit1 * digit2:
        print("WRONG")
        
        digit1 = random.randint(1,12)
        turns = turns + 1


if pts == 30:
    print("CONGRATS!!! You Passed!!!")
    print("It took you " + str(turns) + " turns to get to 5 points!")

