menu = """
BEM-VINDO AO SEU SISTEMA DE BANCO

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

msg_saida = """
> Obrigada pela preferência. Volte sempre!

"""

saldo = 0

# extrato = (transacao(tipo_transacao, valor_transacao))
extrato = list()

transacao = list()

saque_quantidade = 0
SAQUE_LIMITE_VALOR = 500
SAQUE_LIMITE_QUANTIDADE = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        print('Operação selecionada: DEPÓSITO')
        # 1 => depósito
        deposito_valor = float(input("""Valor a ser depositado
=> R$ """))  
        if deposito_valor < 0:
            print('Valor inválido. Tente novamente.')
        else:
            saldo += deposito_valor
            transacao.append('Depósito')
            transacao.append('|')
            transacao.append(deposito_valor)
            transacao.append('|')
            transacao.append(saldo)
            extrato.append(transacao.copy())
            transacao.clear()

    elif opcao == 2:
        print('Operação selecionada: SAQUE')
        # 2 => saque
        if saque_quantidade <= SAQUE_LIMITE_QUANTIDADE:
            saque_valor = float(input("""Valor a ser sacado
=> R$ """))
            if saque_valor < 0:
                print('Valor inválido. Tente novamente.')
            elif saque_valor <= SAQUE_LIMITE_VALOR:
                if saque_valor < saldo:
                    saldo -= saque_valor
                    transacao.append('Saque')
                    transacao.append('|')
                    transacao.append(saque_valor)
                    transacao.append('|')
                    transacao.append(saldo)
                    extrato.append(transacao.copy())
                    transacao.clear()
                else:
                    print(f'Não é possível realizar saque por falta de saldo. Saldo atual: R$ {saldo: .2f}')
            else:
                print('Valor limite para saque excedido. O limite para saque é de R$ 500,00. Tente novamente.')
            saque_quantidade += 1
        else:
            print('Limite diário de saques atingido. Tente novamente amanhã.')
            
    elif opcao == 3:
        print('\nOperação selecionada: EXTRATO')
        print(f"{"Tipo transação":20} | {"Valor":20} | {"Saldo":20}")
        for i in extrato:
            for j in i:
                if isinstance(j, (int, float)):
                    print(f'R$ {j:17.2f}', end='')
                elif j == '|':
                    print(f' {j} ', end='')
                else:
                    print(f'{j:20}', end='')
            print()
        print(f'\n=> Saldo final: R$ {saldo:.2f}')

    elif opcao == 0:
        print(msg_saida)
        break

    else:
        print('Operação inválida. Por favor, selecione novamente a operação desejada.')