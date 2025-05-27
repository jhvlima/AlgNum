function x = substituicoes_retroativas(n, U, d)
  x = zeros(1, n);

  for i = n:-1:1
    soma = 0;
    for j = i+1:n
      soma = soma + U(i, j) * x(j);
    endfor
    x(i) = (d(i) - soma) / U(i, i);
  endfor
endfunction
