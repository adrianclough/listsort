import readchar
from random import randint

random_pair = (randint(0,100), randint(0,100))

print(random_pair)

ordered = random_pair[0] < random_pair[1]

while True:
    key = readchar.readkey()
    if key == readchar.key.UP or key == readchar.key.DOWN:
        if (key == readchar.key.UP) == ordered:
            print("Well done!")
        else:
            print("Better luck next time!")
        break
    else:
        print("Invalid key. Press UP or DOWN.")