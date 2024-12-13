def menu():
    menu = """
    BEM-VINDO AO SEU SISTEMA DE BANCO

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [0]\tSair

    => """
    return input(menu)

def depositar(saldo, valor, transacao, extrato):
    if valor < 0:
        print('Operação falhou! O valor informado é inválido.')
    else:
        saldo += valor
        transacao.append('Depósito')
        transacao.append('|')
        transacao.append(valor)
        transacao.append('|')
        transacao.append(saldo)
        extrato.append(transacao.copy())
        transacao.clear()
        print('Depósito realizado com sucesso!')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques, transacao):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    print("numero de saques",numero_saques)
    print()
    if excedeu_saldo:
        print('\nOperação falhou! Você não tem saldo suficiente.')
    elif excedeu_limite:
        print('\nOperação falhou! O valor do saque excede o limite.')
    elif excedeu_saques:
        print('\nOperação falhou! Número máximo de saques excedido.')
    elif valor > 0:
        saldo -= valor
        transacao.append('Saque')
        transacao.append('|')
        transacao.append(valor)
        transacao.append('|')
        transacao.append(saldo)
        extrato.append(transacao.copy())
        transacao.clear()
        numero_saques += 1
    else:
        print('\nOperação falhou! O valor informado é inválido.')

    return saldo, extrato

def exibir_extrato(extrato, saldo):
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

def main():
    SAQUE_LIMITE_QUANTIDADE = 3
    AGENCIA = "0001"
    SAQUE_LIMITE_VALOR = 500
    saldo = 0
    numero_saques = 0

    # extrato = (transacao(tipo_transacao, valor_transacao))
    extrato = list()
    transacao = list()

    while True:
        opcao = int(menu())

        if opcao == 1: # 1 => DEPÓSITO
            print('Operação selecionada: DEPÓSITO')
            valor = float(input("Informe o valor do depósito => R$ "))

            saldo, extrato = depositar(saldo, valor, transacao, extrato)
        
        elif opcao == 2: # 2 => SAQUE
            print('Operação selecionada: SAQUE')
            valor = float(input("Informe o valor do saque => R$ "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=SAQUE_LIMITE_VALOR,
                numero_saques=numero_saques,
                limite_saques=SAQUE_LIMITE_QUANTIDADE,
                transacao=transacao
            )
        
        elif opcao == 3: # 3 => EXIBIR EXTRATO
            print('\nOperação selecionada: EXTRATO')
            exibir_extrato(extrato=extrato, saldo=saldo)

        elif opcao == 0: # 0 => SAIR
            print("\n> Obrigada pela preferência. Volte sempre!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()