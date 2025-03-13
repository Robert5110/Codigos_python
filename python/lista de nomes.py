nome = []
telefone = []
lista = []

escolha = int(input('Digite quantos usuarios deseja adicionar: '))

for i in range(escolha):
    nome.append(input(f'Digite o nome do \033[1;33m{i + 1}°\033[0m usuario: '))

    telefone.append(int(input(f'Digite o telefone do \033[1;32m{nome[i]}: \033[0m')))

for i in range(escolha):
    tupla = (nome[i + 1], telefone[i + 1])
    lista.append(tupla)
lista.sort()    

for nome, telefone in lista:

    print(f'\033[1;32mNome: {nome}\033[0m\n\033[1;33mTelefone: {telefone}')








#nomes = ["Robert","Andre","Kauã"]
#telefone = [92999,92692,92777]

#print(f'Nomes dos usuarios: {nomes}')
#print(f'Telefone: {telefone}')
