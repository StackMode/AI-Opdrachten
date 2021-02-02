def palindroom(woord):
    flipwoord = woord[::-1]
    return woord == flipwoord

print(palindroom('racecar'))