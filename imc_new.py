sentinela = 1
import os

while sentinela == 1:
    seu_peso = float(input("Informe seu peso: "))
    altura = float(input("Informe sua altura"))

    IMC = seu_peso/altura*altura

    print("Seu IMC é: ", IMC)

    if IMC <= 18.5:
        print("Seu peso é normal")
    if IMC <= 25:
        print("Você está no peso ideal")
    if IMC <= 30.0:
        print("Você está acima do peso")
    if IMC <= 39.9:
        print("OBESIDADE II")
    if IMC >= 40:
        print("OBESIDADE III")

    print("Deseja continuar?")
    print("1 - Para sim")
    print("2 - Para não")
    sentinela = int(input("Informe a opção: "))