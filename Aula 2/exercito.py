class Pessoa:
    def __init__ (self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

def exercito (altura):
    if altura > 1.70:
        print("Voce entrou para o exército")
    else:
        print("Você foi dispensada")

pessoa1 = Pessoa("Julio", 18, 1.71)
exercito(pessoa1.idade)