import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos
x = np.array([0.2, 0.34, 0.4, 0.52, 0.6, 0.72])
y = np.array([0.16, 0.22, 0.27, 0.29, 0.32, 0.37])
z = 0.46

# Grau do polinômio desejado
m = 2  # Altere para 1, 2, 3...

# Função: diferenças divididas
def diferencas_divididas(x, y):
    n = len(x)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:-j])
    return coef

# Função: avalia polinômio de Newton
def newton_eval(coef, x_base, x_vals):
    n = len(coef)
    y_vals = np.zeros_like(x_vals)
    for i, z in enumerate(x_vals):
        val = coef[-1]
        for k in range(n-2, -1, -1):
            val = coef[k] + (z - x_base[k]) * val
        y_vals[i] = val
    return y_vals

# Seleciona os (m+1) pontos mais próximos de z
distancias = np.abs(x - z)
indices_ordenados = np.argsort(distancias)
indices_m = np.sort(indices_ordenados[:m+1])  # pontos usados na interpolação
x_m = x[indices_m]
y_m = y[indices_m]

# Coeficientes de Newton para interpolação
coef = diferencas_divididas(x_m, y_m)
Pz = newton_eval(coef, x_m, np.array([z]))[0]

# Estimativa do erro:
# Tenta usar m+2 pontos para calcular a diferença dividida de ordem (m+1)
erro_estimado = None
if m+2 <= len(x):
    indices_erro = np.sort(indices_ordenados[:m+2])
    x_erro = x[indices_erro]
    y_erro = y[indices_erro]
    coef_erro = diferencas_divididas(x_erro, y_erro)
    delta_ordem = abs(coef_erro[m+1])  # ordem m+1
    produto = np.prod([abs(z - xi) for xi in x_m])
    erro_estimado = delta_ordem * produto
else:
    erro_estimado = None

# Construção para o gráfico do polinômio
x_vals = np.linspace(min(x_m)-0.02, max(x_m)+0.02, 200)
y_vals = newton_eval(coef, x_m, x_vals)

# Gráfico
plt.figure(figsize=(8, 4))
plt.plot(x_vals, y_vals, 'b-', label=f'Polinômio de grau {m}')
plt.plot(x_m, y_m, 'ko', label='Pontos usados')
plt.plot(x, y, 'k.', alpha=0.3, label='Todos os dados')
plt.plot(z, Pz, 'ro', label=f'z = {z:.2f}\nP(z) ≈ {Pz:.4f}')

plt.title(f'Interpolação de Newton em z = {z} (grau {m})')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Exibição dos resultados
print(f'Valor interpolado em z = {z:.2f} com grau {m}: {Pz:.6f}')
if erro_estimado is not None:
    print(f'Estimativa do erro |E(z)| ≈ {erro_estimado:.6e}')
else:
    print('Não há pontos suficientes para estimar o erro de ordem m+1.')
