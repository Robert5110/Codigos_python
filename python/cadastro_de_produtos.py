produtos = []
def adicionar_produto(nome,preco,quantidade):
    produto={"nome":nome,"preco":preco,"quantidade":quantidade}
    produtos.append(produto)
    print("produto adicionado com sucesso!!")

def listar_produtos():
    if not produtos:
        print("Não ha produtos cadastrados!")
    else:
        for produto in produtos:
            print(f"\n nome:{produto['nome']},\nPreço: R${produto['preco']},\nquantidade:{produto['quantidade']}")

def busca_produto(nome):
    for produto in produtos:
        if produto['nome']==nome:
            print(f"produto encontrado: \nnome: {nome}\npreço: R${preco}\nquantidade: {quantidade}")
            return
    print("Produto não encontrado")

def remov_produto():
    for i, produto in enumerate(produtos):
        if produto ["nome"]==nome:
            produtos.pop(i)
            print("produto removido com sucesso!")
            return
    print("Produto nao encontrado")

while True:
    print("\n---Sistema de cadastro de produtos---\n")
    print("\n 1.Adicionar\n 2.Listar\n 3.Buscar\n 4.Remove\n 5.Sair")
    Opção = int(input("Escolha uma opção: "))

    match Opção:
        case 1:
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço: "))
            quantidade = int(input("digite a quantidade: "))
            adicionar_produto(nome,preco,quantidade)
        case 2:
            listar_produtos()
        case 3:
            nome = input("Digite o nome do produto que deseja buscar: ")
            busca_produto(nome)
        case 4:
            nome = input("digite o nome do produto para remover: ")
            remov_produto(nome)
        case 5:
            break
        case _:
            print("Opção invalida.")