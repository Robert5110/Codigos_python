class pilhanova(object):
    def __init__(self):
        self.dados=[]
    def add(self,parametro):
        for i in range(parametro):
            self.dados.append(input("Insira um livro na biblioteca virtual:"))
    def remover(self,parametro2):
        self.dados.pop(0)
    def mostrar(self,parametro3):
        n=1
        for livro in range(self.dados):
            print(f"livro{n}-{livro}")
            n=n+1
    
    