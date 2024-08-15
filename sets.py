
set_inicial = {11, 12, 13, 14}
print("Conteúdo do set_inicial:", set_inicial)


set_inicial.add(15)
print("Conteúdo do set_inicial após adicionar 15:", set_inicial)


set_inicial.update({1, 2, 3, 4, 5})
print("Conteúdo do set_inicial após update:", set_inicial)


set_inicial.discard(13)
print("Conteúdo do set_inicial após remover 13:", set_inicial)


novo_set = set({20, 21, 23, 1, 2})
print("Conteúdo do novo_set:", novo_set)

uniao = set_inicial.union(novo_set)
print("União entre set_inicial e novo_set:", uniao)


intersecao = set_inicial.intersection(novo_set)
print("Interseção entre set_inicial e novo_set:", intersecao)


diferenca = set_inicial.difference(novo_set)
print("Diferença entre set_inicial e novo_set:", diferenca)


diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print("Diferença simétrica entre set_inicial e novo_set:", diferenca_simetrica)
