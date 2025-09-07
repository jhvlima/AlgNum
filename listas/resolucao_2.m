% Exercício 1 - Eliminação de Gauss (sem pivotação)

% Passo 1: Definição da matriz aumentada [A | b]
A = [-2 3 1;
      2 1 -4;
      7 10 -6];
b = [-5; -9; 2];

Ab = [A b];  % Matriz aumentada 3x4

disp('Matriz aumentada inicial:')
disp(Ab)

% Etapa 1: Eliminar elemento (2,1)
m21 = Ab(2,1) / Ab(1,1);  % multiplicador L21
Ab(2,:) = Ab(2,:) - m21 * Ab(1,:);

% Eliminar elemento (3,1)
m31 = Ab(3,1) / Ab(1,1);  % multiplicador L31
Ab(3,:) = Ab(3,:) - m31 * Ab(1,:);

disp('Após eliminação na primeira coluna:')
disp(Ab)

% Etapa 2: Eliminar elemento (3,2)
m32 = Ab(3,2) / Ab(2,2);  % multiplicador L32
Ab(3,:) = Ab(3,:) - m32 * Ab(2,:);

disp('Após eliminação na segunda coluna:')
disp(Ab)

% Agora temos uma matriz triangular superior
% Fazemos substituição regressiva
x = zeros(3,1);
x(3) = Ab(3,4) / Ab(3,3);
x(2) = (Ab(2,4) - Ab(2,3)*x(3)) / Ab(2,2);
x(1) = (Ab(1,4) - Ab(1,2)*x(2) - Ab(1,3)*x(3)) / Ab(1,1);

disp('Solução final do sistema:')
disp(x)

r = A*x - b


% Exercício 1 e 2
A1 = [-2 3 1; 2 1 -4; 7 10 -6];
b1 = [-5; -9; 2];
x1 = A1 \ b1
[L2, U2, P2] = lu(A1);
y2 = L2 \ (P2 * b1);
x2 = U2 \ y2

% Exercício 3 e 4
A3 = [4 -1 3; 1 6 2; 5 5 1];
b3 = [43; 7; 8];
[L3, U3, P3] = lu(A3);
y3 = L3 \ (P3 * b3);
x3 = U3 \ y3

% Exercício 5
A5 = [1 6 4; 2 -3 1; 5 5 8];
invA5 = inv(A5)

% Exercício 6 - Jacobi
A6 = [10 2 -3; 1 8 -1; 2 -1 -5];
b6 = [48; 4; -11];
x0 = b6 ./ diag(A6);
D = diag(diag(A6));
R = A6 - D;
x1 = inv(D) * (b6 - R * x0);
x2 = inv(D) * (b6 - R * x1);
norm_inf = norm(x2 - x1, inf) / norm(x2, inf)

% Exercício 7 - Gauss-Seidel
xgs0 = [0; 0; 0];
xgs1 = zeros(3,1);
xgs1(1) = (b6(1) - A6(1,2)*xgs0(2) - A6(1,3)*xgs0(3)) / A6(1,1);
xgs1(2) = (b6(2) - A6(2,1)*xgs1(1) - A6(2,3)*xgs0(3)) / A6(2,2);
xgs1(3) = (b6(3) - A6(3,1)*xgs1(1) - A6(3,2)*xgs1(2)) / A6(3,3);

xgs2 = zeros(3,1);
xgs2(1) = (b6(1) - A6(1,2)*xgs1(2) - A6(1,3)*xgs1(3)) / A6(1,1);
xgs2(2) = (b6(2) - A6(2,1)*xgs2(1) - A6(2,3)*xgs1(3)) / A6(2,2);
xgs2(3) = (b6(3) - A6(3,1)*xgs2(1) - A6(3,2)*xgs2(2)) / A6(3,3)
