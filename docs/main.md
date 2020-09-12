# Arquivo Main
---

Por fim, um arquivo contém a implementação de todas as funcionalidade disponíveis nas classes **Conjunto**, **Controller** e **View**.

- **Criação dos Objetos**: Neste arquivo são instanciado os objetos necessários para a utilização da classe View e a criação dos objetos de Conjuntos. Por fim, para a utilizaçaão dos objetos, basta apenas utilizar as variáveis e
inserir os parâmetros.

```python
import Conjunto
import View

# OBJETOS DE CONJUNTO
C1 = Conjunto.Conjunto()
C2 = Conjunto.Conjunto()

# OBJETOS DE VIEW
vw = View.View()

# CONJUNTO UNIVERSO
universo = vw.conjunto_universo()
```

- **Inserindo nomes e elementos dos conjuntos**: Com as classes instanciadas, é possível realizar as operações básica de inserção de nome e elemento.
```python
# INSERIR NOME DO CONJUNTO
print('\n Inserindo nome do conjunto')
vw.inserir_nome_conjunto(C1, 'A')
vw.inserir_nome_conjunto(C1, 'A')
vw.inserir_nome_conjunto(C2, 'B')

# INSERIR ELEMENTOS DO CONJUNTO
print('\n Inserindo elementos nos conjuntos')
vw.inserir_elemento_conjunto(C1, 'x')
vw.inserir_elemento_conjunto(C1, 'y')
vw.inserir_elemento_conjunto(C1, 'x')
vw.inserir_elemento_conjunto(C2, 'a')
vw.inserir_elemento_conjunto(C2, 'b')
vw.inserir_elemento_conjunto(C2, 'c')
vw.inserir_elemento_conjunto(C2, 'd')
```

- Chamada da função para exibição do conjunto e tamanho do conjunto em formato oficial.

```python
# EXIBIR ELEMENTOS DO CONJUNTO
print('\n Exibino elementos do conjunto')
vw.elementos_conjunto(C1)
vw.elementos_conjunto(C2)
print('\n Exibindo elementos dos conjuntos')
vw.tamanho_conjunto(C1)
vw.tamanho_conjunto(C2)
```

- As operações básicas entre os conjuntos e elementos têm uma redução significativa de código, visto que todas as verificações já estão implementadas em outras classes.

```python
# OPERAC¸OES ENTRE ELEMENTOS E CONJUNTOS ~
print('\n Verificando se um elemento pertence ao um conjunto')
vw.elemento_pertence('A', C1)
vw.elemento_pertence('x', C1)
print('\n Verificando subconjuntos')
vw.conjunto_subconjunto(C1, C2)
vw.conjunto_subconjunto(C2, C1)
print('\n Verificando conjuntos próprios')
vw.conjunto_proprio(C1, C2)
vw.conjunto_proprio(C2, C1)
```

- Semelhantes as operações básica, para as operações entre os conjuntos, também há muito menos códigos e as verificações e resultados são apresentados.

```python
# ALGEBRA DE CONJUNTOS 
print('\n #´Algebra de conjuntos')
print('\n União de Conjuntos')
vw.operacoes_conjuntos_uniao(C1, C2)
vw.operacoes_conjuntos_uniao(C2, C1)
print('\n Intersecção de Conjuntos')
vw.operacoes_conjuntos_interseccao(C1, C2)
vw.operacoes_conjuntos_interseccao(C1, universo)
vw.operacoes_conjuntos_interseccao(C2, universo)
print('\n Diferença de Conjuntos')
vw.diferenca_conjunto(C2, C1)
print('\n Conjunto das Partes')
vw.conjunto_partes(C2)
print('\n Complemento dos Conjunto')
vw.complemento_conjunto(C1, C2)
```