import random

numero_secreto = random.randrange(1,100) 
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