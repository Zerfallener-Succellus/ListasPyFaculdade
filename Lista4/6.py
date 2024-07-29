n = int(input("digite um número inteiro positivo N: "))

numero = 1

for linha in range (1,n+1):
    for _ in range(linha):
        print(numero,end=' ')
        numero+=1

    print()