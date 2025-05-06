L = [4 0 0; -2 5 0; 1 7 3];
c = [-2; 5; 6];
n = size(L)(1);
L
c
n

x = substituicoes_sucessivas(n, L, c);
x

r = c - L * transpose(x);
r
