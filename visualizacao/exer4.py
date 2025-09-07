# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# --- Funções para o Polinômio de Newton (do seu código) ---

def newton_divided_diff(x, y):
    """Calcula os coeficientes das diferenças divididas de Newton."""
    n = len(x)
    # Copia o array y para não modificar o original
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:] = (coef[j:] - coef[j-1:-1]) / (x[j:] - x[:n-j])
    return coef

def newton_poly(x_eval, x_nodes, coef):
    """Avalia o polinômio de Newton para um conjunto de pontos."""
    n = len(coef)
    # Inicia o polinômio com o primeiro coeficiente
    p = np.full_like(x_eval, coef[0], dtype=float)
    term_prod = np.ones_like(x_eval, dtype=float)
    for i in range(1, n):
        term_prod *= (x_eval - x_nodes[i-1])
        p += coef[i] * term_prod
    return p

# --- Função principal para gerar cada gráfico ---

def plotar_aproximacao_newton(func, a, b, n, titulo_grafico, nome_arquivo):
    """
    Plota a função original, os pontos de interpolação e o polinômio de Newton.

    Args:
        func: A função matemática a ser plotada (ex: f1).
        a, b: Limites do intervalo de integração.
        n: Grau do polinômio de Newton-Cotes.
        titulo_grafico: Título para o gráfico.
        nome_arquivo: Nome do arquivo para salvar a imagem.
    """
    # 1. Gerar os pontos de interpolação (nós)
    x_nodes = np.linspace(a, b, n + 1)
    y_nodes = func(x_nodes)

    # 2. Calcular os coeficientes do polinômio de Newton
    coef = newton_divided_diff(x_nodes, y_nodes)

    # 3. Gerar pontos para uma curva suave para plotagem
    x_vals = np.linspace(a, b, 400)
    y_true = func(x_vals)
    y_interp = newton_poly(x_vals, x_nodes, coef)

    # 4. Plotagem
    plt.figure(figsize=(10, 6))
    # Plota a função real
    plt.plot(x_vals, y_true, 'b-', label='Função Real f(x)', linewidth=2.5)
    # Plota o polinômio de aproximação
    plt.plot(x_vals, y_interp, 'g--', label=f'Polinômio de Aproximação (Grau {n})', linewidth=2)
    # Plota os pontos (nós) que definem o polinômio
    plt.plot(x_nodes, y_nodes, 'ro', markersize=8, label=f'{n+1} Pontos de Interpolação')
    
    # Preenche a área sob a curva do polinômio (a integral aproximada)
    plt.fill_between(x_vals, y_interp, alpha=0.2, color='green', label='Área da Integral Aproximada')

    plt.title(titulo_grafico)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5) # Eixo x
    plt.tight_layout()
    
    # Salva o gráfico em um arquivo
    plt.savefig(nome_arquivo)
    plt.clf() # Limpa a figura para o próximo gráfico

# --- Definição das Funções dos Exercícios ---

def f1(x):
    # CORREÇÃO: A função deve usar np.log e retornar o valor
    return 1 / (x * np.log(x))

def f2(x):
    return np.sin(x) / np.exp(x - 1)


# --- Execução: Gerar os dois gráficos separadamente ---

# Parâmetros para o Exercício 1
n_ex1 = 3 # Grau 3 (Regra 3/8 de Simpson) -> 4 pontos
a1, b1 = 2, 5
plotar_aproximacao_newton(f1, a1, b1, n_ex1,
                          'Aproximação de Newton para $f(x) = \\frac{1}{x \\ln(x)}$',
                          'grafico_newton_f1.png')

# Parâmetros para o Exercício 2
n_ex2 = 2 # Grau 2 (Regra 1/3 de Simpson) -> 3 pontos
a2, b2 = 0, np.pi
plotar_aproximacao_newton(f2, a2, b2, n_ex2,
                          'Aproximação de Newton para $f(x) = \\frac{\\sin(x)}{e^{x-1}}$',
                          'grafico_newton_f2.png')

print("Gráficos 'grafico_newton_f1.png' e 'grafico_newton_f2.png' gerados com sucesso.")