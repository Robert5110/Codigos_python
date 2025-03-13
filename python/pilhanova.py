class pilhanova(object):
    def __init__(self):
        self.dados=[]
    def add(self,parametro):
        for i in range(parametro):
            self.dados.append(input("Insira um livro na biblioteca virtual:"))
    def remov(self):
        self.dados.pop(-1)
    def mostre(self):
        n=1
        for i in self.dados:
            print(f"livro{n}-{i}")
            n=n+1
    
    
    