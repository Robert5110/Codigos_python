class pilha(object):
    def __init__(self):
        self.dados=[]
    def empilhar(self):
        self.dados.append(input("digite um numero:".capitalize()))
    def desempilha(self):
        self.dados.pop(-1)
    def prin (self):
        for x in self.dados:
            print(f"{x}")
