#função sort() ORDEM CRESCENTE +

faturamento = float
lojas = ["Manaus","São Paulo","Porto Alegre"]
faturamento = [15000,30000,25000]

lojas.sort()
faturamento.sort()


print(f"Lojas: {lojas}\nFaturamento: {faturamento}\n")

#função sort(reverse = True) ORDEM DESCRECENTE -

lojas.sort(reverse = True)
faturamento.sort(reverse = True)

print(f'{lojas}\n{faturamento}\n')

lojas_fat = []

for i in range(3):
    tupla = (lojas[i - 1], faturamento[i - 1])
    lojas_fat.append(tupla)
lojas_fat.sort()    

print(f'{lojas_fat}\n')

print('\033[1;93m----lojas e Faturamento----\n\033[0m') 

for loja, faturamento in lojas_fat:
    print(f"\033[1;32mLoja:\033[0m \033[1;97m{loja}\033[0m\n\033[1;31mFaturamento\033[0m: \033[1;33mR${faturamento}")
