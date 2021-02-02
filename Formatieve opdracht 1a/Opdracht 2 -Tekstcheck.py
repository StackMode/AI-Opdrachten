def tekstcheck(string1,string2):
    index = 0
    for i,j in zip(string1,string2):
        if i == j:
            index += 1
        else:
            return 'Het eerste verschil zit op index: ' + str(index)


print(tekstcheck(string1=str(input('Geef een string: ')),
                 string2=str(input('Geef een string: '))))
