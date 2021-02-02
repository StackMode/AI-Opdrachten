def cyclisch(ch,n):
    ch = list(ch)
    ch = ch[n:] + ch[:n]
    return ''.join(ch)


print(cyclisch('1011000', 3))