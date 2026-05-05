import os
os.system("cls")

pilha = []

while True:
    print("\nTexto atual:", " ".join(pilha) if pilha else "[vazio]")
    
    entrada = input(
        "\nDigite uma palavra | 'desfazer' | 'fim': "
    ).strip().lower()

    if entrada == "fim":
        print("Encerrando editor...")
        break

    elif entrada == "desfazer":
        if pilha:  
            removido = pilha.pop()
            print(f"Última palavra removida: {removido}")
        else:
            print("Nada para desfazer! (pilha vazia)")

    else:
        pilha.append(entrada)