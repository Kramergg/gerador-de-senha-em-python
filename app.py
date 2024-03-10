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
    print(Color.MAGENTA+" =================================================")
    print(" ||             INSTRUÇÕES OPÇÃO 2:              ||")
    print(" ||                                              ||")
    print(" ||   - Você deve colocar sua senha existente:   ||")
    print(" ||      -- iremos retornar uma senha mais forte ||")
    print(" ||                                              ||")
    print(" ||                                              ||")
    print(" ==================================================")
    password = input( Color.BOLD +'Digite sua senha com base nos requisitos: ' + Color.END)
    

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