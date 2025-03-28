class Pessoa:
    def __init__ (self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def exercito (self):
        if self.altura > 1.70:
            print(f"Parabêns {self.nome} você entrou para o exército\n")
        else:
            print(f"Você foi dispensado {self.nome}\n")

    def __str__(self):
        return f"nome: {self.nome} \nidade: {self.idade} \naltura: {self.altura}\n"


pessoa1 = Pessoa("Julio", 18, 1.71)
pessoa2 = Pessoa("Paulo", 19, 1.69)
print(pessoa1)
pessoa1.exercito()
print(pessoa2)
pessoa2.exercito()

