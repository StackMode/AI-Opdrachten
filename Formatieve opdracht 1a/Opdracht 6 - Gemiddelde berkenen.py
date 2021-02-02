def gemiddelde(lijst):
    som = 0
    for x in lijst:
        som += x
    return som//len(lijst)

def gemiddelde_lijst(lijsten):
    gemiddeld_lijst = []
    for lst in lijsten:
        som = 0
        for i in lst:
            som += i
        gemiddeld_lijst.append(som//len(lst))
    return gemiddeld_lijst

lijst= [1,2,2,3,4,5,5,6,6,6,6,1,2,7,7,6,8,9,9,9,4,4,7,0,0,2,4,3,5,5]
lijsten = [[1,2,6,0,8],[1,6,6,4,8],[1,2,6,7,3],[6,9,5,3,4],[8,8,5,4,2],[2,4,5,9,1],[3,6,7,1,9],
           [9,9,5,2,7],[7,4,5,1,3],[7,9,4,6,8],[5,1,2,8,9],[0,1,6,9,3],[1,5,0,3,7],[1,9,0,0,4]]
print(gemiddelde(lijst))
print(gemiddelde_lijst(lijsten))