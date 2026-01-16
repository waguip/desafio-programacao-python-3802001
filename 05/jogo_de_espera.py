def jogo_de_espera():
    import time
    import random

    tempo = random.randint(2, 4)
    print(f"Seu objetivo é de {tempo} segundos.")
    print("---Pressione Enter para começar---")
    input()
    inicio = time.time()
    print(f"...Pressione Enter de novo depois de {tempo} segundos")
    input()
    fim = time.time()
    duracao = fim - inicio
    print(f"Tempo decorrido: {duracao:.2f} segundos.")
    if duracao < tempo - 0.01:
        print(f"Muito rápido! Ainda tinha {tempo - duracao:.2f} segundos.")
    elif duracao > tempo + 0.01:
        print(f"Muito lento! {duracao - tempo:.2f} segundos a mais.")
    else:
        print("Acertou!")
