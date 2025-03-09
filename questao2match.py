for i in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média final do aluno: "))
    
    conceito_nota = (
        0 if media < 5 else
        5 if media < 7 else
        7 if media < 9 else
        9
    )
    
    match conceito_nota:
        case 0:
            conceito = "D"
        case 5:
            conceito = "C"
        case 7:
            conceito = "B"
        case 9:
            conceito = "A"
            
    print(f"Aluno: {nome} - Média: {media:.2f} Conceito: {conceito}")
    