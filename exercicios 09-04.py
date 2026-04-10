#exc 1
contador = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")
        contador += 1
print("\nTotal de números:", contador)

#exc 2
n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Número inválido! Encerrando programa.")
else:
    soma = 0
    expressao = ""
    for i in range(1, n+1):
        soma += i
        expressao += str(i)
        if i < n:
            expressao += " + "
    print(f"{expressao} = {soma}")

#exc 3 
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

for num in range(inicio, fim+1):
    print(f"\nTabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

#exc 4 
linhas = int(input("Digite a quantidade de linhas: "))

for i in range(1, linhas + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  
