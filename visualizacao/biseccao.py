import numpy as np
import matplotlib.pyplot as plt

# Define a função para a qual queremos encontrar a raiz
def f(x):
    return 1/x - 0.5

# Configurações iniciais do método da bisseção
a = 1.0  # Início do intervalo
b = 4.0  # Fim do intervalo
n_iteracoes = 3 # Número de aproximações a serem calculadas

# Cria os dados para plotar a curva da função
x = np.linspace(0.5, 5, 400)
y = f(x)

# Inicia o gráfico
plt.figure(figsize=(12, 8))
plt.plot(x, y, label=r'$f(x) = \frac{1}{x} - \frac{1}{2}$', color='blue', zorder=1)
plt.axhline(0, color='black', linewidth=0.5) # Eixo x
plt.title('Visualização do Método da Bisseção')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Loop para as iterações do método da bisseção
colors = ['red', 'green', 'purple']
for i in range(n_iteracoes):
    c = (a + b) / 2 # Calcula o ponto médio (aproximação)
    
    # Adiciona elementos gráficos para a iteração atual
    plt.axvline(a, color=colors[i], linestyle='--', alpha=0.7, label=f'Intervalo {i+1}: [{a:.2f}, {b:.2f}]')
    plt.axvline(b, color=colors[i], linestyle='--', alpha=0.7)
    plt.plot(c, 0, 'o', color=colors[i], markersize=8, zorder=2)
    plt.text(c, -0.05, f'$x_{i+1}={c:.3f}$', ha='center', color=colors[i], fontsize=12)

    # Atualiza o intervalo para a próxima iteração
    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

plt.legend()
plt.savefig('bisection_method.png')