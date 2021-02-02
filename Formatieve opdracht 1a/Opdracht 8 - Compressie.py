file = open('Compressedbestand.txt','w+')
with open('Tekstbestand.txt','r') as myfile:
    for line in myfile:
        lijst = list(line.strip())
        if lijst:
            file.write("%s\n" % ''.join(lijst))
file.close()


