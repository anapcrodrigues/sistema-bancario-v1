# 💲Criando um Sistema Bancário com Python

<img src="Savings-bro.png" alt="Mão colocando nota de dinheiro em um cofre no formato de um porquinho redondo e sorridente.">

> Projeto desenvolvido a partir de um desafio do bootcamp NTT DATA - Engenharia de Dados com Python disponível na plataforma [DIO](https://web.dio.me/home).
## 🎯 Objetivo geral
- (v1) Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
- (v2) Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

## 🚀 Desafio
> (v1) Fomos contratos por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
> (v2) Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar extrato. Além disso, para a versão 2 (v2) do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
- Você instalou a versão mais recente de `python`
  
## ⚠️ Premissas
O projeto está na versão v1, na mesma trabalhamos apenas com 1 usuário, dessa forma não nos preocuparemos em identificar qual o número da agência e conta bancária.

## 📝 Requisitos
### Operações
   1. Depósito
   2. Saque
   3. Extrato

### 1. Operação - depósito
- Depositar valores positivos.
- Haverá apenas 1 usuário. Não é necessário identificar conta e banco.
- Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### 2. Operação - saque
- Sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
- Se não tiver saldo, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### 3. Operação - extrato
- Deve listar todos os depósitos e saques realizados na conta.
- No fim da listagem deve ser exibido o saldo atual da conta.
- Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45.

### Funções
## Saque
A função saque deve receber os argumentos apenas por nome (*keyword only*). Sugestão de argumentos: saldo, valor, extrato, limite, número_saques, limite_saques. Sugestão de retorno: saldo e extrato.

## Depósito
A função depósito deve receber os argumentos apenas por posição (*positional only*). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

## Extrato:
A função extrato deve receber os argumentos por posição e nome (*positional only* e *keyword only*). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Criar usuário (cliente)
- O programa deve armazenar os usuários em uma lista.
- Um usuário é comporto por: nome, data de nascimento, cpf e endereço.
- O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado.
- Deve ser armazenado somente os números do CPF.
- Não podemos cadastrar 2 usuários com o mesmo CPF.

## Cria conta corrente
- O programa deve armazenar contas em uma lista.
- Uma conta é composta por: agência, número da conta e usuário.
- O número da conta é sequencial, iniciando em 1.
- O número da agência é fixo: "0001".
- O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
Dica: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.

## 📫 Contribuindo para o projeto

Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
