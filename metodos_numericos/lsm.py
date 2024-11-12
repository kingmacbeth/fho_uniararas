# %%
import numpy as np
import matplotlib.pyplot as plt

# Definicao dos Vetores X e Y
x = np.array([1.15, 2., 3.045, 4.])
y = np.array([4.01, 8.11, 10.2111, 12.0541])

# Vetores [X, Y] elevados, somas e quantidades
x_sqr = np.square(x)

# Soma
x_sum = np.sum(x)
x2_sum = np.sum(x_sqr)
y_sum = np.sum(y)

# Produto
xy_prod = x * y
xy_sum_prod = sum(xy_prod)

# Quantidade
n = len(x)

C = np.zeros((2, 2))
C = np.array([[x2_sum, x_sum], [x_sum, n]])

d = np.zeros((2, 1))
d = np.array([[xy_sum_prod], [y_sum]])

# Resolvendo o Sistema Linear C.z = d
z = np.linalg.solve(C, d)

# Coeficientes A e B
a = z[0][0]
b = z[1][0]

print(f"x = {x}")
print(f"a = {a}")
print(f"b = {b}")

# f(x) = a.x + b
f = (a * x) + b

print("*" * 25)
print("Função de melhor ajuste linear por meio do método dos quadrados mínimos.")
print(f"f(x) = a.x + b =>  {f}")
print("*" * 25)

# Definindo funcao para gerar o grafico


def f(x):
    return x**2+x+1


# Grafico da curva de funcao de ajuste com pontos tabelados
# %%
plt.title("Grafico de f(x) = x^2 + x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.scatter(x, y, color="red")

dom = np.linspace(0, 5)
imag = f(dom)

plt.plot(dom, imag)

# %%
