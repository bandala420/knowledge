sum_num(0,0).
sum_num(X,Y):-
    X>0,
    X1 is X-1,
    sum_num(X1,Y1),
    Y is X+Y1.