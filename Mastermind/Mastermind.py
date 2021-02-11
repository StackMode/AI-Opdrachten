"""

..:: Code Review ::..

Ik heb mijn voorgestelde aanpassingen bij de betreffende code gezet met TODO's;
uiteraard rest jou de keuze hoeveel je hiermee wilt doen. Hier even centraal een paar opmerkingen.
Onderzochte aspecten:

1) Functionele decompositie

Ik vind het een mooi gegeven dat je zo veel mogelijk parameters meegeeft (bijv. de kleurenlijst die consistent wordt
doorgegeven); dat is een goed beginsel, want het maakt je code een stuk makkelijker aan te passen als er inderdaad meer
kleuren bij komen. Wel zou ik de kleurenlijst ook in een functie meegeven als een default parameter, i.p.v een global.
Verder is de onderverdeling tot dusver netjes; wel wordt dat met toekomstige algoritmen des te lastiger.

2) Onderverdeling in modules

Er is nog geen onderverdeling gemaakt in modules; op het moment loopt alle functionaliteit dus door elkaar. Voor
de reeds geimplementeerde functies is dat niet al te erg; op het moment dat je de algoritmes gaat implementeren, zou ik
die in een andere module zetten en gescheiden houden van deze functies.

3) Commentaar

In het algemeen heb je commentaar in je functies staan dat beknopt beschrijft wat de functies doen; wel zou ik je
aanraden om overal kort bij op te nemen hoe de functies dat doel bereiken. Neem bijvoorbeeld de functie playerinput();
hier zou ik bij zetten
    '''De speler geeft hier zijn kleurencombinatie in, door de kleuren een voor een via de console in te voeren.'''
Wat, maar ook hoe. Zeker bij lastigere functies is dat handig!

4) Naamgeving variabelen

De naamgeving van je variabelen is qua formaat prima, en goed consistent Nederlands.

5) Werking van de code

Ik loop tegen een error aan bij het invoeren van de combinatie; ik voerde het woord "geel" an sich in, om te testen wat
er zou gebeuren, en vervolgens treedt er een error op (not enough values to unpack). Ik zie dat je je best doet om
input te valideren, maar nog niet alle gevallen worden afgevangen; ik zou aanraden bijv. een try-except constructie
binnen die loop te zetten!

"""

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
