
print('Digite um número e descubra quais são os números')



num = int(input('Digite um número: '))

for i in range(num):
    result = num - (i + 1)
    print(f'{result}')
