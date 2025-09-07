fprintf('Calcular a integral de 1/(x*ln(x)) de 2 a 5.\n\n');

% --- Parâmetros do Exercício 2 ---
a = 2;          % Limite inferior de integração
b = 5;          % Limite superior de integração
m = 6;          % Número de subintervalos
valor_exato = 0.84240; % Valor exato para comparação

% --- a) Regra do Trapézio (n=1) ---
n1 = 1;
integral_n1 = newton_cotes(a, b, n1, m, @f_1);
erro_n1 = valor_exato - integral_n1;
fprintf('a) Regra do Trapézio (n=%d): I = %f, Erro = %f\n', n1, integral_n1, erro_n1);

% --- b) Regra 1/3 de Simpson (n=2) ---
n2 = 2;
integral_n2 = newton_cotes(a, b, n2, m, @f_1);
erro_n2 = valor_exato - integral_n2;
fprintf('b) Regra 1/3 de Simpson (n=%d): I = %f, Erro = %f\n', n2, integral_n2, erro_n2);

% --- c) Regra 3/8 de Simpson (n=3) ---
n3 = 3;
integral_n3 = newton_cotes(a, b, n3, m, @f_1);
erro_n3 = valor_exato - integral_n3;
fprintf('c) Regra 3/8 de Simpson (n=%d): I = %f, Erro = %f\n', n3, integral_n3, erro_n3);

fprintf('------------------------------------------------------------\n');
fprintf('Calcular a integral de sin(x)/exp(x-1) de 0 a pi.\n\n');

% --- Parâmetros do Exercício 3 ---
a2 = 0;          % Limite inferior de integração 
b2 = pi;         % Limite superior de integração 
m2 = 12;         % Número de subintervalos 
valor_exato2 = 1.41787; % Valor exato para comparação 

% --- a) Regra do Trapézio (n=1) ---
integral_2a = newton_cotes(a2, b2, 1, m2, @f_2);
erro_2a = valor_exato2 - integral_2a;
fprintf('a) Regra do Trapézio (n=1): I = %f, Erro = %f\n', integral_2a, erro_2a);

% --- b) Regra 1/3 de Simpson (n=2) ---
integral_2b = newton_cotes(a2, b2, 2, m2, @f_2);
erro_2b = valor_exato2 - integral_2b;
fprintf('b) Regra 1/3 de Simpson (n=2): I = %f, Erro = %f\n', integral_2b, erro_2b);

% --- c) Regra 3/8 de Simpson (n=3) ---
integral_2c = newton_cotes(a2, b2, 3, m2, @f_2);
erro_2c = valor_exato2 - integral_2c;
fprintf('c) Regra 3/8 de Simpson (n=3): I = %f, Erro = %f\n\n', integral_2c, erro_2c);