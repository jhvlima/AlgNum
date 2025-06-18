function Pz = polinomio_newton(m, x, y, z)
  % Usa os primeiros m+1 pontos
  x = x(1:m+1);
  y = y(1:m+1);

  n = length(x);
  a = y;

  % Diferenças divididas
  for j = 2:n
    for i = n:-1:j
      a(i) = (a(i) - a(i-1)) / (x(i) - x(i-j+1));
    end
  end

  % Avaliação do polinômio
  Pz = a(n);
  for k = n-1:-1:1
    Pz = a(k) + (z - x(k)) * Pz;
  end
end
