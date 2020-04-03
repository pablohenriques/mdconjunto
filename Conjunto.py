
class Conjunto():

    def __init__(self):
        self.lista = []
        self.nome = ''
        self.infinito = False

    def inserir_nome(self, nome):
        self.nome = nome

    def inserir_elemento(self, elemento):
        self.lista.append(elemento)
    
    def inserir_infinito(self, condicao):
        self.infinito = condicao
    
    def lista(self):
        return self.lista

    

    