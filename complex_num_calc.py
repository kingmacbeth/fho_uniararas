import numpy as np

re1 = int(input("digite o numero real do primeiro complexo "))
im1 = int(input("digite o numero imaginario do primeiro complexo "))

z1 = complex(re1, im1)

print("[1] conjugado\n[2] z1 + z2\n[3] z1 - z2\n[4] z1 * z2\n[5] z1 / z2")

escolha = input("digite o que vc quer fazer: ")

if escolha == "1":
    conjugado = np.conj(z1)
    print("o conjugado é", conjugado)

elif escolha == "2":
    re2 = int(input("digite o numero real do segundo complexo "))
    im2 = int(input("digite o numero imaginario do segundo complexo "))

    z2 = complex(re2, im2)

    soma = z1 + z2
    print("a soma dos complexos é", soma)


elif escolha == "3":
    re2 = int(input("digite o numero real do segundo complexo "))
    im2 = int(input("digite o numero imaginario do segundo complexo "))

    z2 = complex(re2, im2)

    sub = z1 - z2
    print("a subtraçao dos complexos é", sub)

elif escolha == "4":
    re2 = int(input("digite o numero real do segundo complexo "))
    im2 = int(input("digite o numero imaginario do segundo complexo "))

    z2 = complex(re2, im2)
    mult = z1 * z2

    print("a multiplicação dos complexos é", mult)

elif escolha == "5":
    re2 = int(input("digite o numero real do segundo complexo "))
    im2 = int(input("digite o numero imaginario do segundo complexo "))

    z2 = complex(re2, im2)
    div = z1 / z2

    print("a divisão dos complexos é", div)