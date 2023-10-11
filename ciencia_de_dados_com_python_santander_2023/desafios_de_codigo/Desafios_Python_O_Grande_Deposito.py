valor = float(input())
saldo=0.0

if valor > 0:
    saldo=+valor
    print(f"""Deposito realizado com sucesso!
Saldo atual: R$ {saldo:.2f}""")
elif valor < 0:
   print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")
  