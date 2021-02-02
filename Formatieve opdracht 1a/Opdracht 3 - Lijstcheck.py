def count(lijst, n):
    teller = 0
    for x in lijst:
        if x == n:
            teller += 1
    return teller

def counter(lijst, n):
    """Ik wist niet of ik .count() mocht gebruiken, vandaar allebei."""
    return lijst.count(n)

def verschil(lijst):
    verschil_lijst = []
    for i in range(1, len(lijst)):
        verschil_lijst.append(lijst[i] - lijst[i-1])
    return max(verschil_lijst)

def binairtellen(lijst):
    tel_nul = count(lijst, 0)
    tel_een = count(lijst, 1)
    if tel_nul > tel_een:
        return 'Er zijn meer nullen dan enen'
    elif tel_nul> 12:
        return 'Er zitten teveel nullen in de lijst.'
    else:
        return True
    
lijst= [1,2,2,3,4,5,5,6,6,6,6,1,2,7,7,6,8,9,9,9,4,4,7,0,0,2,4,3,5,5]
print(count(lijst, n=int(input('Geef een getal onder de 10: '))))
print(counter(lijst, n=int(input('Geef een getal onder de 10: '))))
print(verschil(lijst))
print(binairtellen(lijst=[0,0,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1]))