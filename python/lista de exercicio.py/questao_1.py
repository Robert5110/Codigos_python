print('\t\033[1;33m|================|')
print('\t\033[1;32m|MEDIA DOS ALUNOS|')
print('\t\033[1;33m|================|\033[0m\n')




not1 = float(input('Digite a 1° nota: '))
not2 = float(input('Digite a 2° nota: '))
not3 = float(input('Digite a 3° nota: '))

media = (not1 + not2 + not3)/3

if media >=6:
    print(f'Nota do aluno: {media:.1f}\n\033[1;32O aluno esta aprovado!')
else:
    print(f'Nota do aluno: {media:.1f}\n\033[1;31mO aluno esta reprovado...')