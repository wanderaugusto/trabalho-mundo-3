from operacoes import calcular_media, verificar_reprovacao, listar_alunos_reprovados

alunos = {
    'nomes': ['maria', 'ana', 'joao', 'agatha', 'joaquim', 'felix'],
    'matricula': [26, 101, 13, 37, 72, 5],
    'notas': {
        26: [8, 7, 5, 9],
        101: [9, 9, 8, 9],
        13: [6, 5, 5, 5],
        37: [8, 6, 7.5, 9],
        72: [6, 5.5, 5, 7],
        5: [10, 8, 8, 8]
    }
}

reprovados = []

for matricula in alunos['matricula']:
    media = calcular_media(alunos['notas'][matricula])
    if verificar_reprovacao(media):
        reprovados.append(matricula)

listar_alunos_reprovados(alunos, reprovados)
