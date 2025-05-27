function [U, d, Info] = eliminacao_gauss_sem_pivotacao(n, A, b)
  U = A;
  d = b;
  Info = 0;

  for k = 1:n-1
    if abs(U(k, k)) < 1e-12
      Info = k; % detecta pivô zero
      return;
    endif
    for i = k+1:n
      m = U(i, k) / U(k, k);
      U(i, k:n) = U(i, k:n) - m * U(k, k:n);
      d(i) = d(i) - m * d(k);
    endfor
  endfor
endfunction
