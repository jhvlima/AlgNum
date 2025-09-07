# Recarregar bibliotecas após reset
import numpy as np
import matplotlib.pyplot as plt

# Função de exemplo
def f(x):
    return (9*x*x*x*x + -x*x*x*8)

def f1(x):
    return 1 / (x * np.log(x))

def f2(x):
    return np.sin(x) / np.exp(x - 1)

# Pontos de interpolação (Newton-Cotes grau 4 -> 5 pontos)
a, b = 2, 5
n = 3
x_nodes = np.linspace(a, b, n + 1)
y_nodes = f1(x_nodes)

# Cálculo do polinômio de interpolação de Newton (diferenças divididas)
def newton_divided_diff(x, y):
    n = len(x)
    coef = np.copy(y)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:n-j])
    return coef

def newton_poly(x_eval, x, coef):
    n = len(coef)
    p = np.zeros_like(x_eval)
    for i in range(n):
        term = coef[i]
        for j in range(i):
            term *= (x_eval - x[j])
        p += term
    return p

# Calcular os coeficientes
coef = newton_divided_diff(x_nodes, y_nodes)

# Avaliar polinômio de Newton
x_vals = np.linspace(a, b, 50)
y_interp = newton_poly(x_vals, x_nodes, coef)
y_true = f1(x_vals)

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_true, 'b-', label='f(x)', linewidth=2)
plt.plot(x_vals, y_interp, 'g--', label='Polinômio de Newton', linewidth=2)
plt.plot(x_nodes, y_nodes, 'ro', label='Pontos de interpolação')
plt.fill_between(x_vals, y_interp, alpha=0.2, color='green', label='Área aproximada')
plt.title('Interpolação de Newton (grau n - Newton-Cotes)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
