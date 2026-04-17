print("Modos de jogo:")
print("(1) humano x humano")
print("(2) humano x máquina")
print("(3) máquina x máquina")
print("(4) Sair")
pj1 = 0
pj2 = 0
pmqn = 0
pmqn1 = 0
pmqn2 = 0
empatesjj = 0
empatesjm = 0
empatesmm = 0

modojogo = int(input("selecione modo de jogo: "))

while True:
     if modojogo == 1:
        print("REGRAS:")
        print("Para pedra, digite 1. ")
        print("Para papel, digite 2. ")
        print("Para tesoura, digite 3. ")
        jogador1 = int(input("Jogador 1, digite a sua escolha: "))
        print(" \n " * 35)
        jogador2 = int(input("Jogador 2, digite a sua escolha: "))
        print(" \n " * 35)
        
        if jogador1 == 2 and jogador2 == 1 or jogador1 == 1 and jogador2 == 3 or jogador1 == 3 and jogador2 == 2:
            #print(f"Jogador 1 jogou ()")
            print("Parabéns jogador 1, você venceu!")
            pj1 += 1

        elif jogador1 == 1 and jogador2 == 2 or jogador1 == 2 and jogador2 == 3 or jogador1 == 3 and jogador2 == 1:
            print("Parabéns jogador 2, você venceu!")
            pj2 += 1

        elif jogador1 == 1 and jogador2 == 1 or jogador1 == 2 and jogador2 == 2 or jogador1 == 3 and jogador2 == 3 :
            print("A partida deu empate.")
            empatesjj += 1
           
            print("(1) Sair" "/n" "(2) Continuar")
            alt = int(input("Digite a alternativa: "))
            if alt == 1:
             print(f"Pontuação jogador 1: ", (pj1),  "/n", "Pontuação jogador 2: ", (pj2), "/n", "Empates: ", (empatesjj))
             break
        else:
            print("Algum jogador digitou uma alternativa errada, por favor repita o processo.")
    #####################################################################################################################
     if modojogo == 2:
        print("REGRAS:")
        print("Para pedra, digite 1. ")
        print("Para papel, digite 2. ")
        print("Para tesoura, digite 3. ")
        jogador1 = int(input("Jogador 1, digite a sua escolha: "))
        escolhamqn = random.randit(1,3)
        
        if jogador1 == 2 and escolhamqn == 1 or jogador1 == 1 and escolhamqn == 3 or jogador1 == 3 and escolhamqn == 2:
                #print(f"Jogador 1 jogou ()")
                print("Parabéns, você venceu!")
                pj1 += 1

        elif jogador1 == 1 and escolhamqn == 2 or jogador1 == 2 and escolhamqn == 3 or jogador1 == 3 and escolhamqn == 1:
                print("Não foi desta vez :/, tente novamente.")
                pmqn += 1

        elif jogador1 == 1 and escolhamqn == 1 or jogador1 == 2 and escolhamqn == 2 or jogador1 == 3 and escolhamqn == 3 :
                print("A partida deu empate.")
                empatesjm += 1
        else:
            print("Você digitou uma alternativa errada, por favor repita o processo.")
     #######################################################################################################################################
     if modojogo == 3:
        escolhamqn1 = random.randit(1,3)
        escolhamqn2 = random.randit(1,3)
    
        if escolhamqn1 == 2 and escolhamqn2 == 1 or escolhamqn1 == 1 and escolhamqn2 == 3 or escolhamqn1 == 3 and escolhamqn2 == 2:
            #print(f"Jogador 1 jogou ()")
            print("A maquina 1 venceu!")
            pj1 += 1

        elif escolhamqn1 == 1 and escolhamqn2 == 2 or escolhamqn1 == 2 and escolhamqn2 == 3 or escolhamqn1 == 3 and escolhamqn2 == 1:
            print("A maquina 2 venceu!")
            pmqn += 1

        elif escolhamqn1 == 1 and escolhamqn2 == 1 or escolhamqn1 == 2 and escolhamqn2 == 2 or escolhamqn1 == 3 and escolhamqn2 == 3 :
            print("A partida deu empate.")
            empatesmm += 1 


    