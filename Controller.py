
class Controller():

    # VARIÁVEIS GLOBAIS
    conjuntos_existentes = []
    relacoes_exsitentes = []
    conjunto_universo = []
    conjunto_p = []
    # OPERAÇÕES BÁSICAS DE CONJUNTO

    def verificar_nome(self, nome):
        if nome in self.conjuntos_existentes:
            return False

        self.conjuntos_existentes.append(nome)
        return True

    def inserir_elemento(self, objeto, elemento):
        if elemento in objeto.lista:
            return False
        if elemento not in self.conjunto_universo:
            self.conjunto_universo.append(elemento)
        return True

    def universo(self):
        return self.conjunto_universo

    # OPERAÇÕES ENTRE ELEMENTOS E CONJUNTOS
    def elemento_pertence(self, elemento, objeto):
        if elemento in objeto.lista:
            return True
        return False

    def conjunto_subconjunto(self, objeto1, objeto2):
        for i in objeto1.lista:
            if i not in objeto2.lista:
                return False
        return True

    def conjunto_proprio(self, objeto1, objeto2):
        if objeto1.lista == objeto2.lista:
            return False
        else:
            for i in objeto1.lista:
                if i not in objeto2.lista:
                    return False
        return True

    # ÁLGEBRA DE CONJUNTOS

    # Funções de verificação
    def adicionar_relacaoes(self, key, value):
        self.relacoes_exsitentes.append({key: value})

    # Funções de verificação
    def relacao_conjunto(self, objeto1, objeto2):
        relacao = f'{objeto1.nome}u{objeto2.nome}'
        relacao_inversa = relacao[::-1]
        for lista in self.relacoes_exsitentes:
            for key in lista:
                if key == relacao or key == relacao_inversa:
                    return True
        return False

    # Funções de verificação
    def relacao_conjunto_interseccao(self, objeto1, objeto2):
        relacao = f'{objeto1.nome}n{objeto2.nome}'
        relacao_inversa = relacao[::-1]
        for lista in self.relacoes_exsitentes:
            for key in lista:
                if key == relacao or key == relacao_inversa:
                    return True
        return False

    def elemento_neutro_uniao(self, objeto1, objeto2):
        if len(objeto1.lista) == 0 or len(objeto2.lista) == 0:
            return True
        return False

    def idem_potencia_uniao(self, objeto1, objeto2):
        if objeto1.lista == objeto2.lista:
            return True
        return False

    def uniao_conjunto(self, objeto1, objeto2):
        conjunto = []
        restante = []
        relacao = f'{objeto1.nome}u{objeto2.nome}'

        if objeto1.infinito == True:
            conjunto = objeto2.lista.copy()
            conjunto = objeto1.lista.copy()
        elif objeto2.infinito == True:
            conjunto = objeto1.lista.copy()
            conjunto = objeto2.lista.copy()
        else:
            conjunto = objeto1.lista.copy()
            restante = objeto2.lista.copy()

        for i in restante:
            if i not in conjunto:
                conjunto.append(i)

        self.adicionar_relacaoes(relacao, conjunto)

        return conjunto

    # Função de verificação
    def elemento_neutro_interseccao(self, objeto, conjunto):
        conjunto_interseccao = []

        if conjunto == self.conjunto_universo:
            for i in objeto.lista:
                if i in self.conjunto_universo:
                    conjunto_interseccao.append(i)
        else:
            return False

        if len(conjunto_interseccao) == 0:
            return False
        return True

    # Função de verificação
    def idem_potencia_interseccao(self, objeto1, objeto2):
        if objeto1.nome == objeto2.nome:
            return True

    def interseccao_conjunto(self, objeto1, objeto2):
        conjunto = []
        relacao = f'{objeto1.nome}n{objeto2.nome}'
        restante = objeto2.lista.copy()

        for i in objeto1.lista:
            if i in restante:
                conjunto.append(i)

        self.adicionar_relacaoes(relacao, conjunto)

        return conjunto

    def diferenca_conjunto(self, objeto1, objeto2):
        conjunto_diferenca = []

        for i in objeto1.lista:
            if i not in objeto2.lista:
                conjunto_diferenca.append(i)

        return conjunto_diferenca

    def conjunto_partes(self, conjunto_final, conjunto, length, nome):
        if((len(self.conjunto_p) + 1) == pow(2, length)):
            print(f'Conjunto das partes do conjunto {nome}: {self.conjunto_p}')

        if len(conjunto) == 0:
            self.conjunto_p.append(conjunto_final)
        else:
            self.conjunto_partes(
                conjunto_final+conjunto[0], conjunto[1::], length, nome)
            self.conjunto_partes(conjunto_final, conjunto[1::], length, nome)

    def complemento(self, objeto1, objeto2):
        conjunto = []

        for i in objeto2.lista:
            if i not in objeto1.lista:
                conjunto.append(i)
        return conjunto
