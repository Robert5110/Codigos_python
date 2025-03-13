compras = []

escolha = int(input('Digite quantas compras você fara: '))

for i in range(escolha):
    compras.append(input(f'{i+1}° compra: '))

print('\033[1;33m----lista de compras----\033[0m')

for i in range(escolha):

    print(f'\033[1;33m{i + 1}°\033[0m \033[1;32mCompra\033[0m: {compras[i]}')


remove = compras.pop()

print(f'O item {remove} foi removido\n')
print('\033[1;33m----lista de compras----\033[0m')

for i in range(len(compras)):

    print(f'\033[1;33m{i + 1}°\033[0m \033[1;32mCompra\033[0m: {compras[i]}')
