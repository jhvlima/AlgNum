import numpy as np
import matplotlib.pyplot as plt

# Função a ser integrada
def f(x):
    return -x*x*x

# Intervalo de integração
a, b = 0, np.pi

# PONTOS PARA REGRA 1/3 DE SIMPSON (n deve ser par)
n13 = 2
x13 = np.linspace(a, b, n13 + 1)
y13 = f(x13)

# PONTOS PARA REGRA 3/8 DE SIMPSON (n = 3 subintervalos -> 4 pontos)
n38 = 3
x38 = np.linspace(a, b, n38 + 1)
y38 = f(x38)

# Interpolação para visualização com polinômios
def interp_poly(x_nodes, y_nodes, x_eval):
    coef = np.polyfit(x_nodes, y_nodes, len(x_nodes) - 1)
    return np.polyval(coef, x_eval)

# Plot da função original
x_vals = np.linspace(a, b, 500)
y_true = f(x_vals)

plt.figure(figsize=(12, 6))

# ---- Simpson 1/3 ----
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_true, 'b-', label='f(x)', linewidth=2)
plt.plot(x13, y13, 'ko', label='Pontos 1/3')
for i in range(0, len(x13)-1, 2):
    x_local = np.linspace(x13[i], x13[i+2], 100)
    y_local = interp_poly(x13[i:i+3], y13[i:i+3], x_local)
    plt.fill_between(x_local, y_local, color='green', alpha=0.3)
plt.title("Regra de Simpson 1/3")
plt.xlabel("x"); plt.ylabel("f(x)")
plt.grid(True); plt.legend()

# ---- Simpson 3/8 ----
plt.subplot(1, 2, 2)
plt.plot(x_vals, y_true, 'b-', label='f(x)', linewidth=2)
plt.plot(x38, y38, 'ro', label='Pontos 3/8')
x_local = np.linspace(x38[0], x38[-1], 200)
y_local = interp_poly(x38, y38, x_local)
plt.fill_between(x_local, y_local, color='orange', alpha=0.3)
plt.title("Regra de Simpson 3/8")
plt.xlabel("x"); plt.ylabel("f(x)")
plt.grid(True); plt.legend()

plt.tight_layout()
plt.show()
