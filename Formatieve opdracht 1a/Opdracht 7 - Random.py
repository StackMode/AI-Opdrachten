import random
def willekeurig(inp,n):
    while inp != n:
        inp = int(input('Probeer nog eens: '))
    if inp == n:
        return 'Je hebt gewonnen!'


print(willekeurig(int(input('Gok een getal tussen de 0 en de 20: ')),random.randint(0,20)))