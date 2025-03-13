

def nomes(nome):


    di1 = {"nome","n1","n2"}
    di2 = {"telefone"}
    di3 = {"email"}

for i in range(3):
    di1 = input(f'Digite o {i + 1}° nome: ')
    di2 = input(f'Digite o telefone do {di1}: ')
    di3 = input(f'Digite o Email do {di1}: ')


    print(di1,di2,di3)
    
nome = input('Digite o nome que deseja procurar: ')


print(nome)