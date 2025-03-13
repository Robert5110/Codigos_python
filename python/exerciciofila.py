import pilhanova
l = pilhanova.pilhanova()
print("digite 1 para inserir uma quantidade de livros da sua escolha:\n".capitalize())
print("digite 2 para remover um livro:\n".capitalize())
print("digite 3 para mostrar os livros disponiveis:\n".capitalize())
print("digite 4 para finalizar o programa:\n".capitalize())
opcao=0
while opcao!=4:
    opcao=int(input("digite uma opcao:".capitalize()))
    if opcao==1:
        n=int(input("digite a quantidade de livros para adicionar:".capitalize()))
        l.add(n)
    elif opcao==2:
        l.mostre()
    elif opcao==3:
        l.remov()
    else:
        print("PROGRAMA FINALIZADO!")

    

