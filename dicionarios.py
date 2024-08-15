
meuDicionario = {
    "codigo1": "Python",
    "codigo2": "Java",
    "codigo3": "PHP"
}

print("Conteúdo do dicionário:")
print(meuDicionario)

print("Tipo de dados do dicionário:")
print(type(meuDicionario))


print("Valor associado à chave 'codigo1':")
print(meuDicionario.get("codigo1"))


print("Tamanho do dicionário:")
print(len(meuDicionario))


dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}


print("Nome e tipo da chave 1:")
print("Nome:", dicionario_frutas[1]["nome"])
print("Tipo:", dicionario_frutas[1]["tipo"])

print("Nome e tipo da chave 2:")
print("Nome:", dicionario_frutas[2]["nome"])
print("Tipo:", dicionario_frutas[2]["tipo"])


print("Valores de todas as chaves 'nome' e 'tipo':")
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave}: Nome = {valor['nome']}, Tipo = {valor['tipo']}")
