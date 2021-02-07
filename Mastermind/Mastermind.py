import random


def playerinput(kleuren):
    """De speler geeft hier zijn kleuren combinatie."""
    vierhidden = list()
    i = 0
    print('We spelen met deze kleuren: ' + str(kleuren))
    while i < 4:
        kleur1, kleur2, kleur3, kleur4 = input('Geef jouw verborgen combinatie: ').split()
        kleurcombinatie = kleur1, kleur2, kleur3, kleur4
        for kleur in kleurcombinatie:
            if kleur not in kleuren:
                print('Kies een van de kleuren uit de lijst.')
            else:
                vierhidden.append(kleurcombinatie)
                i += 1
    return vierhidden


def computerinput(kleuren):
    """"De computer genereerd hier een random kleuren combinatie"""
    vierhidden = list()
    for pos in range(0, 4):
        vierhidden.append(random.choice(kleuren))
    return vierhidden


def spelinput(kleuren):
    """De speler raadt een kleuren combinatie."""
    i = 0
    combi = []
    while i < 4:
        kleur1, kleur2, kleur3, kleur4 = input('Geef jouw combinatie: ').split()
        kleurcombinatie = kleur1, kleur2, kleur3, kleur4
        for kleur in kleurcombinatie:
            if kleur not in kleuren:
                print('Kies een van de kleuren uit de lijst.')
            else:
                combi.append(kleur)
                i += 1
    return combi


def playerzetten(vierhidden):
    """De speler heeft 10 kansen om te raden wat de kleuren combinatie is."""
    zet = 1
    while zet <= 10:
        combi = spelinput(kleurenlijst)
        print('Zet ' + str(zet) + ' is: ' + str(combi))
        zet += 1
        validatie = validatecombination(vierhidden,combi)
        if validatie == 1:
            if zet-1 == 1:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zet!'
            else:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zetten!'
        else:
            print('Feedback: ' + str(validatie))
    if zet > 10:
        return 'je hebt geen zetten meer.'


def computerzetten(vierhidden):
    """De computer raad hier binnen 10 kansen de door de speler gemaakte kleuren combinatie."""

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
        vierhiddencomputer = computerinput(kleurenlijst)
        return playerzetten(vierhiddencomputer)
    elif keuze == 2:
        vierhiddenplayer = playerinput(kleurenlijst)
        return computerzetten(vierhiddenplayer)
    else:
        return 'Kies voor nummer 1 of 2.'


kleurenlijst = ['blauw','rood', 'geel', 'groen', 'wit', 'zwart']
print(main())
