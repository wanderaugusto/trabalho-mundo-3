
dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

dicionario.update({2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'}})
dicionario.update({3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'argentina'}})

print("Dicionário atualizado:")
print(dicionario)


dicionario_copia = dicionario.copy()


print("\nDicionário cópia:")
print(dicionario_copia)


elemento_removido = dicionario.pop(2)


print("\nElemento removido com pop:")
print(elemento_removido)


print("\nDicionário após remoção com pop:")
print(dicionario)


ultimo_elemento = dicionario.popitem()


print("\nÚltimo elemento removido com popitem:")
print(ultimo_elemento)


print("\nDicionário após remoção com popitem:")
print(dicionario)


dicionario.clear()


dicionario_copia.clear()


print("\nDicionário após clear:")
print(dicionario)
print("Dicionário cópia após clear:")
print(dicionario_copia)


novas_chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(novas_chaves, 'valor_default')


print("\nNovo dicionário (items):")
print(novo_dicionario.items())


print("\nChaves do novo dicionário:")
print(novo_dicionario.keys())


print("\nValores do novo dicionário:")
print(novo_dicionario.values())
