while True:
    print("\n=== Calculadora ===")
    print("1: soma")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")
    print("0: sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Encerrando a calculadora...")
        break

    elif opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")

        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")

        elif opcao == 3:
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")

        elif opcao == 4:
            if num2 == 0:
                print("Erro: divisão por zero não é permitida!")
            else:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")

    else:
        print("Opção inválida! Tente novamente.")
