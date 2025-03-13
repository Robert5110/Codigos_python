#sum = somar todoas os valores da lista (usar apenas com listas)
#len = serve para incluir itens de uma lista
#exemplo:

#notas = []

#media = sum(notas) / len(notas)

#exemplo mostra os elementos

frutas = ['laranja','maça','uva','pêssego']

print(f'O arry possui: {len(frutas)} elemenos')

#exeplo 2: tamanho da caracteres

x = 'Biomas do amazonas'

print(f'O Tamanho da string é: {len(x)}')


#exemplo 3: número minimo e maximo:

num = [2,5,7,10]

#min() retorna o menor elemento

print(f'O mínimo é: {min(num)}')

#max() retorna o maior valor

print(f'O maximo é : {max(num)}')

#exemplo 4: append:

num = [2,5,7,10]

num.append(11)

print(f'O append é: {num}')

#exemplo: extend

#insere mais de um elemento na lista

num = [5,7,10,112,]

num.extend([12,13,14])

print(f'A sequencia da lista é: {num}')

#exemplo 5: insert

#inseri um elemnto na posição em uma posição especifica

num = [2,5,7,10]
num.insert(0,1)

print(f'Um elemnto foi movido: {num}')

frutas = ['laranja','uva','pera']
frutas.insert(2,'maça')

print(f'Um elemnto foi movido: {frutas}')

#exemplo 6: remove

#remove um item especifico da lista

frutas = ['maça','laranja','uva']

frutas.remove('maça')
print(f'Um elemento foi removido: {frutas}')

#exemplo: 7 pop

frutas = ['maça','laranja','uva']

#POP () remove o ultimo elemnto

x = frutas.pop()

print(f'{x}: foi removida') #mostrar o elemento removido

frutas = ['maça','laranja','uva']

x = frutas.pop(1)

print(f'{x}: foi removida') #mostrar o elemento removido

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
    tarefa = input("Digite uma tarefa ou \033[1;31m'sair'\033[0m para encerrar: ")

    if tarefa.lower() == "sair":
        break
    else:
        lista.append(tarefa)
        print(f'Tarefa \033[1;32m{tarefa}\033[0m adicionada')

print('\033[1;36m--LISTA COMPLETA--\033[0m')

for i in range(len(lista)):
    print(f'\033[1;33m{i + 1}\033[0m-\033[1;32m{lista[i]}')


#TUPLAS

"""São sequências ordenadas e imutaveis de elementos. Isso sgnifica que,
uma vez criada, não pode ser modificado: não pode adicionar, remover e nem alterar. """

# exemplo 

tupla = (1,2,3 ,"Ola", True)

#Por que usar Tupla?

"""Para garantir que os dados adicionados não serão alterados.
Uma função pode retornar uma Tupla para fornecer vários resultados.   """

 #ex:
coordenadas = (10,20)

print(coordenadas[0])

#ex:

produto = ("Smartphone","Samsung", 1989.99)

print("Produto:", produto[0])
print("Produto:", produto[1])
print("Produto:", produto[2])

#DICIOANARIOS

""" São coleções de pares chave.valor não ordenados.
Cada chave de ser único e imutavel(como uma String, número ou uma Tupla)
e cada valor pode ser de qualquer tipo. """

#ex:
dicionario = {"nome":"Robert","Idade":16,"cidade":"Manaus","interesses":["jogar","ler"],"vigens":["manacapuru"]}

print(dicionario["nome"])

#adacionar chave.valor no Dicionario

dicionario["interesses"].append("viagens")
print(dicionario)