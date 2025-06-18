function [x, Iter, Info] = gauss_seidel(n, A, b, Toler, IterMax)
    x = zeros(n, 1);       % chute inicial
    x_old = x;
    Info = 0;

    fprintf("Iter\tx1\t\tx2\t\tx3\t\tNormaRel\n");

    for Iter = 1:IterMax
        x_old = x;
        for i = 1:n
            soma = 0;
            for j = 1:n
                if j ~= i
                    soma = soma + A(i,j) * x(j); % usa os valores já atualizados
                end
            end
            x(i) = (b(i) - soma) / A(i,i);
        end

        norma = norm(x - x_old, inf) / (norm(x, inf) + eps);
        fprintf("%2d\t%f\t%f\t%f\t%.6f\n", Iter, x(1), x(2), x(3), norma);

        if norma < Toler
            return;
        end
    end

    Info = 1; % não convergiu
end
