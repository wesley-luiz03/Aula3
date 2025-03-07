saldo_medio = float(input("Digite o saldo médio do cliente: "))

match saldo_medio:
    case saldo if saldo <= 500:
        credito = 0
    case saldo if saldo <= 1000:
        credito = saldo * 0.20
    case saldo if saldo <= 2000:
        credito = saldo * 0.30
    case _:
        credito = saldo_medio * 0.40
        
print(f"Saldo médio: R$ {saldo_medio:.2f}")
print(f"Crédito concedido: R$ {credito:.2f}")