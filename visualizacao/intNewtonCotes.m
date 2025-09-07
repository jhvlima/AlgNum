
f = @(x) sin(x);
a = 0; b = pi;
n = 4; % grau do polinômio
x = linspace(a, b, n+1);
y = f(x);
h = (b - a) / n;

% Pesos para Newton-Cotes fechado
switch n
  case 1
    w = [1 1];            c = h/2;
  case 2
    w = [1 4 1];          c = h/3;
  case 3
    w = [1 3 3 1];        c = 3*h/8;
  case 4
    w = [7 32 12 32 7];   c = 2*h/45;
  otherwise
    error('n não suportado!');
end

I = c * sum(w .* y);
fprintf("Aproximação da integral (Newton-Cotes grau %d): %.6f\n", n, I);
