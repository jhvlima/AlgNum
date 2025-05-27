function [U, d, Info] = eliminacao_gauss_com_pivotacao(n, A, b)
  U = A;
  d = b;
  Info = 0;

  for k = 1:n-1
    % Encontra o índice da maior magnitude na coluna k, das linhas k até n
    [~, p] = max(abs(U(k:n, k)));
    p = p + k - 1; % Ajusta o índice relativo para absoluto

    % Se o maior pivô for zero, o sistema é singular
    if abs(U(p, k)) < 1e-12
      Info = k;
      return;
    endif

    % Troca as linhas k e p em U e em d
    if p != k
      U([k p], :) = U([p k], :);
      d([k p]) = d([p k]);
    endif

    % Eliminação
    for i = k+1:n
      m = U(i, k) / U(k, k);
      U(i, k:n) = U(i, k:n) - m * U(k, k:n);
      d(i) = d(i) - m * d(k);
    endfor
  endfor
endfunction
