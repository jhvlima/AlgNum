f = @(x) sin(x);
a = 0; b = pi;
n = 6; % deve ser par
x = linspace(a, b, n+1);
y = f(x);

% Aproximação por Simpson 1/3 composta
h = (b - a)/n;
I = (h/3) * (y(1) + 2*sum(y(3:2:end-1)) + 4*sum(y(2:2:end)) + y(end));
fprintf("Aproximação da integral (Simpson 1/3): %.6f\n", I);

% Visualização
xx = linspace(a, b, 1000);
yy = f(xx);
plot(xx, yy, 'b-', 'LineWidth', 2); hold on;
plot(x, y, 'ko-');

for i = 1:2:n-1
  xx_local = linspace(x(i), x(i+2), 100);
  % Interpolar parabólica com 3 pontos
  p = polyfit(x(i:i+2), y(i:i+2), 2);
  yy_local = polyval(p, xx_local);
  fill([xx_local fliplr(xx_local)], [yy_local zeros(1,length(yy_local))], 'g', 'FaceAlpha', 0.3);
end

title('Regra de Simpson 1/3');
xlabel('x'); ylabel('f(x)');
legend('f(x)', 'Pontos', 'Parábolas');
grid on;
