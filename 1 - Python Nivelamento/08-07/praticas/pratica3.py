candidatoA = 0
candidatoB = 0
votoBranco = 0
votoNulo = 0

while True:
    voto = int(input('Informe seu voto\n1 - Candidato A\n2 - Candidato B\n3 - Voto Branco\n4 - Voto Nulo\nOpção: '))
    print('\n')
    
    match voto:
        case 1:
            candidatoA += 1
        case 2:
            candidatoB += 1
        case 3:
            votoBranco += 1
        case 4:
            votoNulo += 1
        case _:
            print(f'Total de Votos\nCadidato A: {candidatoA}\nCandidato B: {candidatoB}\nVotos em Branco: {votoBranco}\nVotos Nulo: {votoNulo}\n')
            break