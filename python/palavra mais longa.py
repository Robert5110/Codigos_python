#soma = []

#escolha = int(input('Digite quantos números vai somar: '))

#for i in range(escolha):
 ####print('A soma de todos os números: ', soma)






def encontrar_string(string_long):
    return max(string_long, key = len)



    
lista = ["topp","Marcelo","naosei"]
resultado = encontrar_string(lista)
print("A string mais longa: ", resultado)


def encontrar_string2(string_longa):
    string_maior = " "
    for string in string_longa:
        if len(string) > len (string_maior):
            string_maior = string
    return string_maior


lista = ["Pedro", "carvalho","maninho"]
resultado = encontrar_string2(lista)
print("A string mais longa: ", resultado)

