from colorama import Fore, Style

# Lista dos níveis e situações do reservatório
niveis_agua = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Definindo a cor de cada nível de água
def definir_cor(nivel):
    if nivel == 1:
        cor = Fore.RED
    elif nivel == 2:
        cor = Fore.YELLOW
    elif nivel == 3:
        cor = Fore.GREEN
    elif nivel == 4:
        cor = Fore.CYAN
    elif nivel == 5:
        cor = Fore.BLUE
    else:
        cor = Fore.WHITE

    return cor

# Exibição dos níveis de água com cores e reset do terminal
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis_agua[nivel - 1]

    print(cor + "Nível " + str(nivel) + ": " + mensagem + Style.RESET_ALL)