# --- Dados da Tabela (Exemplo 2) ---
x_pontos = [0.1, 0.6, 0.8]
y_pontos = [1.221, 3.320, 4.953]

# Ponto onde queremos calcular o valor do polinômio
x_para_calcular = 0.2

# Separando os pontos para maior clareza, como na fórmula
x0, x1, x2 = x_pontos, x_pontos[1], x_pontos[2]
y0, y1, y2 = y_pontos, y_pontos[1], y_pontos[2]

# --- Cálculo de cada termo da soma de Lagrange ---
# A fórmula de Lagrange é P(x) = y0*L0(x) + y1*L1(x) + y2*L2(x)

# Termo 1: y0 * L0(x)
# L0(x) = (x - x1)(x - x2) / (x0 - x1)(x0 - x2)
termo1 = y0 * ( (x_para_calcular - x1) * (x_para_calcular - x2) ) / ( (x0 - x1) * (x0 - x2) )

# Termo 2: y1 * L1(x)
# L1(x) = (x - x0)(x - x2) / (x1 - x0)(x1 - x2)
termo2 = y1 * ( (x_para_calcular - x0) * (x_para_calcular - x2) ) / ( (x1 - x0) * (x1 - x2) )

# Termo 3: y2 * L2(x)
# L2(x) = (x - x0)(x - x1) / (x2 - x0)(x2 - x1)
termo3 = y2 * ( (x_para_calcular - x0) * (x_para_calcular - x1) ) / ( (x2 - x0) * (x2 - x1) )

# --- Soma dos termos para obter o resultado final ---
# P2(x) = Termo 1 + Termo 2 + Termo 3
resultado_final = termo1 + termo2 + termo3

# --- Imprimir os resultados ---
print(f"Cálculo de P({x_para_calcular}):\n")
print(f"Termo 1 (associado a y0={y0}): {termo1:.6f}")
print(f"Termo 2 (associado a y1={y1}): {termo2:.6f}")
print(f"Termo 3 (associado a y2={y2}): {termo3:.6f}")
print("-" * 30)
print(f"O valor final de P({x_para_calcular}) é: {resultado_final:.4f}")
print(f"(O valor na imagem é 1.414)")