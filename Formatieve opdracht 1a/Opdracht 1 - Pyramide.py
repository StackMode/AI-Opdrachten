aantal = int(input('Hoe groot? '))

def for_loop():
    for x in range(aantal + 1):
        print('*' * x)
    for x in range(aantal-1,0,-1):
        print('*' * x)


def while_loop():
    rij = 1
    while rij < aantal:
        print('*' * rij)
        rij += 1
    while rij > 0:
        print('*' * rij)
        rij -= 1

def inverted():
    for x in range(aantal + 1):
        print(' '*(aantal - x) + '*' * x)
    for x in range(aantal-1,0,-1):
        print(' '*(aantal - x) + '*' * x)


for_loop()
while_loop()
inverted()


