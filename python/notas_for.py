notas = []
escolha = int(input('Digite quantas avaliações você deseja: '))
for i in range(escolha):
    nota = float(input(f'Digite a {i + 1}° nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)

if media > 6:
    print(f'A nota do aluno foi {media:.1f} !')
    print('\033[1;32mFoi aprovado!\033[0m')
elif media >= 5 and media < 6:
    print(f'A nota do aluno foi {media:.1f} \n\033[1;33mEsta em recuperação\033[0m')
else:
    print(f'A nota do aluno foi {media:.1f} \n\033[1;31mFoi reprovado...\033[0m')
