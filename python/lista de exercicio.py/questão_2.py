print('\033[1;40mDescubra agora se o número é')
print('\033[1;32mPAR\033[0m \033[1;34mou\033[0m \033[1;31mIMPAR\033[0m')

num = int(input('Digite um número inteiro: '))

if num %2 == 0:
    print(f'O número \033[1;32m{num}\033[0m é \033[1;32mpar')
else:
    print(f'O número \033[1;31m{num}\033[0m é \033[1;31mimpar')
