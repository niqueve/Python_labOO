from datetime import datetime

valor_em_conta = 0
movimentacao = []

#verifica se quer continuar
def verifica():
    resposta = (input("Digite SIM caso deseje retornar ao menu anterior ou pressione qualquer outra tecla para encerrar: ")).upper()
    if resposta == "SIM":
        menu_principal()
    else:
        None
#registro de movimentação
def registro(saldo_atual, operacao):
    global movimentacao
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    movimentacao.append([data,operacao,saldo_atual])

# Saque
def saque():
    global valor_em_conta
    if valor_em_conta > 0:
        valor_saque = float(input("Quanto deseja sacar?"))
        if (valor_em_conta >= valor_saque):
            valor_em_conta -= valor_saque
            registro(valor_em_conta, "saque")
            print("Saque realizado com sucesso, valor em conta: ", valor_em_conta)
            verifica()
        else:
            print("Você não possui dinheiro suficiente em conta para o saque")
    else:
        print("você não possui dinheiro em conta")
        resposta = (input("Digite SIM caso deseje retornar ao menu anterior ou pressione qualquer outra tecla para encerrar: ")).upper()
        verifica()

# Depósito
def deposito():
    global valor_em_conta
    valor_deposito = float(input("Quanto deseja depositar? "))
    if valor_deposito >= 0:
        valor_em_conta += valor_deposito
        print(f"Você depositou {valor_deposito} \n seu novo saldo é de: {valor_em_conta}")
        registro(valor_em_conta,"deposito")
        verifica()
    else:
        print("Não é permitido o depósito de valores negativos")
        resposta = (input("Digite sim caso deseje depositar outro valor: ")).upper
        if resposta == "SIM":
            deposito()
        else:
            verifica()
# Extrato
def extrato ():
    global movimentacao
    if len(movimentacao) > 0:
        for n in movimentacao:
            print(f"{n[0]} - operação {n[1]} - saldo {n[2]}")
        verifica()
    else:
        print("Você não possui extrato disponivel")
        verifica()

# Empréstimo
def emprestimo ():
    global valor_em_conta
    valor_emprestimo = 0
    if (valor_em_conta >=800)%(valor_em_conta<=1000):
        valor_emprestimo = (valor_em_conta*10)/100
        print(f"Você tem {valor_emprestimo} para empréstimo liberado")
    elif (valor_em_conta > 1000) % (valor_em_conta <= 5000):
        valor_emprestimo = (valor_em_conta * 30) / 100
        print(f"Você tem {valor_emprestimo} para empréstimo liberado")
    elif (valor_em_conta > 5000)%(valor_em_conta<=10000):
        valor_emprestimo = (valor_em_conta*50)/100
        print(f"Você tem {valor_emprestimo} para empréstimo liberado")
    elif (valor_em_conta > 10000):
        valor_emprestimo = (valor_em_conta*100)/100
        print(f"Você tem {valor_emprestimo} para empréstimo liberado")
    else:
        print("Você não possui valor liberado para empréstimo")
        
    verifica()

# menu principal
def menu_principal():
    global valor_em_conta
    print("Bem vindo, seu saldo atual é de: ", valor_em_conta )
    print("1- Saque \n 2-Depósito \n 3-Extrato \n 4- Empréstimo")
    opcao = int(input("Digite o número da opção desejada: "))
    match opcao:
        case 1:
            saque()
        case 2:
            deposito()
        case 3:
            extrato()
        case 4:
            emprestimo()
        case _:
            print("Operação encerrada")


# Tela inicial de login
def login():
    user_permido = ["USUARIO", "USUÁRIO"]
    pin = "12345"
    contador = 3
    while contador > 0:
        usuario = input("Digite o nome do usuário: ").upper()
        senha = input("Digite a sua senha: ")
        if (usuario in user_permido) & (senha == pin):
            print("Usuário autenticado")
            menu_principal()
            break
        else:
            print("Acesso negado")
            contador -= 1
            print(f"você possui {contador} tentativas")

    print("Operação encerrada")
login()