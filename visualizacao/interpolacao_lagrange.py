import numpy as np
import matplotlib.pyplot as plt

# --- Dados da Tabela (Exemplo 2 da sua foto) ---
x_pontos = np.array([0.1, 0.6, 0.8])
y_pontos = np.array([1.221, 3.320, 4.953])

# Ponto onde queremos calcular o valor
x_para_calcular = 0.2

# --- Funções para os Polinômios de Base L(x) ---
# CORREÇÃO: O denominador agora usa o elemento escalar correto (ex: x_pontos)
def L0(x):
    return ((x - x_pontos[1]) * (x - x_pontos[2])) / ((x_pontos - x_pontos[1]) * (x_pontos - x_pontos[2]))

def L1(x):
    return ((x - x_pontos) * (x - x_pontos[2])) / ((x_pontos[1] - x_pontos) * (x_pontos[1] - x_pontos[2]))

def L2(x):
    return ((x - x_pontos) * (x - x_pontos[1])) / ((x_pontos[2] - x_pontos) * (x_pontos[2] - x_pontos[1]))

# --- Função para o Polinômio de Lagrange Final P(x) ---
# Esta função combina os polinômios de base com os valores y corretos
def P2(x):
    return y_pontos * L0(x) + y_pontos[1] * L1(x) + y_pontos[2] * L2(x)

# Calcula o valor no ponto específico para verificação
valor_calculado = P2(x_para_calcular)
print(f"O valor calculado de P({x_para_calcular}) é: {valor_calculado:.4f}")

# --- Geração dos Gráficos ---
# Cria um intervalo suave de x para desenhar as curvas
x_range = np.linspace(0, 0.9, 400)

# Gráfico 1: O Resultado Final
plt.figure(figsize=(10, 6))
plt.plot(x_range, P2(x_range), 'b-', label='Polinômio de Lagrange P₂(x)')
plt.plot(x_pontos, y_pontos, 'ro', markersize=10, label='Pontos Originais da Tabela')
plt.plot(x_para_calcular, valor_calculado, 'g*', markersize=15, label=f'Ponto Interpolado P({x_para_calcular}) = {valor_calculado:.3f}')
plt.title('Gráfico 1: Interpolação de Lagrange - Resultado Final', fontsize=16)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()

# Gráfico 2: Como a "Mágica" Acontece (Polinômios de Base)
plt.figure(figsize=(10, 6))
plt.plot(x_range, L0(x_range), 'c--', label='L₀(x) - "Interruptor" para o Ponto 1')
plt.plot(x_range, L1(x_range), 'm--', label='L₁(x) - "Interruptor" para o Ponto 2')
plt.plot(x_range, L2(x_range), 'y--', label='L₂(x) - "Interruptor" para o Ponto 3')
plt.plot(x_pontos, np.zeros_like(x_pontos), 'ko', markersize=5)
plt.plot(x_pontos, np.ones_like(x_pontos), 'ko', markersize=5)
plt.axhline(0, color='black', linewidth=0.5)
plt.axhline(1, color='black', linewidth=0.5, linestyle=':')
plt.title('Gráfico 2: Os Polinômios de Base ("Interruptores")', fontsize=16)
plt.xlabel('x')
plt.ylabel('Valor do Polinômio de Base')
plt.grid(True)
plt.legend()
plt.show()