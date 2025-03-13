import random

nume = []


for _ in range(10):

    num = random.randint(1,100)
    print(num)
    nume.append(num)
    
print('\033[1;33mO maior número : ',max(nume))
print('\033[1;34mO menor número : ',min(nume))