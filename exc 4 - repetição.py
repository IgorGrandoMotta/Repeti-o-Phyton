pares = 0
impares = 0
contador = 0

print("Esse é um programa que conta a quantia de pares e impares em 10 números digitados!")
while contador < 10:
    num = int(input(f"Digite o {contador+1}º número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
