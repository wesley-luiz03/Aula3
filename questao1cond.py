#Solicitando ao usuário que insira o saldo médio
saldo_medio = float(input("Digite o saldo médio do cliente: "))

#Calculando a faixa de saldo médio e o crédito do cliente
if saldo_medio <= 500:
    credito = 0
elif saldo_medio <= 1000: #Valores maior que 500
    credito = saldo_medio * 0.20
elif saldo_medio <= 2000: #Valores maior que 1000
    credito = saldo_medio * 0.30
else: #Calculando qualquer valor acima de 2000
    credito = saldo_medio * 0.40
    
#Imprimindo o resultado    
print(f"Saldo médio: R$ {saldo_medio:.2f}")
print(f"Crédito concedido: R$ {credito:.2f}")