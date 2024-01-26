menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor para depositar:"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor Inválido")
    elif opcao == "s":
        print("Saque")
        valor_do_saque = float(input("Digite o valor para ser sacado: "))
        if numero_saques <= LIMITE_SAQUES and valor_do_saque <= limite:
            print("Saque de {valor_do_saque} efetuado com sucesso.")
            saldo -= valor_do_saque
            numero_saques +=1
            extrato += f"Saque: R$ {valor_do_saque:.2f}\n"
        else:
            print("saque falhou")
    elif opcao == "e":
        print(f"Extrato:")
        print(f"As operações da suas conta foram:\n")
        print(f"{extrato}\n")
        print(f"Seu saldo atual é de {saldo:.2f}")

    elif opcao == "q":
        break
    else:
        print("Operação inválida")