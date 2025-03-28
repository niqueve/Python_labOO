#Aula 1: Revisando programação estruturada:
Desenvolva um caixa eletrônico, em Python. O caixa eletrônico deve conter:

login para entrar no sistema;
menu principal contendo os serviços:
Saque
Depósito
Extrato
Empréstimo
Detalhes:

O usuário só pode ter 3 tentativas para fazer login, se exceder as tentativas o sistema emite uma mensagem de bloqueio e encerra;
Ele só pode sacar se tiver dinheiro na conta, caso contrário uma mensagem é emitida impedindo o saque;
O empréstimo é dado nas seguintes condições:
Se ele tiver entre R$ 800,00 a R$ 1.000,00, ele ganha 10% do valor que tiver na conta corrente;
Se ele tiver entre R$ 1000,01 e R$ 5.000,00 ele ganha 30% do valor que tiver na conta corrente;
Se ele tiver entre R$ 5.000,01 e R$ 10.000,00 ele ganha 50% do valor que tiver na conta corrente;
Se ele tiver igual ou maior que R$ 10.000,01 ele ganha 100% do valor que tiver na conta corrente;