import random

numero_secreto = random.randrange(1,100) 


print("Qual é o nivel de dificuldade?")
print("(1)-Fácil (2)-Médio (3)-Difícil")

escolha = True
while(escolha):
    nivel = input("Defina o nível: ")
    nivel = int(nivel)
    
    if nivel > 3 or nivel < 1:
        print("Nivel inválido")
    else:
        escolha = False


if nivel == 1:
    total_de_tentativas = 10
elif nivel == 2:
    total_de_tentativas = 5
else:
    total_de_tentativas = 3        

for rodada in range(1, total_de_tentativas + 1):
    print("Total de tentativas {} de {}".format(rodada, total_de_tentativas))

    chute = input("Digite o seu numero: ")

    chute = int(chute)

    if (chute < 1 or chute > 100):
        print('O numero', chute, 'é inválido, você deve digitar um numero entre 1 e 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("voce acertou")
        break
    else:
        if(maior):
            print("O numero secreto é menor que o digitado")
        elif(menor):
            print("O numero secreto é maior que o digitado")


print("fim do jogo")