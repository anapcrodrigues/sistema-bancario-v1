menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0

transacao = dict()

extrato = ""

saque_quantidade = 0
SAQUE_LIMITE_VALOR = 500
SAQUE_LIMITE_QUANTIDADE = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print('depósito')
        # 1 => depósito
        deposito = float(input("""Valor a ser depositado
=> R$ """))  
        if deposito < 0:
            print('Valor inválido. Tente novamente.')
        else:
            saldo += deposito
            transacao['Tipo'] = 'Depósito'
            transacao['Valor'] = deposito

    elif opcao == 2:
        print('saque')
        # 2 => saque
        if saque_quantidade < SAQUE_LIMITE_QUANTIDADE:
            saque_quantidade += 1
        else:
            print('Limite diário de saques atingido. Tente novamente amanhã.')
            break
        saque_valor = input("""Valor a ser sacado
=> R$ """)
        if saque_valor <= SAQUE_LIMITE_VALOR:
            if saque_valor < saldo:
                saldo -= saque_valor
                transacao['Tipo'] = 'Saque'
                transacao['Valor'] = saque_valor
            else:
                print('Não é possível realizar saque por falta de saldo.')
        else:
            print('Valor limite para saque excedido. Tente novamente.')
            
    elif opcao == 3:
        print('extrato')

    elif opcao == 0:
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')