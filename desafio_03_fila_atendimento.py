import os
os.system("cls")

fila = []

while True:
    print("\nFila atual:", " -> ".join(fila) if fila else "[vazia]")

    entrada = input(
        "\nDigite o nome | 'atender' | 'fim': "
    ).strip().title()

    if entrada == "Fim":
        print("Encerrando sistema...")
        break

    elif entrada == "Atender":
        if fila:
            atendido = fila.pop(0)
            print(f"Aluno atendido: {atendido}")
        else:
            print("Fila vazia! Ninguém para atender.")

    else:
        fila.append(entrada)