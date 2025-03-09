maior_altura = 0
menor_altura = float('inf')
soma_alturas = 0
soma_alturas_mulheres = 0
qntd_mulheres = 0


for i in range(5):
    print(f"\nPessoa {i + 1}:")
    altura = float(input("Digite a altura (em metros): "))
    genero = int(input("Digite o gênero (1 - Maculino, 2 - Feminino): "))
    
    if altura > maior_altura:
        maior_altura = altura
    if altura < menor_altura:
        menor_altura = altura
        
    soma_alturas += altura
    
    if genero == 2:
        soma_alturas_mulheres += altura
        qntd_mulheres += 1
        
media_altura_turma = soma_alturas / 5
media_altura_mulheres = soma_alturas_mulheres / qntd_mulheres if qntd_mulheres > 0 else 0

print("\nResultado:")
print(f"Maior altura da turma: {maior_altura:.2f} m")
print(f"Menor altura da turma: {menor_altura:.2f} m")
print(f"Média de altura das mulheres: {media_altura_mulheres:.2f} m")
print(f"Média de altura da turma: {media_altura_turma:.2f} m")