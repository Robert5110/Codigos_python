#EXEMPLO 1: random
import random

#gera 5 números aleatórios

for _ in range(5):
    numero = random.randint(1,10)
    print(f'{numero:.0f}')

#EXEMPLO 2: random com randint()

#gera números aleatórios com inicio e fim

num = random.randint(1,34)
print('O número aleatório: ', num)


#EXEMPLO 3: random com choice()

alunos = ["Robert","Kauã","Pedro","Marcelo","Marcus"]

aluno_esc = random.choice(alunos)
print('O aluno(a) escolhido foi: ',aluno_esc)