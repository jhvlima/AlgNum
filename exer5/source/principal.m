Toler = 10^-10;
IterMax = 50;

a = 0;
b = 3;
x = (a + b) / 2;
[Raiz, Iter, Info] = bissecao(a, b, Toler, IterMax, @f_1);
%[Raiz, Iter, Info] = newton_raphson(x, Toler, IterMax, @f_1, @df_1);

%a = -3;
%b = 3;
%x = (a + b) / 2;
%[Raiz, Iter, Info] = bissecao(a, b, Toler, IterMax, @f_2);
%[Raiz, Iter, Info] = newton_raphson(x, Toler, IterMax, @f_2, @df_2);

%a = 0;
%b = 2;
%x = (a + b) / 2;
%[Raiz, Iter, Info] = bissecao(a, b, Toler, IterMax, @f_3);
%[Raiz, Iter, Info] = newton_raphson(x, Toler, IterMax, @f_3, @df_3);

fprintf("Raiz: %.12f\n", Raiz)
fprintf("Inter: %d\n", Iter)
fprintf("Info: %d\n", Info)
