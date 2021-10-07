y = 1
x = 1
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



while x != 3 or y != 1:
    
    if x == 1 and y == 1:
        print("You can travel: (N)orth.")
        allowed=["N"]

    elif x == 1 and y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        allowed=["N","E","S"]

    elif x == 1 and y == 3:
        print("You can travel: (E)ast or (S)outh.")
        allowed=["E","S"]

    elif x == 2 and y == 1:
        print("You can travel: (N)orth.")
        allowed=["N"]

    elif x == 2 and y == 2:
        print("You can travel: (S)outh or (W)est.")
        allowed=["W","S"]

    elif x == 2 and y == 3:
        print("You can travel: (E)ast or (W)est.")
        allowed=["E","W"]

    elif x == 3 and y == 2:
        print("You can travel: (N)orth or (S)outh.")
        allowed=["N","S"]

    elif x == 3 and y == 3:
        print("You can travel: (S)outh or (W)est.")
        allowed=["W","S"]

    direction = input("Direction: ")
    if direction.upper() in allowed:
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



print("Victory!")