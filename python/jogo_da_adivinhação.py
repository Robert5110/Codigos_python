import random
acerto = []
escolha = int(input('Digite o nível da dificuldade:\n1-Facil\n2-Médio\n3-Difícl\n4-Impossivel!!\n'))

match (escolha):
    
    case 1:
        while True:
            acerto = random.randint(1,100)
            chute = int(input('Chute um número: '))
            if chute == acerto:
                print('Você acertou!')
                break
            elif chute > acerto:
                print('O número é menor')
            elif chute < acerto:
                print('O número é menor')
        
      

