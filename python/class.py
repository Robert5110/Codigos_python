class Node:
    def __init__(self,dado):
        self.dado = dado
        self.proximo= None
        
        
    class ListaLigada:
        def __init__(self):
            self.head = None

        def append(self, dado):
            novo_no = Node(dado)
            if self.head is None:
                self.head = novo_no
                return
            ultimo_no = self.head
            while ultimo_no.proximo:
                ultimo_no = ultimo_no.proximo
            ultimo_no.proximo = novo_no
        def print_list(self):
            no_atual = self.head
            while no_atual:
                print(no_atual.dado, end = " ")
                no_atual = no_atual.proximo
if __name__ == '__main__':
    lista = ListaLigada()
    lista.append(7)
    lista.append(8)
    lista.append(9)
    lista.append(10)
    lista.print
    
        