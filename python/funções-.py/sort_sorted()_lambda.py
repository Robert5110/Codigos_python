#sort
lista = [3,2,5,4,8]
lista.sort()
print(lista)

#sort reverse
lista = [3,2,5,4,8]
lista.sort(reverse = True)
print(lista)

#sorted()

nova_lista = sorted(lista)
print(nova_lista)

#lambda

dobro = lambda x: x * 2

print("O dobro é: ",dobro(5))

num = int(input("Digite um número: "))
dobro = lambda x:x * 2
resultado = dobro(num)

print("O dobro de ", num," é ",resultado)
