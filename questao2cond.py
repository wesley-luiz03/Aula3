for i in range (5):

    nome_aluno = (input("Digite o nome do aluno: "))
    media_aluno = float(input("Digite a média final do aluno: "))
    
    if 0.0 <= media_aluno <= 4.9:
        conceito = "D"
    elif 5.0 <= media_aluno <= 6.9:
        conceito = "C"
    elif 7.0 <= media_aluno <= 8.9:
        conceito = "B"
    elif 9.0 <= media_aluno <= 10.0:
        conceito = "A"
    else:
        conceito = "Média inválida"
    
    print(f"Aluno: {nome_aluno}, Média: {media_aluno:.2f}, Conceito: {conceito}")
