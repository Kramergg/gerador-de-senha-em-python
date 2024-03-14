import random
import string
from colorama import init, Fore

#  ||||||| COLORAMA |||||||

# Inicializa o colorama para sistemas Windows
class Color:
    # Cores de texto
    RED = '\033[91m'  # Vermelho
    GREEN = '\033[92m'  # Verde
    YELLOW = '\033[93m'  # Amarelo
    BLUE = '\033[94m'  # Azul
    MAGENTA = '\033[95m'  # Magenta
    CYAN = '\033[96m'  # Ciano
    WHITE = '\033[97m'  # Branco

    # Formatação de texto
    BOLD = '\033[1m'  # Negrito
    UNDERLINE = '\033[4m'  # Sublinhado
    END = '\033[0m'  # Resetar formatação
init()

#  ||||||| FUNÇÕES |||||||

def criar_nova_senha():

    # Define os conjuntos de caracteres para cada tipo de caractere
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    # Combina todos os conjuntos de caracteres
    caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos

    # Gera uma senha aleatória com 12 caracteres
    senha = ''.join(random.sample(caracteres, 15))
    print(Color.BLUE + " =================================================")
    print(" ||                INFORMAÇÃO:                   ||")
    print(" ||                                              ||")
    print(" ||      - Uma senha segura deve conter:         ||")
    print(" ||           -- Letra maiúscula                 ||")
    print(" ||           -- Letra minúscula                 ||")
    print(" ||           -- Números                         ||")
    print(" ||           -- Símbolos (@#$%¨&*)              ||")
    print(" ||                                              ||")
    print(" =================================================="+ Color.END)

    print(Color.GREEN + " ==================================================")
    print(" ||                                              ||")
    print(" ||           SENHA GERADA COM SUCESSO!          ||")
    print(" ||                                              ||")
    print(" ||                 "+senha+"              ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" =================================================="+ Color.END)



def tratar_senha_fraca():
    print(Color.MAGENTA + " =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 2:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||      -- iremos retornar uma senha mais forte ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")
    password = input(Color.BOLD + 'Digite sua senha com base nos requisitos: ' + Color.END)

    # Define os conjuntos de caracteres para cada tipo de caractere
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    # Inicializa as variáveis para armazenar os caracteres faltantes
    faltantes = {'maiusculas': '', 'minusculas': '', 'numeros': '', 'simbolos': ''}

    # Verifica se a senha contém letras maiúsculas
    if not any(char.isupper() for char in password):
        faltantes['maiusculas'] = random.choice(letras_maiusculas)

    # Verifica se a senha contém letras minúsculas
    if not any(char.islower() for char in password):
        faltantes['minusculas'] = random.choice(letras_minusculas)

    # Verifica se a senha contém números
    if not any(char.isdigit() for char in password):
        faltantes['numeros'] = random.choice(numeros)

    # Verifica se a senha contém símbolos
    if not any(char in '@#$%¨&*' for char in password):
        faltantes['simbolos'] = random.choice(simbolos)

    # Combinar a senha antiga com os caracteres faltantes
    nova_senha = password + ''.join(faltantes.values())

    # Verifica se a senha tem menos de 15 caracteres
    if len(nova_senha) < 15:
        # Calcula quantos caracteres adicionais são necessários
        caracteres_faltantes = 15 - len(nova_senha)
        # Adiciona caracteres aleatórios até atingir o mínimo de 15 caracteres
        for _ in range(caracteres_faltantes):
            nova_senha += random.choice(string.ascii_letters + string.digits + '@#$%¨&*')

    print(Color.GREEN + " ==================================================")
    print(" ||                                              ||")
    print(" ||           SENHA TRATADA COM SUCESSO!          ||")
    print(" ||                                              ||")
    print(Color.BOLD + "               "+nova_senha+"               "+  Color.END)
    print(Color.GREEN + " ||                                              ||")
    print(" ||                                              ||")
    print(" =================================================="+ Color.END)




def verifica_senha_segura():
    print(Color.MAGENTA+" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 3:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||    -- Verificamos se a senha é segura ou não ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")
    password = input('Digite sua senha com base nos requisitos: ')

    # Define os conjuntos de caracteres para cada tipo de caractere
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = '@#$%¨&*'

    # Verifica se a senha contém pelo menos uma letra maiúscula
    if not any(char in letras_maiusculas for char in password):
        print(Color.RED + "A senha não contém letra maiúscula." + Color.RED)
        return

    # Verifica se a senha contém pelo menos uma letra minúscula
    if not any(char in letras_minusculas for char in password):
        print(Color.RED + "A senha não contém letra minúscula." + Color.RED)
        return

    # Verifica se a senha contém pelo menos um número
    if not any(char in numeros for char in password):
        print(Color.RED + "A senha não contém número." + Color.RED)
        return

    # Verifica se a senha contém pelo menos um símbolo
    if not any(char in simbolos for char in password):
        print(Color.RED + "A senha não contém símbolo." + Color.RED)
        return

    # Se a senha passou por todas as verificações, é considerada segura
    print(Color.GREEN + " ==================================================")
    print(" ||                                              ||")
    print(" ||                  SENHA SEGURA!               ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" =================================================="+ Color.END)

#  ||||||| MENU |||||||


def menu():


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
        escolha = input(Color.BOLD +"Digite o número da opção desejada: " + Color.END)


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