while True:
    nota = float(input("Digite a nota do aluno:"))      
    if nota >= 0 and nota <= 10:
        print(f"A nota do aluno é {nota}.") 
        break
    else:
        print("Nota não válida.")