import os 
os.system("cls")

votos=[]

while True:
    print('Candidatos : Leonardo Mendes, Enzo Bom e Vinicius Nazario')
    entrada_nomevoto=input('Informe o nome do aluno(a) que voce escolheu'
    'ou fim para sair e votar nulo: ').strip().title()

    if entrada_nomevoto == 'Fim':
        print('Programa encerrado')
        break
    if entrada_nomevoto in ['Leonardo Mendes','Enzo Bom','Vinicius Nazario']: 
        votos.append(entrada_nomevoto)
        os.system('cls')
        print('voto confirmado')
        print('\n')
    
    else:
        os.system('cls')
        print('candidato nao encontrado, tentar novamente !!!')

#contaçao de votos
Leonardo_Mendes=votos.count('Leonardo Mendes')
Enzo_Bom=votos.count('Enzo Bom')
Vinicius_Nazario=votos.count('Vinicius Nazario')

maxvotos=max(Leonardo_Mendes,Enzo_Bom,Vinicius_Nazario)


vencedores = []

if Leonardo_Mendes == maxvotos:
    vencedores.append("Leonardo Mendes")
if Enzo_Bom == maxvotos:
    vencedores.append("Enzo Bom")
if Vinicius_Nazario == maxvotos:
    vencedores.append("Vinicius Nazario")

if len(vencedores) == 1:
        print(f"Vencedor: {vencedores[0]}")
else:
    print("Empate entre:", ", ".join(vencedores))

print(f'Resultado do embate Leonardo={Leonardo_Mendes} , Enzo={Enzo_Bom} e Vinicius={Vinicius_Nazario}')