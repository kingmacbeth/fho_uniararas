import numpy as np

# EXERCÍCIO 1

# Definindo os valores das variáveis

h = 0.00001
x0 = 3.0


def f(x):
    funcao = 2 * x**3 + np.log(x) + np.cos(x)
    return funcao


funcao = f(x0)


def dfn(x):
    derivada = (f(x + h) - f(x)) / h
    return derivada


derivada = dfn(x0)

print("Exercício 1\n")
print(
    f"A derivada da função com a regra de diferenças finitas com h = 0.00001 é: {derivada}\n"
)

print("*" * 25)

# EXERCÍCIO 2

# Definindo os valores das variáveis
a = 4.0
b = 4.5
n = 5
h = (b - a) / n

y = np.linspace(a, b, n)

# Definindo a função


def f(x):
    funcao = 2 * x**3 + np.log(x) + np.cos(x)
    return funcao


soma = sum(f(y[1:4]))

result = (h / 2) * (f(y[0]) + 2 * soma + f(y[4]))

print("Exercício 2\n")
print(f"O resultado da integral numérica é: {result}")
