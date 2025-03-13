#exemplo 8: lower(), upper() e count()

#lower() converter strings MAIÚSCULA para minusculas

palavra = input('Digite uma palavra MAIÚSCULA: ')
minuscula = palavra.lower()
print (minuscula)

banco_de_dados=["casa","boneca","maria","sol"]

pesquisa = input('Digite uma palavra: ')

if pesquisa.lower() in banco_de_dados:
    print(f'palavra \033[1;33m{pesquisa}\033[0m encontrada no banco de dados')

else:
    print('palavra não encontrada no banco de dados')



#upper() converter strings minuculas para maiusculas
palavra = input('Digite uma palavra minuscula: ')
maiuscula = palavra.upper()
print (maiuscula)

#count() conta caracteres especificas ou geral

a = input('Digite: ')

print(a.count("a"))

#exemplo de count

a = ["casa","casa","sol","boneca","casaco"]

print(a.count("casa"))

# exemplo  usando lower() e append()

lista = []

while True:
    tarefa = input("Digite uma \033[1;33mtarefa\033[0m ou \033[1;31m'sair'\033[0m para encerrar: ")

    if tarefa.lower() == "sair":
        break
    else:
        lista.append(tarefa)
        print(f'Tarefa \033[1;32m{tarefa}\033[0m adicionada')

print('\033[1;36m--LISTA COMPLETA--\033[0m')

for i in range(len(lista)):
    print(f'\033[1;33m{i + 1}\033[0m-\033[1;32m{lista[i]}')

