function [Integral, Info] = newton_cotes(a, b, n, m, f)
    % h é a largura de cada um dos 'm' subintervalos
    h = (b - a) / m;
    Integral = 0;
    
    switch n
        case 1  % Regra do Trapézio
            w = [1 1];
            coef = h / 2;
        case 2  % Regra 1/3 de Simpson
            w = [1 4 1];
            coef = h / 6;
        case 3  % Regra 3/8 de Simpson
            w = [1 3 3 1];
            coef = h / 8;
        otherwise
            error('O grau n deve ser 1, 2 ou 3');
    endswitch

    % h_local é o passo dentro de um único intervalo de integração de Newton-Cotes
    h_local = h / n;

    for i = 0:(m-1)
        % x0 é o início do intervalo de integração atual
        x0 = a + i * h;
        
        % Gera os n+1 pontos para a regra de grau n dentro do intervalo de integração atual
        x_local = x0 + (0:n) * h_local;
        y_local = f(x_local);

        % Aplica a regra para o intervalo de integração atual e soma à integral total
        Integral = Integral + coef * dot(w, y_local);
    endfor

    Info.n = n;
    Info.m = m;
    Info.a = a;
    Info.b = b;
end