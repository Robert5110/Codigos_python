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