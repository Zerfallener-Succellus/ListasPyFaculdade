def soma(a):
    if a == 0:
        return 0
    else:
        return a +soma(a-1)


n = 5

somala = soma(n)

print(somala)