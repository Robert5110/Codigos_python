
print('\t\033[1;10m*********************\033[0m')
print('\t\033[1;33m*CALCULADORA DE SOMA*\033[0m')
print('\t\033[1;10m*********************\033[0m\n')


escolha = (input('1-Somar\n2-Subtrair\n3-Multiplicação\n4-Divisão\n'))

if escolha == 1 or 'somar'or 'Somar':

    def soma (a, b):
        resultado = a + b
        return resultado

a = int(input('Digite o 1° números: '))
b = int(input('Digite o 2° números: '))

x = soma(a, b) 
print(a,'+',b,'=', x )


def subtrair (a, b):
        resultado = a - b
        return resultado


x = (a, b) 
print(a,'-',b,'=', x )

def subtrair (a, b):
        resultado = a - b
        return resultado


x = subtrair(a, b) 
print(a,'-',b,'=', x )

def subtrair (a, b):
        resultado = a - b
        return resultado


x = subtrair(a, b) 
print(a,'-',b,'=', x )