# Interpolação Polinomial de Newton
# Este script implementa a interpolação polinomial de Newton
# usando diferenças divididas e plota o polinômio resultante.
# Geração dos gráficos passo a passo: grau 0, grau 1 e grau 2

import numpy as np
import matplotlib.pyplot as plt

# Cálculo das diferenças divididas (coeficientes de Newton)
def diferencas_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j-1:n-1]) / (x[j:n] - x[0:n-j])
    return coef

# Avaliação do polinômio de Newton
def newton_interpolador(x_data, coef, x_val):
    n = len(coef)
    p = coef[-1]
    for k in range(2, n+1):
        p = coef[-k] + (x_val - x_data[-k]) * p
    return p

# Polinômios parciais corrigidos
def P0(x_val):
    return np.full_like(x_val, coef[0], dtype=float)

def P1(x_val):
    return coef[0] + coef[1] * (x_val - x[0])

def P2(x_val):
    return coef[0] + coef[1] * (x_val - x[0]) + coef[2] * (x_val - x[0]) * (x_val - x[1])

# Pontos dados
x = np.array([1, 2, 3])
y = np.array([2, 3, 5])

# Coeficientes do polinômio
coef = diferencas_divididas(x, y)

# Geração de pontos para o gráfico
x_vals = np.linspace(min(x) - 0.5, max(x) + 0.5, 200)
y_vals = [newton_interpolador(x, coef, xi) for xi in x_vals]

y_P0 = P0(x_vals)
y_P1 = P1(x_vals)
y_P2 = P2(x_vals)

# Plot
plt.figure(figsize=(12, 8))

# Grau 0
plt.subplot(3, 1, 1)
plt.plot(x_vals, y_P0, label='Grau 0 (Constante)', color='green')
plt.plot(x, y, 'ro', label='Pontos dados')
plt.title('Interpolação Grau 0 - Constante')
plt.grid(True)
plt.legend()

# Grau 1
plt.subplot(3, 1, 2)
plt.plot(x_vals, y_P1, label='Grau 1 (Linear)', color='orange')
plt.plot(x, y, 'ro', label='Pontos dados')
plt.title('Interpolação Grau 1 - Linear')
plt.grid(True)
plt.legend()

# Grau 2
plt.subplot(3, 1, 3)
plt.plot(x_vals, y_P2, label='Grau 2 (Quadrático)', color='blue')
plt.plot(x, y, 'ro', label='Pontos dados')
plt.title('Interpolação Grau 2 - Quadrático (Final)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
