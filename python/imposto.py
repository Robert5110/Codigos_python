
print('\033[1;33mIMPOSTO DE RENDA\033[0m')
def imposto(salario):


    if salario <=1500:
        print("Não precisa pagar")
        return 0
    elif salario > 1500 and salario <=2500:
      
        return salario * 0.05
    elif salario > 2500 and salario <=3000:
       
        return salario * 0.10
    else:
      
        return salario * 0.15
salario = float(input('\033[1;32mDigite seu sálario: \033[0m'))    
print(f'\033[1;31mO total a pagar é: R$\033[0m {imposto(salario):.2f}')