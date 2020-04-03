import Controller
ctrl = Controller.Controller()


class View():

    def conjunto_universo(self):
        return ctrl.universo()

    def inserir_nome_conjunto(self, objeto, nome):
        if ctrl.verificar_nome(nome) == False:
            print(
                f'Nome {nome} de conjunto já existe. Insira outro nome para o conjunto.')
        else:
            objeto.inserir_nome(nome)
            print(f'Nome de conjunto {nome} inserido com sucesso')

    def inserir_elemento_conjunto(self, objeto, elemento):
        if ctrl.inserir_elemento(objeto, elemento) == False:
            print(
                f'Elemento {elemento} já existe neste conjunto {objeto.nome}. Insira outro elemento.')
        else:
            objeto.inserir_elemento(elemento)

            print(
                f'Elemento {elemento} inserido com sucesso no conjunto {objeto.nome}')

    def elementos_conjunto(self, objeto):
        conjunto = str(objeto.lista)
        conjunto = conjunto.replace('[', '{')
        conjunto = conjunto.replace(']', '}')
        print(f'Elemento do conjunto: {objeto.nome} = {conjunto}')

    def tamanho_conjunto(self, objeto):
        print(f'Tamnho do conjunto {objeto.nome} é: {len(objeto.lista)}')

    def elemento_pertence(self, elemento, objeto):
        if ctrl.elemento_pertence(elemento, objeto):
            print(
                f'O elemento {elemento} "pertence" ao Conjunto {objeto.nome}')
        else:
            print(
                f'O elemento {elemento} "não" pertence ao Conjunto {objeto.nome}')

    def conjunto_subconjunto(self, objeto1, objeto2):
        if ctrl.conjunto_subconjunto(objeto1, objeto2):
            print(f'Conjunto {objeto1.nome} é subconjunto de {objeto2.nome}')
        else:
            print(
                f'Conjunto {objeto1.nome} é não subconjunto de {objeto2.nome}')

    def conjunto_proprio(self, objeto1, objeto2):
        if ctrl.conjunto_proprio(objeto1, objeto2):
            print(
                f'Conjunto {objeto1.nome} é conjunto próprio em relação ao conjunto {objeto2.nome}')
        else:
            print(
                f'Conjunto {objeto1.nome} não é conjunto próprio em relação ao conjunto {objeto2.nome}')

    def operacoes_conjuntos_uniao(self, objeto1, objeto2):
        if ctrl.elemento_neutro_uniao(objeto1, objeto2):
            print(
                f'Um ou mais conjuntos são neutros. Conjunto {objeto1.nome}:{objeto1.lista} - Conjunto {objeto2.nome}:{objeto2.lista}')
        elif ctrl.idem_potencia_uniao(objeto1, objeto2):
            print(
                f'Ambos conjuntos possuem os mesmos valores. Conjunto {objeto1.nome}:{objeto1.lista} - Conjunto {objeto2.nome}:{objeto2.lista}')
        else:
            if ctrl.relacao_conjunto(objeto1, objeto2):
                print(
                    f'União entre o conjunto {objeto1.nome} e {objeto2.nome} já existe!')
            else:
                conjunto = ctrl.uniao_conjunto(objeto1, objeto2)
                print(
                    f'União dos Conjuntos {objeto1.nome} e {objeto2.nome}: {conjunto}')

    def operacoes_conjuntos_interseccao(self, objeto1, objeto2):
        if ctrl.elemento_neutro_interseccao(objeto1, objeto2):
            print(
                f'Elemento neutro da Intersecção: {objeto1.nome} n Universo é: {objeto1.lista}')
        elif ctrl.idem_potencia_interseccao(objeto1, objeto2):
            print(
                f'Conjuntos iguais: Conjunto 1: {objeto1.nome} - Conjunto 2 {objeto2.nome} - Idem Potência da Intersecção')
        else:
            if ctrl.relacao_conjunto_interseccao(objeto1, objeto2):
                print(
                    f'União entre o conjunto {objeto1.nome} e {objeto2.nome} já existe!')
            else:
                conjunto = ctrl.interseccao_conjunto(objeto1, objeto2)
                print(
                    f'Intersecção entre os conjuntos: {objeto1.nome} e {objeto2.nome}: {conjunto}')

    def diferenca_conjunto(self, objeto1, objeto2):
        conjunto = ctrl.diferenca_conjunto(objeto1, objeto2)

        print(f'A diferença entre {objeto1.nome} e {objeto2.nome} = {conjunto}')

    def conjunto_partes(self, objeto):
        conjunto = ctrl.conjunto_partes(
            "", objeto.lista, len(objeto.lista), objeto.nome)

    def complemento_conjunto(self, objeto1, objeto2):
        conjunto = ctrl.complemento(objeto1, objeto2)

        print(f'Complemento do conjunto {objeto1.nome}: {conjunto}')
