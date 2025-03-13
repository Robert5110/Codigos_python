
escolha = int(input('\033[1;33mDigite quantas tarefas vai adicionar:\033[0m'))

lista = []
for i in  range(escolha):


    lista.append(input(f'Digite a { i + 1 }° tarefa: '))
   
print(f'\n{lista}') 

lista.insert(0,input('Digite qual é o item deprioridade: '))
print(lista)
