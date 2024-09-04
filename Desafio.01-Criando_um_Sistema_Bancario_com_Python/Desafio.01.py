## NTT DATA & DIO - Bootcamp Engenharia de Dados com Python
## Autor das modificações: Lucas Chiara
## Modificações: inclusão de data e hora no extrato
## 04/09/2024
## Desafio 01

import datetime

# esta funcao inclui a data e hora da operacao nos registros do extrato
def hora_transacao():
  global data_completa, data, hora
  t=datetime.datetime.now() #obtem data e hora no momento da operacao
  data_completa=t.strftime('%d/%m/%Y %H:%M:%S') # formatacao data e hora
  data=t.strftime('%d/%m/%Y') # formatacao data
  hora=t.strftime('%H:%M:%S') # formatacao hora

menu = """
Bem Vindo ao Banco XX
Por favor escolha a opção desejada:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        hora_transacao()

        if valor > 0:
            saldo += valor
            extrato += f"{data_completa} Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        hora_transacao()

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"{data_completa} Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        hora_transacao()
        print("\n================ EXTRATO ================")
        print('Data: ',data, '  Hora: ',hora,'\n')
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
