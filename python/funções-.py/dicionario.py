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
