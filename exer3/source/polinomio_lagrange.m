function Pz = polinomio_lagrange(m, x, y, z)
  % Usa os primeiros m+1 pontos
  x = x(1:m+1);
  y = y(1:m+1);
  
  n = length(x);
  Pz = 0;

  for k = 1:n
    Lk = 1;
    for j = 1:n
      if j != k
        Lk = Lk * (z - x(j)) / (x(k) - x(j));
      end
    end
    Pz = Pz + y(k) * Lk;
  end
end
