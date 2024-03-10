from colorama import init, Fore

# Inicializa o colorama para sistemas Windows
init()

def criar_nova_senha():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 1:              ||")
    print(" ||                                              ||")
    print(" ||      - Uma senha segura deve conter:         ||")
    print(" ||           -- Letra maiúscula                 ||")
    print(" ||           -- Letra minúscula                 ||")
    print(" ||           -- números                         ||")
    print(" ||           -- Simbolos (@#$%¨&*)              ||")
    print(" ||                                              ||")
    print(" ==================================================")
    password = input('Digite sua senha com base nos requisitos: ')

    # Verifica o comprimento da senha
    if len(password) < 8:
        print('1 - Sua senha deve conter mais de 8 caracteres!')

    # Verifica se a senha contém letras maiúsculas
    if not any(char.isupper() for char in password):
        print('2 - Sua senha deve conter pelo menos uma letra maiúscula!')

    # Verifica se a senha contém letras minúsculas
    if not any(char.islower() for char in password):
        print('3 - Sua senha deve conter pelo menos uma letra minúscula!')

    # Verifica se a senha contém números
    if not any(char.isdigit() for char in password):
        print('4 - Sua senha deve conter pelo menos um número!')

    # Verifica se a senha contém símbolos
    if not any(char in '@#$%¨&*' for char in password):
        print('5 - 1Sua senha deve conter pelo menos um símbolo (@#$%¨&*)!')
 

def tratar_senha_fraca():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 2:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||      -- iremos retornar uma senha mais forte ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")

def verifica_senha_segura():
    print(" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 3:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||    -- Verificamos se a senha é segura ou não ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")


 

#  ||||||| MENU |||||||


def menu():
    print(" =================================================")
    print(" ||                                             ||")
    print(" ||   Selecione uma opção:                      ||")
    print(" ||                                             ||")
    print(" ||   1. Criar Nova Senha                       ||")
    print(" ||   2. Tratar senha fraca deixando mais forte ||")
    print(" ||   3. Verifica se a senha é segura ou não    ||")
    print(" ||   0. Sair                                   ||")
    print(" ||                                             ||")
    print(" =================================================")

    while True:
        print(" =================================================")
        print(" ||                                             ||")
        print(" ||   Selecione uma opção:                      ||")
        print(" ||                                             ||")
        print(" ||   1. Criar Nova Senha                       ||")
        print(" ||   2. Tratar senha fraca deixando mais forte ||")
        print(" ||   3. Verifica se a senha é segura ou não    ||")
        print(" ||   0. Sair                                   ||")
        print(" ||                                             ||")
        print(" =================================================")
        escolha = input("Digite o número da opção desejada: ")


        if escolha == "1":
            criar_nova_senha()
        elif escolha == "2":
            tratar_senha_fraca()
        elif escolha == "3":
            verifica_senha_segura()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções listadas.")

#  ||||||| PROJETO MAIN |||||||

if __name__ == "__main__":
    menu()
1