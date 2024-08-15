def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def listar_alunos_reprovados(alunos, reprovados):
    for matricula in reprovados:
        nome = alunos['nomes'][alunos['matricula'].index(matricula)]
        media_final = calcular_media(alunos['notas'][matricula])
        print(f'Aluno Reprovado: {nome} – Matrícula: {matricula} – Média Final: {media_final}')
