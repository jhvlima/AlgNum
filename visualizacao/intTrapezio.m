f = @(x) sin(x);
a = 0; b = pi;
n = 5;
x = linspace(a, b, n+1);
y = f(x);

% Aproximação pela regra do trapézio composta
h = (b - a) / n;
I = (h/2) * (y(1) + 2*sum(y(2:end-1)) + y(end));
fprintf("Aproximação da integral: %.6f\n", I);

% Visualização gráfica
xx = linspace(a, b, 1000);
yy = f(xx);
plot(xx, yy, 'b-', 'LineWidth', 2); hold on;

% Desenhar os trapézios
for i = 1:n
  fill([x(i) x(i) x(i+1) x(i+1)], [0 y(i) y(i+1) 0], 'r', 'FaceAlpha', 0.3);
end

plot(x, y, 'ko-');  % pontos usados
title('Regra do Trapézio');
xlabel('x'); ylabel('f(x)');
legend('f(x)', 'Trapézios');
grid on;
