while True:
    try:
        num = int(input("Digite um número inteiro:"))
        soma = 0
        i = 1

        while i >= num:
            soma += i
            i += 1
        print(f"A soma dos {num} primeiros números interios é {soma}.")
        break
    except ValueError:
        print("Seu número não faz parte do conjunto dos inteiros.")