#Robert e Geovanni codigo.
#cadastra os produto da lanchonete
pratos = []

def adicionar():
    nome = input("Digite o nome do prato que deseja: ")
    ingredientes = input(f"Digite os ingredientes de {nome}(escreva com ','): ")
    preco = float(input(f"Digite o preço de {nome}: "))
    prato = {"nome":nome,"ingredientes":ingredientes,"preco":preco}
    pratos.append(prato)
    print("prato adicionado ao cardapio!")

def listar():
    if not pratos:
        print("Nenhum prato no cardapio.")
    for prato in pratos:
        print(f"\033[1;33mRefeição\033[0m: {prato['nome']}\n\033[1;32mIngredientes\033[0m: {prato['ingredientes']}\n\033[1;31mPreço: ${prato['preco']}\033[0m\n")

def remover():
    nome = input("Digite o prato que deseja remover: ")
    for i,prato in enumerate(pratos):
        if prato["nome"]==nome: 
            pratos.pop(i)
            print("prato removido com sucesso!\n")
    else:
        print(f"\033[1;31mPrato nao listado no caradapio...\033[0m\n")

def buscar():
    nome = input("Digite o prato que deseja buscar: ")
    for prato in pratos:
        if prato['nome']==nome:
            print(f"Refeição: {prato['nome']}\nIngredientes: {prato['ingredientes']}\nPreço: {prato['preco']}\n")    
    else:
        print(f"\033[1;31mPrato nao listado no caradapio...\033[0m\n")
print(f'\033[1;32mRestaurante Sabor Amazônico\033[0m\n')

while True:
    print("1 - Adicionar prato nó cardapio\n2 - Ver cardapio\n3 - Remover prato\n4 - Buscar prato\n5 - Relatorio\n6 - Sair\n")

    esc = int(input("Digite sua escolha: "))
    match esc:
        case 1:
            adicionar()
        case 2:
            listar()
        case 3:
            remover()
        case 4:
            buscar()
        case 5:
            print("Obv: Relatorio em Desenvolvimento")
        case 6:
            break
        case _:
            print("opçao invalida.")