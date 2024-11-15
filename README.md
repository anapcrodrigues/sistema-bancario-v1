# 💲Criando um Sistema Bancário com Python

<img src="Savings-bro.png" alt="Mão colocando nota de dinheiro em um cofre no formato de um porquinho redondo e sorridente.">

## 🎯 Objetivo geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## 🚀 Desafio
> Fomos contratos por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
- Você instalou a versão mais recente de `python`
  
## ⚠️ Premissas
O projeto está na versão v1, na mesma trabalhamos apenas com 1 usuário, dessa forma não nos preocuparemos com identificar qual o número da agência e conta bancária.

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

## 📫 Contribuindo para o projeto

Para contribuir, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).