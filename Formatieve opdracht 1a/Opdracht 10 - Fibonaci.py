def fibonaci(n, v0=0, v1=1):
    return fibonaci(n-1, v1, v0 + v1) if n > 1 else (v0, v1)[n]

print(fibonaci(8))