#  Class View
---

Esta classe utiliza as funcionalidades da classe **Controller** e retorna valores formatados, com mensagens padronizadas. Esta apresenta uma, das várias formas, de se utilizar as funções disponíveis.

```python
import Controller
ctrl = Controller.Controller()
class View():

...
```
Antes da definição da classe **View** o arquivo importa a classe **Controller** e cria uma instância *ctrl* que fica disponível para uso na classe. Essa foi uma forma de trabalhar apenas com um instância de Controller, com todas as funções de verificação disponível.

- `conjunto_universo`: Uma função que disponibiliza todos o conjunto com todos elementos.
```python
def conjunto_universo(self):
    return ctrl.universo()
```

- `inserir nome`: Verifica o resultado da verificação, se no nome já existe ou não, retornando uma mensagem personalizada.
```python
def inserir_nome_conjunto(self, objeto, nome):
    if ctrl.verificar_nome(nome) == False:
    print(f'Nome {nome} de conjunto j´a existe.Insira outro nome para o conjunto.')
    
    else:
        objeto.inserir_nome(nome)
        print(f'Nome de conjunto {nome} inserido com sucesso')
```

- `inserir_elemento_conjunto`: Recebe o objeto conjunto a com a classe Controller verifica a existência do nome.

```python
def inserir_elemento_conjunto(self, objeto, elemento):
    if ctrl.inserir_elemento(objeto, elemento) == False:
        print(f'Elemento {elemento} j´a existe neste conjunto {objeto.nome}. Insira outro elemento.')
    else:
        objeto.inserir_elemento(elemento)
    print(f'Elemento {elemento} inserido com sucesso no conjunto {objeto.nome}')
```

- `elementos_conjuntos`: uma função que apresenta a lista de forma personalizada, no formato padrão de um conjunto.

```python 
def elementos_conjunto(self, objeto):
    conjunto = str(objeto.lista)
    conjunto = conjunto.replace('[', '{')
    conjunto = conjunto.replace(']', '}')
    print(f'Elemento do conjunto: {objeto.nome} = {conjunto}')
```

- `tamanho_conjunto`: retorna o tamanho do conjunto.

```python
def tamanho_conjunto(self, objeto):
    print(f'Tamnho do conjunto {objeto.nome} e: {len(objeto.lista)}')
```

- `elemento_pertence`: Função que verifica a propriedade de pertencimento de um elemento em um conjunto, funcionalidade implementada na classe
Controller.

```python
def elemento_pertence(self, elemento, objeto):
    if ctrl.elemento_pertence(elemento, objeto):
        print(f'O elemento {elemento} "pertence" ao Conjunto {objeto.nome}')
    else:
        print(f'O elemento {elemento} "não" pertence ao Conjunto {objeto.nome}')
```

- `conjunto_subconjunto`: Funcionalidade disponível a classe Controller, retorna o resultado da verificação dos objetos passados pela função.

```python
def conjunto_subconjunto(self, objeto1, objeto2):
    if ctrl.conjunto_subconjunto(objeto1, objeto2):
        print(f'Conjunto {objeto1.nome} ´e subconjunto de {objeto2.nome}')
    else:
        print(f'Conjunto {objeto1.nome} ´e n~ao subconjunto de {objeto2.nome}')
```

- `conjunto prorpio`: Retorna o resultado da verificação do entre os objetos, a relação de subconjuntos.
```python
def conjunto_proprio(self, objeto1, objeto2):
    if ctrl.conjunto_proprio(objeto1, objeto2):
        print(f'Conjunto {objeto1.nome} é conjunto próprio em relação ao conjunto {objeto2.nome}')
    else:
        print(f'Conjunto {objeto1.nome} não é conjunto próprio em relação ao conjunto {objeto2.nome}')
```
- `operacoes_conjuntos_uniao`: Esta função é um agrupamento que utiliza outras funções disponibilizadas no Controller, a fim de evitar repetição de código e apresentar corretamente as operações de **União de Conjuntos**.

```python
def operacoes_conjuntos_uniao(self, objeto1, objeto2):
    if ctrl.elemento_neutro_uniao(objeto1, objeto2):
        print(f'Um ou mais conjuntos são neutros.Conjunto {objeto1.nome}:{objeto1.lista} Conjunto {objeto2.nome}:{objeto2.lista}')
    elif ctrl.idem_potencia_uniao(objeto1, objeto2):
        print(f'Ambos conjuntos possuem os mesmos valores.Conjunto {objeto1.nome}:{objeto1.lista Conjunto {objeto2.nome}:{objeto2.lista}')
    else:
        if ctrl.relacao_conjunto(objeto1, objeto2):
            print(f'União entre o conjunto {objeto1.nome} e {objeto2.nome} já existe!')
        else:
            conjunto = ctrl.uniao_conjunto(objeto1, objeto2)
            print(f'União dos Conjuntos {objeto1.nome} e {objeto2.nome}: {conjunto}')
```

- `operacoes_conjuntos_interseccao`: Semelhante a operações de União, esta
função reutiliza outras funções para implementar corretamente a Intersecção de conjuntos.

```python
def operacoes_conjuntos_interseccao(self, objeto1, objeto2):

    if ctrl.elemento_neutro_interseccao(objeto1, objeto2):
        print(f'Elemento neutro da Intersec¸c~ao: {objeto1.nome} n Universo ´e: {objeto1.lista}')

    elif ctrl.idem_potencia_interseccao(objeto1, objeto2):
        print(f'Conjuntos iguais: Conjunto 1:{objeto1.nome} - Conjunto 2 {objeto2.nome}- Idem Potência da Intersecção')

    else:
        if ctrl.relacao_conjunto_interseccao(objeto1, objeto2):
            print(f'Uni~ao entre o conjunto {objeto1.nome} e {objeto2.nome} j´a existe!')
        else:
            conjunto = ctrl.interseccao_conjunto(objeto1, objeto2)
            print(f'Intersec¸c~ao entre os conjuntos: {objeto1.nome} e {objeto2.nome}: {conjunto}')
```

- `diferenca_conjunto`: apresenta o resultado da diferença entre conjuntos.

```python
def diferenca_conjunto(self, objeto1, objeto2):
    conjunto = ctrl.diferenca_conjunto(objeto1, objeto2)
    print(f'A diferençaa entre {objeto1.nome} e {objeto2.nome} = {conjunto}')
```

- `conjunto_partes`: apresenta o resultado do conjunto das partes.

```python
def conjunto_partes(self, objeto):
    conjunto = ctrl.conjunto_partes("", objeto.lista, len(objeto.lista), objeto.nome)
```

- `complemento_conjunto`: Apresenta o resultado para o complemento do
conjunto.

```python
def complemento_conjunto(self, objeto1, objeto2):
    conjunto = ctrl.complemento(objeto1, objeto2)
    print(f'Complemento do conjunto {objeto1.nome}: {conjunto}')
```
