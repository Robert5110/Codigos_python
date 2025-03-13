def vefiricar_expressao(expressao):
    pilha = []
    abertuta = set("([{")
    fechamento = set(")]}")
    
    pares = set([('(',')'),('[',']'),('{','}')])
    
    for char in expressao:
        if char in abertuta:
            pilha.append(char)
            
        elif char in fechamento:
            if not pilha or (pilha.pop(),char) not in pares:
                return False
    return not pilha

exp1 = input(f'Digite o 1° conjuto: ')
exp2 = input(f'Digite o 2° conjuto: ')
exp3 = input(f'Digite o 3° conjuto: ')

print (vefiricar_expressao(exp1))
print (vefiricar_expressao(exp2))
print (vefiricar_expressao(exp3))

# obs: eu não entendi nada
