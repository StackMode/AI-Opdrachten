import random
import itertools


def playerinput(kleuren):
    """De speler geeft hier zijn kleuren combinatie."""
    vierhidden = []
    i = 0
    while i < 4:
        kleur1, kleur2, kleur3, kleur4 = input('Geef jouw combinatie: ').split()
        kleurcombinatie = kleur1, kleur2, kleur3, kleur4
        for kleur in kleurcombinatie:
            if kleur not in kleuren:
                print('Kies een van de kleuren uit de lijst.')
            else:
                vierhidden.append(kleur)
                i += 1
    return vierhidden


def computerinput(kleuren):
    """"De computer genereerd hier een random kleuren combinatie"""
    vierhidden = list()
    for pos in range(0, 4):
        vierhidden.append(random.choice(kleuren))
    return vierhidden


def playerzetten(vierhidden):
    """De speler heeft 10 kansen om te raden wat de kleuren combinatie is."""
    zet = 1
    while zet <= 10:
        combi = playerinput(kleurenlijst)
        print('Zet ' + str(zet) + ' is: ' + str(combi))
        zet += 1
        validatie = validatecombination(vierhidden, combi)
        if validatie == 1:
            if zet-1 == 1:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zet!'
            else:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zetten!'
        else:
            print('Feedback: ' + str(validatie))
    if zet > 10:
        return 'je hebt geen zetten meer.\n De geheime combinatie was ' + str(vierhidden)


def computerzetten(vierhidden):
    """De computer raad hier binnen 10 kansen de door de speler gemaakte kleuren combinatie."""
    # Ik ben nog bezig met het algoritme
    nieuwecombinaties = []
    zet = 1
    totalecombinaties = [list(mogelijkheid) for mogelijkheid in itertools.product(kleurenlijst, repeat=4)]
    print(len(totalecombinaties))
    while zet <= 10:
        for kleur in range(len(kleurenlijst)):
            combination = [kleurenlijst[kleur]] * 4
            valid = validatecombination(vierhidden, combination)
            if valid == 1:
                return 'De computer heeft gewonnen in ' + str(zet - 1) + ' zetten!'
            else:
                for mog in totalecombinaties:
                    x = validatecombination(vierhidden, mog)
                    if x == valid:
                        nieuwecombinaties.append(mog)

        zet += 1
    print(len(nieuwecombinaties))
    if zet > 10:
        return 'Je hebt gewonnen van de computer'
    return


def validatecombination(vierhidden,combinatie):
    """ Het feedback geven op de gekozen combinatie.
        Hulp bron: https://bnbasilio.medium.com/mastermind-a-how-to-in-python-7b80ca9809ab"""
    feedback = []
    code = vierhidden.copy()
    combi = combinatie.copy()
    for pos in range(len(code)):
        if combi[pos] == code[pos]:
            code[pos] = '-'
            combi[pos] = ''
            feedback.append('zwart')
    for pos in range(len(code)):
        if combi[pos] in code:
            for i in range(len(code)):
                if code[i] == combi[pos]:
                    code[i] = '-'
                    combi[pos] = ''
            feedback.append('wit')
    if len(feedback) == 4 and all(i == 'zwart' for i in feedback):
        return 1
    else:
        return feedback


def main():
    """De speler kiest hoe hij mastermind wilt spelen"""

    print('Kies hier hoe u mastermind wil spelen: \n1.Ik wil raden.\n2.De computer laten raden.')
    keuze = int(input('Ik kies voor nummer: '))
    if keuze == 1:
        print('We spelen met deze kleuren: ' + str(kleurenlijst))
        vierhiddencomputer = computerinput(kleurenlijst)
        return playerzetten(vierhiddencomputer)
    elif keuze == 2:
        print('We spelen met deze kleuren: ' + str(kleurenlijst))
        vierhiddenplayer = playerinput(kleurenlijst)
        return computerzetten(vierhiddenplayer)
    else:
        return 'Kies voor nummer 1 of 2.'


kleurenlijst = ['blauw','rood', 'geel', 'groen', 'wit', 'zwart']
print(main())
