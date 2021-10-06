hombre(bart).
hombre(homero).
hombre(abraham).
hombre(herb).
hombre(clancy).
mujer(lisa).
mujer(maggie).
mujer(marge).
mujer(selma).
mujer(patty).
mujer(mona).
mujer(jackeline).
mujer(ling).
padre(bart,homero).
padre(lisa,homero).
padre(maggie,homero).
padre(homero,abraham).
padre(herb,abraham).
padre(marge,clancy).
padre(patty,clancy).
padre(selma,clancy).
madre(bart,marge).
madre(lisa,marge).
madre(maggie,marge).
madre(homero,mona).
madre(herb,mona).
madre(marge,jackeline).
madre(patty,jackeline).
madre(selma,jackeline).
madre(ling,selma).
%La interpretaci´on del predicado padre(X,Y) es Y es el padre de X.
%La interpretaci´on del predicado madre(X,Y) es Y es la madre de X.

% Y es abuelo(forzosamente varon) de X
abuelo(X,Y):-
    padre(X,Y1),
    hombre(Y),
    padre(Y1,Y).

% Y es abuela de X.
abuela(X,Y):-
    madre(X,Y1),
    mujer(Y),
    madre(Y1,Y).

% Y es nieto(forzosamente varon) de X
nieto(X,Y):-
    padre(Y1,X),
    hombre(Y1),
    padre(Y,Y1).

%  Y es nieta de X
nieta(X,Y):-
    madre(Y1,X),
    mujer(Y1),
    madre(Y,Y1).

% si Y es hermano(forzosamente varon) de X
hermano(X,Y):-
    padre(X,P),
    padre(Y,P),
    madre(X,M),
    madre(Y,M),
    hombre(Y),
    not(X=Y).
    
% Y es hermana de X
hermana(X,Y):-
    padre(X,P),
    padre(Y,P),
    madre(X,M),
    madre(Y,M),
    mujer(Y),
    not(X=Y).

% Y es herman@ de X
hermanos(X,Y):-
    padre(X,P),
    padre(Y,P),
    madre(X,M),
    madre(Y,M),
    not(X=Y).

% Y es tía de X
tia(X,Y):-
    padre(X,P),
    hermana(P,Y);
    madre(X,M),
    hermana(M,Y).

% Y es primo(forzosamente varon) de X
primo(X,Y):-
    (padre(X,P),hermanos(P,H);madre(X,M),hermanos(M,H)),padre(Y,H),hombre(Y);
    (padre(X,P),hermanos(P,H);madre(X,M),hermanos(M,H)),madre(Y,H),hombre(Y).

% Y es prima de X
prima(X,Y):-
    (padre(X,P),hermanos(P,H);madre(X,M),hermanos(M,H)),padre(Y,H),mujer(Y);
    (padre(X,P),hermanos(P,H);madre(X,M),hermanos(M,H)),madre(Y,H),mujer(Y).

% Y es sobrino(forzosamente varon) de X
sobrino(X,Y):-
    (hermanos(X,H),padre(Y,H);
    hermanos(X,H),madre(Y,H)),
    hombre(Y).

% Y es sobrina de X
sobrina(X,Y):-
    (hermanos(X,H),padre(Y,H);
    hermanos(X,H),madre(Y,H)),
    mujer(Y).

% X y Y han tenido por lo menos un hijo o hija en comun
pareja(X,Y):-
    (padre(H,X);
    madre(H,X)),
    (padre(H,Y);
    madre(H,Y)),
    not(X=Y).