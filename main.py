import Conjunto
import View

# OBJETOS DE CONJUNTO
C1 = Conjunto.Conjunto()
C2 = Conjunto.Conjunto()

# OBJETOS DE VIEW
vw = View.View()

# CONJUNTO UNIVERSO
universo = vw.conjunto_universo()

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

# EXIBIR ELEMENTOS DO CONJUNTO
print('\n Exibino elementos do conjunto')
vw.elementos_conjunto(C1)
vw.elementos_conjunto(C2)

print('\n Exibindo elementos dos conjuntos')
vw.tamanho_conjunto(C1)
vw.tamanho_conjunto(C2)

# OPERAÇÕES ENTRE ELEMENTOS E CONJUNTOS
print('\n Verificando se um elemento pertence ao um conjunto')
vw.elemento_pertence('A', C1)
vw.elemento_pertence('x', C1)

print('\n Verificando subconjuntos')
vw.conjunto_subconjunto(C1, C2)
vw.conjunto_subconjunto(C2, C1)

print('\n Verificando conjuntos prórpios')
vw.conjunto_proprio(C1, C2)
vw.conjunto_proprio(C2, C1)

# ÁLGEBRA DE CONJUNTOS
print('\n #Álgebra de conjuntos')
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
