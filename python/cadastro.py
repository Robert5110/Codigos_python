

usuarios = []
       
def cadastrar_usuarios():
    nome = input('Digite o seu nome de usuário: ')
    cpf = input('Digite o seu CPF: ')
    email = input('Digite o seu e-mail: ')
    senha = input('Insira uma senha: ')
    usuario = {'nome': nome , 'cpf': cpf, 'email': email, 'senha': senha}
    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!\n")

def login():
    print('\033[1;33m---------- TELA DE LOGIN ----------\033[0m')
    email = input('E-mail: ')
    senha = input('Senha: ')
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print('\n\033[1;32mBem-vindo ao sistema!\033[0m\n')
            return True

        
    print('Usuário ou senha incorretos.\n')
    return False
    
            
def listar_usuarios():
    if not usuarios:
        print("Não há usuários cadastrados!")
    else:
        for usuario in usuarios:
            print(f'Nome: {usuario['nome']}\nCPF: {usuario['cpf']}')

def buscar_usuario():
    nome = input('Digite o nome do usuário que deseja buscar: ')
    for usuario in usuarios:
        if usuario["nome"] == nome:
            print(f'{usuario["nome"]}\n',)
            print(f'{usuario["cpf"]}\n',)
            print(f'{usuario["email"]}\n')

def remover_usuario():
    nome = input('Digite o nome do usuário que deseja remover: ')
    for i, usuario in enumerate(usuarios):
        if usuario["nome"] == nome:
            usuarios.pop(i)
            print("Usuário removido com sucesso!")
        else:
            print("Usuário não encontrado!")


cadastro_ = int(input('Deseja criar um cadastro?\n1-Sim\n2-Não\n'))
if cadastro_ == 1:
    cadastrar_usuarios()
    login()
        
    

print("\033[1;33m--------- SISTEMA DE USUÁRIOS ---------\033[0m\n")

while True:
    print('Escolha uma opção:\n1. Adicionar usuário\n2. Listar usuários existentes')
    opcao = int(input('3. Remover um usuário\n4. Busca por nome de usuário\n5. Entrar no sistema\n6. Sair\n'))


    match opcao:
        case '1':
            cadastrar_usuarios()

        case '2':
            print("\033[1;32m------- USUÁRIOS CADASTRADOS -------\033[0m\n")
            listar_usuarios()
        case '3':
            remover_usuario()

        case '4':
            buscar_usuario()

        case '5':
            login()

        case '6':
            print('Você escolheu sair.')
            break

        case _:
            print("\033[1;31mOpção inválida. Tente novamente!\033[0m")
