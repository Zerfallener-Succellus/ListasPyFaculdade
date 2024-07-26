idade = float(input("Digite a idade do nadador : "))

classificacao = "bebe"

if idade >= 5 and idade <= 7:
    classificacao = "infantil A"

if idade >= 8 and idade <= 10:
    classificacao = "infantil B"

if idade >= 11 and idade <= 13:
    classificacao = "juvenil A"

if idade >= 14 and idade <= 17:
    classificacao = "juvenil B"

if idade >= 18:
    classificacao = "adulto"

print("A classificacao do nadador é: "+ classificacao)
