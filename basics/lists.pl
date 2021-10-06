% predicado que cuente el número de elementos que tiene una lista
cuenta([],0).
cuenta([_|T],X):-
    cuenta(T,X1),
    X is X1+1.

% predicado que obtenga el i-ésimo elemento de la sucesión de Fibonacci
fib(0,0):- !.
fib(1,1):- !.
fib(N,X):-
    N1 is N-1,
    N2 is N-2,
    fib(N1,X1),
    fib(N2,X2),
    X is X1+X2.

% predicado que obtiene la n-ésima fila del triángulo de Pascal
pascal_next([X],[X]).
pascal_next([H,H2|T],[A|B]):-
    pascal_next([H2|T],B),
    A is H + H2.

pascal(0,[1]).
pascal(1,[1,1]).
pascal(N,X) :-
    N1 is N-1,
    pascal(N1, R1),
    pascal_next([0|R1],X).

% predicado que cuente el número de veces que un elemento aparece en una lista
cuenta(_,[],0).
cuenta(E,[E|T],X):-
    cuenta(E,T,X1),
    X is X1+1.
cuenta(E,[_|T],X):-
    cuenta(E,T,X).

% predicado que elimine todas las apariciones de un elemento en una lista
elimina(_,[],[]).
elimina(E,[E|T],X):-
    elimina(E,T,X), !.
elimina(E,[H|T],[H|X]):-
    elimina(E,T,X).

% predicado que elimine todos los elementos repetidos de una lista
eliminarepNative(L,X):- sort(L,X).

eliminarep([],[]).
eliminarep([H|T],[H|T1]):- 
    elimina(H,T,T2),
    eliminarep(T2,T1),!.

% predicado que determine si una lista de letras es una palabra palı́ndroma
isLetter([]).
isLetter([H|T]):- is_alpha(H),isLetter(T).
palindroma(X):-
    isLetter(X),
    reverse(X,X).

% predicado que a partir de una lista atributo-valor, cuyo formato es [ a1=>v1 , a2=>v2 ,... , aN=>vN ], obtenga el valor de un atributo que se le pida
:- op(1050,xfy,=>).
valor(K,[K=>X],X).
valor(K,[A=>B|T],X):-
    (K=A),
    valor(K,[K=>B],X);
    valor(K,T,X),!.