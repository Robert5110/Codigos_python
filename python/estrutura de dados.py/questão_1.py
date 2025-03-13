
num = []

print('__Digite dez números aléatorios__\n')


for i in range(5):

    num1 = int(input(f'Digite o {i + 1}° número: '))
    num.append(num1)

print(f'O maximo é : \033[1;32m{max(num)}\033[0m')
print(f'O mínimo é:\033[1;31m {min(num)}')

print(num.count())