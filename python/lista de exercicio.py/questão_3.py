
print('\t\033[1;32mTABUADA DE \033[1;31mMULTIPLICAÇÃO\033[0m')

num = int(input('Digite um número: '))


for i in range(10):
    result =  num * (i + 1)

    print(f'|{num} x {i + 1}| = {result}')