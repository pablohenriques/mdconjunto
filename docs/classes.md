#  Classes
---

Conforme solicitado para este projeto foi criado um programa que implementasse um tipo de dado 'Conjunto'. Para o desenvolvimento da solução foi utilizado a linguagem de programação Python.

## Class Conjunto
Esta classe implementa o tipo de dado Conjunto e possui alguns atributos e funções. Não possui complexidade para a criação de objetos. Apesar de ser possível acessá-la diretamente, neste projeto foram utilizados outras formas para a criação de conjuntos. 

```python
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
```

## Elementos e Funcionalidades

Esta classe possui apenas três elementos e quatro funções:
 - `lista`: Elemento do tipo lista que recebe todos a valores do conjunto
- `nome`: Elemento que recebe o nome do Conjunto
- `infinito`: Elemento que recebe True ou False para um valor infinito
- `inserir nome`: Função que insere o nome do conjunto
- `inserir elemento`: Fun¸c˜ao que insere o um item no conjunto
- `inserir infinito`: Fun¸c˜ao que insere o valor para infinito
- `lista (função)`: Retorna todos os elementos da lista ou o conjunto