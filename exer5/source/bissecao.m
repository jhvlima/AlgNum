function [Raiz, Iter, Info] = bissecao(a, b, Toler, IterMax, f)
    fa = f(a);
    fb = f(b);

    if fa * fb > 0
        Raiz = NaN;
        Iter = 0;
        Info = -1; % Intervalo inválido
        return;
    end

    for Iter = 1:IterMax
        x = (a + b) / 2;
        fx = f(x);

        if abs(fx) < Toler && (b - a)/2 < Toler
            Raiz = x;
            Info = 0; % Sucesso
            return;
        end

        if fa * fx < 0
            b = x;
            fb = fx;
        else
            a = x;
            fa = fx;
        end
    end

    Raiz = (a + b) / 2;
    Info = 1; % Iterações esgotadas sem convergência
end

