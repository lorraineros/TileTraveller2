import random

def play():
    y = 1
    x = 1
    coin=0
    moves=0

    def up(y):
        y += 1
        return y
    def down(y):
        y -= 1
        return y
    def right(x):
        x += 1
        return x
    def left(x):
        x -= 1
        return x

    seed=int(input("Input seed: "))
    random.seed(seed)
    while x != 3 or y != 1:

        if x == 1 and y == 1:
            print("You can travel: (N)orth.")
            allowed=["N"]

        elif x == 1 and y == 2:
            while ask:
                answer = random.choice(["y", "n"])
                print(f"Pull a lever (y/n): {answer}")
                if answer.lower() == "y":
                    coin += 1
                    print(f"You received 1 coin, your total is now {coin}.")
                ask=False
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            allowed=["N","E","S"]

        elif x == 1 and y == 3:
            print("You can travel: (E)ast or (S)outh.")
            allowed=["E","S"]

        elif x == 2 and y == 1:
            print("You can travel: (N)orth.")
            allowed=["N"]

        elif x == 2 and y == 2:
            while ask:
                answer = random.choice(["y", "n"])
                print(f"Pull a lever (y/n): {answer}")
                if answer.lower() == "y":
                    coin += 1
                    print(f"You received 1 coin, your total is now {coin}.")
                ask = False
            print("You can travel: (S)outh or (W)est.")
            allowed=["W","S"]

        elif x == 2 and y == 3:
            while ask:
                answer = random.choice(["y", "n"])
                print(f"Pull a lever (y/n): {answer}")
                if answer.lower() == "y":
                    coin += 1
                    print(f"You received 1 coin, your total is now {coin}.")
                ask = False
            print("You can travel: (E)ast or (W)est.")
            allowed=["E","W"]

        elif x == 3 and y == 2:
            while ask:
                answer = random.choice(["y", "n"])
                print(f"Pull a lever (y/n): {answer}")
                if answer.lower() == "y":
                    coin += 1
                    print(f"You received 1 coin, your total is now {coin}.")
                ask = False
            print("You can travel: (N)orth or (S)outh.")
            allowed=["N","S"]

        elif x == 3 and y == 3:
            print("You can travel: (S)outh or (W)est.")
            allowed=["W","S"]

        direction = random.choice(["n", "e", "s", "w"])
        print(f"Direction: {direction}")
        if direction.upper() in allowed:
            ask = True
            moves +=1
            if direction.upper() == "N":
                y=up(y)
            elif direction.upper() == "S":
                y=down(y)
            elif direction.upper() == "E":
                x=right(x)
            elif direction.upper() == "W":
                x=left(x)
        else:
            print("Not a valid direction!")
            moves += 1
            ask=False
    print(f"Victory! Total coins {coin}. Moves {moves}.")

play()
ask=input("Play again (y/n): ")
while ask.lower() != "n":
    play()
    ask = input("Play again (y/n): ")