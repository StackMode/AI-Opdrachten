def sorteren(lijst):
    for i in range(1,len(lijst)):
        key = lijst[i]
        pos = i - 1
        while pos >= 0 and lijst[pos] > key:
            lijst[pos+1] = lijst[pos]
            pos -= 1
        lijst[pos+1] = key
    return lijst

def sort(lijst):
    """Ik wist niet of ik de sorted() functie mog gebruiken."""
    return sorted(lijst)
lst = [1,2,2,3,4,5,5,6,6,6,6,1,2,7,7,6,8,9,9,9,4,4,7,0,0,2,4,3,5,5]
print(sorteren(lst))
print(sort(lst))