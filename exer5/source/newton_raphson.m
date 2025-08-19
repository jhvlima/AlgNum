function [Raiz, Iter, Info] = newton_raphson(x, Toler, IterMax, f, df)
    for Iter = 1:IterMax
        fx = f(x);
        dfx = df(x);

        if abs(dfx) < eps
            Raiz = NaN;
            Info = -2; % Derivada muito próxima de zero
            return;
        end

        x_new = x - fx / dfx;

        if abs(x_new - x) < Toler
            Raiz = x_new;
            Info = 0; % Sucesso
            return;
        end

        x = x_new;
    end

    Raiz = x;
    Info = 1; % Iterações esgotadas sem convergência
end

