def caesar(txt,rot):
    caesarcode = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for char in txt:
        if char in uppercase:
            index = uppercase.index(char)
            cijfer = (index + rot) % 26
            nieuw = uppercase[cijfer]
            caesarcode.append(nieuw)
        elif char in lowercase:
            index = lowercase.index(char)
            cijfer = (index + rot) % 26
            nieuw = lowercase[cijfer]
            caesarcode.append(nieuw)
        else:
            caesarcode.append(char)
    caesarcode = ''.join(caesarcode)
    return 'Ceasarcode: ' + caesarcode


print(caesar(str(input('Geef een tekst: ')),int(input('Geef een rotatie: '))))