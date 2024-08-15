# 1. Cria uma tupla chamada "primeira_tupla"
primeira_tupla = (1, 2, 3, 4, "Olá, tupla")

# 2. Imprime o conteúdo da tupla
print("Conteúdo da tupla:", primeira_tupla)

# 3. Utiliza o método "index" para encontrar o índice do elemento 4 e imprime o resultado
indice_elemento_4 = primeira_tupla.index(4)
print("Índice do elemento 4:", indice_elemento_4)

# 4. Verifica e imprime se a tupla contém o elemento 3
contém_elemento_3 = 3 in primeira_tupla
print("A tupla contém o elemento 3?", contém_elemento_3)

# 5. Verifica e imprime se a tupla contém o elemento 33
contém_elemento_33 = 33 in primeira_tupla
print("A tupla contém o elemento 33?", contém_elemento_33)
