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
    """De speler geeft hier zijn kleuren combinatie, door de kleuren uit de kleurenlijst in te voeren in de console."""
    vierhidden = []
    i = 0
    try:
        while i < 4:
            kleur1, kleur2, kleur3, kleur4 = input('Geef jouw combinatie: ').split()
            kleurcombinatie = kleur1, kleur2, kleur3, kleur4
            for kleur in kleurcombinatie:
                if kleur not in kleuren:
                    print('Kies een van de kleuren uit de lijst.')
                else:
                    vierhidden.append(kleur)
                    i += 1
    except:
        print('Geef 4 kleuren uit de lijst in 1 regel, met spatie en kleine letters')
        return playerinput(kleurenlijst)
    return vierhidden


def computerinput(kleuren):
    """"De computer genereerd hier een random kleuren combinatie, dit doet hij door de module random.choice()."""
    vierhidden = list()
    for pos in range(0, 4):
        vierhidden.append(random.choice(kleuren))
    return vierhidden


def playerzetten(vierhidden):
    """ De speler heeft 10 kansen om te raden wat de kleuren combinatie is.
        De speler voert zijn kleur combinatie in in de console, deze kleur combinatie ziet er als volgt uit:
        XXXX XXXX XXXX XXXX
    """
    zet = 1
    while zet <= 10:
        combi = playerinput(kleurenlijst)
        print('Zet ' + str(zet) + ' is: ' + str(combi))
        zet += 1
        validatie = validatecombination(vierhidden, combi)
        if validatie[0] == 4:
            if zet - 1 == 1:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zet!'
            else:
                return 'Je hebt gewonnen in ' + str(zet - 1) + ' zetten!'
        else:
            print('Feedback: ' + str(validatie))
    if zet > 10:
        return 'je hebt geen zetten meer.\n De geheime combinatie was ' + str(vierhidden)


def verminderen(mogelijkecombinaties, combinatie, feedback):
    """ In deze functie worden de aantal mogelijkheden die beschikbaar zijn verminderd.
        Dit doet hij door naar alle mogelijkheden die er zijn te kijken welke hetzelfde feedback krijgt als
        de feedback die gekregen is op de eerste gok.
    """
    nieuwecombinaties = []
    for mogelijkheid in mogelijkecombinaties:
        if validatecombination(combinatie, mogelijkheid) == feedback:
            nieuwecombinaties.append(mogelijkheid)
    totalecombinaties = nieuwecombinaties
    return totalecombinaties


def simpel_algoritme(vierhidden, totalecombinatie, combinatie):
    """ In deze functie is een simpel algoritme te zien. Dit simpel algoritme werkt door
        vanuit de eerste gok (die meegegeven is in de functie), de verminder functie oproept.
        Wat de verminder functie returned wordt de nieuwe totale combinatie lijst.
        Uit deze lijst wordt een random combinatie gekozen en met deze combinatie worden de stappen herhaald.
    """
    zet = 1
    while zet <= 10:
        valid = validatecombination(vierhidden, combinatie)
        if valid[0] == 4:
            return 'De computer heeft de code geraden in ' + str(zet) + ' zetten!'
        else:
            totalecombinatie = verminderen(totalecombinatie, combinatie, valid)
            combinatie = totalecombinatie[random.randint(0,len(totalecombinatie)-1)]
        zet += 1
    if zet > 10:
        return 'je hebt gewonnen van de computer.'


def heuristiek(vierhidden, totalecombinatie, combinatie):
    """ De computer raad hier binnen 100 kansen de door de speler gemaakte kleuren combinatie.
        Dit doet hij bijna op de zelfde manier als de simpel algoritme. Hij maakt alleen een andere lijst aan.
        Hierdoor is hij niet zo snel (het was ook een beetje een tijdspaniek functie).
    """
    zet = 1
    while zet <= 100:
        valid = validatecombination(vierhidden, combinatie)
        if valid[0] == 4:
            return 'De computer heeft jouw geheime code geraden ' + str(zet) + ' zetten!'
        else:
            mogelijke = verminderen(totalecombinatie, combinatie, valid)
            combinatie = mogelijke[random.randint(0, len(mogelijke) - 1)]
        zet += 1
    if zet > 100:
        return 'je hebt gewonnen van de computer.'


def bruteforce(vierhidden, totalecombinatie):
    """ Dit is de bruteforce functie, die loopt door de lijst van alle combinaties en zoekt de verstopte code.
        De opdracht liep niet zoals gehoopt en toen kwam dit eruit.
    """
    for x in range(0, 1296):
        code = totalecombinatie[x]
        if validatecombination(vierhidden, code)[0] == 4:
            return 'Gevonden na ' + str(x + 1) + ' zetten.'


def validatecombination(vierhidden, combinatie):
    """ Het feedback geven op de gekozen combinatie, door een kopie te maken van de geheime coden en de geraden combinatie.
        In deze kopieën past hij de inhoud en voor elke pin op de juiste plek voegt hij een 1 toe aan de feedback[0],
        voor wit doet hij dit bij feedback[1].
        Hulp bron: https://bnbasilio.medium.com/mastermind-a-how-to-in-python-7b80ca9809ab"""
    feedback = [0, 0]
    code = vierhidden.copy()
    combi = combinatie.copy()
    for pos in range(len(code)):
        if combi[pos] == code[pos]:
            code[pos] = '-'
            combi[pos] = ''
            feedback[0] += 1
    for pos in range(len(code)):
        if combi[pos] in code:
            for i in range(len(code)):
                if code[i] == combi[pos]:
                    code[i] = '-'
                    combi[pos] = ''
            feedback[1] += 1
    return feedback


def main():
    """ De speler kiest hoe hij mastermind wilt spelen, door nummer 1 of 2 in te voeren in de console.
        Als de speler iets anders invoert wordt hij gevraagt om nummer 1 of 2 in te voeren."""
    print('Kies hier hoe u mastermind wil spelen: \n1.Ik wil raden.\n2.De computer laten raden.')
    keuze = int(input('Ik kies voor nummer: '))
    try:
        if keuze == 1:
            print('We spelen met deze kleuren: ' + str(kleurenlijst))
            vierhiddencomputer = computerinput(kleurenlijst)
            return playerzetten(vierhiddencomputer)
        elif keuze == 2:
            print('We spelen met deze kleuren: ' + str(kleurenlijst))
            vierhiddenplayer = playerinput(kleurenlijst)
            return simpel_algoritme(vierhiddenplayer, totalecombinaties, combinatie)
        else:
            print('kies voor nummer 1 of 2 \n')
    except:
        print('kies voor nummer 1 of 2 \n')
        return main()


kleurenlijst = ['blauw', 'rood', 'geel', 'groen', 'wit', 'zwart']
combinatie = [kleurenlijst[0], kleurenlijst[0], kleurenlijst[1], kleurenlijst[1]]
totalecombinaties = [list(mogelijkheid) for mogelijkheid in itertools.product(kleurenlijst, repeat=4)]
print(main())
