 # Class Controller
 ---
A classe 'Controller' armazena todas regras de negócio da aplicação e gerencia o comportamento da aplicação. E nessa classe que estão implementadas funcionalidades avançadas para a criação e verificação dos conjuntos.

## Variáveis Globais

```python
class Controller():
    #VARIAVEIS GLOBAIS
    conjuntos_existentes = []
    relacoes_exsitentes = []
    conjunto_universo = []
#...
```

As variáveis globias são utilizadas para armazenar valores que serão reutilizadas pelas funções das classes:
- `conjuntos_existentes`: Armazena os nomes dos conjuntos existentes, impedido a repetição de nomes
- `relacoes_existentes`: Armazena um relação de uniãoo ou intersecção entre conjuntos a fim de repetir opera¸cões.
- `conjunto_universo`: armazena todos os elementos de todos os conjuntos

##  Operações Básicas

```python
#OPERAÇÕES BÁSICAS DE CONJUNTO
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
```

As operações básicas para os conjuntos são operações que verificam a existência de um valor e caso ele não seja repetido, adicionado a lista.

- `verifica nome`: realiza uma pesquisa em conjuntos existentes e retorna *True* ou *False*, caso o nome não exista ou exista, respectivamente.

- `inserir elemento`: recebe um objeto, do tipo conjunto que contem a lista e elementos e verifica se o elemento passado no parâmetro já existe neste objeto e caso não exista o elemento do parâmetro é adicionado a lista do objeto.

- `universo`: Retorna todos os elementos do conjunto universo.

## Operações entre elementos e conjuntos

```python
#OPERAÇôES ENTRE ELEMENTOS E CONJUNTOS
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
```

Neste bloco do código estão as operações entre elementos e conjuntos verificando uma propriedade entre os conjuntos.

- `elemento_pertence`: verifica se um elemento pertence a uma lista(conjunto) do objeto passado no parâmetro, caso o objeto não exista retorna True, caso o elemento exista False.

- `conjunto_subconjunto`: verifica se a lista do primeiro objeto é sub conjunto do segundo objeto, com uma função percorrendo os elementos da lista.

- `conjunto_proprio`: verifica a propriedade de conjunto próprio entre o primeiro e segundo objeto, retornando verdadeiro ou falso.


## Álgebra de Conjuntos
Esta parte do código apresenta a lógica para a implementação da Álgebra de Conjuntos, que são operações realizada entre os conjuntos que contem as propriedades para união, intersecção, diferença, complemento e conjunto das partes entre os conjuntos. Para implementação das operações foram criadas algumas funções auxiliares para complementar a verificação das propriedades.

```python
#ALGEBRA DE CONJUNTOS

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
```

Funções de verificação, para união de conjuntos:
- `adicionar_relacoes`: adiciona uma relação no formato *string* em uma lista de dicionários.

- `relacao_conjunto`: verifica se uma relação de união já existe na lista global de relações, percorrendo a lista e as chaves dos dicionários.

- `relacao_conjunto_interseccao`: semelhante a função relação conjunto, verifica se já existe uma relação de intersecão na lista globla de relações.

```python
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
```

Funções de verificação, para intersecção de conjuntos:

- `elemento_neutro_interseccao`: esta função verificar a propriedade do elemento neutro da intersecção, comparando os conjuntos passado com os elementos do conjunto universo e caso haja algum elemento igual retorna *True*, se não, retorna *False*.

- `idem_potencia_interseccao`: verifica se os conjuntos passados possuem as mesmas lista, caso sejam iguais retornam *True*, se não *False*.

## União de Conjuntos
```python
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
```

Propriedades da União:

- `elemento_neutro_uniao`: verifica se algumas das listas dos conjuntos passado está vazia e retorno *True* ou *False*.

- `idem_potencia_uniao`: verifica se o mesmo conjunto está sendo passado duas vezes, retornando *True* ou *False*.

- `uniao_conjunto`: realiza a união dos conjuntos fazendo algumas verificações. Primeiro monta a relaãoo da união com os nomes dos conjuntos(passado nos parâmetros do objeto). Segundo as variáveis auxiliares para receber os conjuntos. Terceiro, os condicionais verificam se as listas possuem valores infinitos, pois o valor infinito deve ser o último elemento da lista. Caso não exista nenhum valor infinito ou as duas listas possuam valores infinitos, a variável conjunto aceita todos os valores. Por fim, a chamada da função ***adicionar_relacoes*** que adiciona a relação e o conjunto na lista global de relações e retorna o lista da união dos conjuntos.

 ## Intersecção dos Conjuntos

 ```python
def interseccao_conjunto(self, objeto1, objeto2):
    conjunto = []
    relacao = f'{objeto1.nome}n{objeto2.nome}'
    restante = objeto2.lista.copy()

    for i in objeto1.lista:
        if i in restante:
            conjunto.append(i)
    self.adicionar_relacaoes(relacao, conjunto)

    return conjunto
 ```

 Esta função recebe dois conjuntos e verifica os elementos em comum, adiciona e uma lista e retorna os valores. Também, cria uma relação entre os conjuntos e adicona na lista global de relações.

 ## Diferença entre os conjuntos

 ```python 
def diferenca_conjunto(self, objeto1, objeto2):
    conjunto_diferenca = []
    
    for i in objeto1.lista:
        if i not in objeto2.lista:
        conjunto_diferenca.append(i)

    return conjunto_diferenca
 ```

Função simples, que verifica se os elementos do primeiro objeto não existem na lista do segundo objeto e adiciona os elementos em um lista. Ao final retorna a lista com valores.

```python
def conjunto_partes(self, conjunto_final, conjunto, length, nome):
    if((len(self.conjunto_p) + 1) == pow(2, length)):
        print(f'Conjunto das partes do conjunto {nome}: {self.conjunto_p}')
    if len(conjunto) == 0:
        self.conjunto_p.append(conjunto_final)
    else:
    self.conjunto_partes(conjunto_final+conjunto[0], conjunto[1::], length, nome)
    self.conjunto_partes(conjunto_final, conjunto[1::], length, nome)
```

A função recursiva que a cada chamada da função envia dois arrays com o segundo array [1 : :] até o segundo array ter tamanho 0 e concatena o valor dos dois arrays dentro de uma lista global e depois retorna essa lista.

## Complemento de um conjunto
```python
def complemento(self, objeto1, objeto2):
    conjunto = []

    for i in objeto2.lista:
        if i not in objeto1.lista:
            conjunto.append(i)
    return conjunto
```
Função semelhante a diferença de conjuntos, porém de maneira inversa, ou seja, os valores do segundo conjunto são comparados com o primeiro conjunto e caso não existam no primeiro conjunto, os valores são armazenados na lista e retornados ao final da função.