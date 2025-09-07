%n = 1;
%n = 2;
n = 3;

%a = 2;
%b = 5;
%m = 6;
%[Integral, Info] = newton_cotes(a, b, n, m, @f_1);

a = 0;
b = pi;
m = 12;
[Integral, Info] = newton_cotes(a, b, n, m, @f_2);

Integral
Info
