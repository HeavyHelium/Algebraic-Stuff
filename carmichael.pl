
len([], 0).
len([_ | T], N) :- len(T, N1), N is N1 + 1.


timesIn(P, N, 0) :- N mod P =\= 0.
timesIn(P, N, T) :- N mod P =:= 0, 
                    N1 is N div P, 
                    timesIn(P, N1, T1), 
                    T is T1 + 1. 

%prime 
prime1(N) :- N > 1,
             N1 is N - 1, 
             not((between(2, N1, X), 
                 N mod X =:= 0)).

clearNumber(N, P, R, T) :- timesIn(P, N, T),
                           T > 0,
                           R is N div (P ** T). 
clearNumber(N, P, P, 0) :- timesIn(P, N, T),
                           T =:= 0.


%primeFactors(N, Factors)
primeFactors(1, []).
primeFactors(N, [[P : Times] | T]) :- 
    N > 1, 
    between(2, N, P),
    prime1(P),
    N mod P =:= 0,
    P1 is P - 1,
    not((between(2, P1, X), 
         N mod X =:= 0)), 
    clearNumber(N, P, R, Times), 
    primeFactors(R, T).

squareFree(N) :- primeFactors(N, Factors), 
                 not((member([_ : Times], Factors), 
                      Times > 1)).

divCondCar(M) :- M > 1,
                 M1 is M - 1, 
                 primeFactors(M, Factors),
                 len(Factors, L),
                 L > 2, %at least 3 prime factors
                 not((member([P : _], Factors),
                      P1 is P - 1, 
                      M1 mod P1 =\= 0)).

nat(0). 
nat(N) :- nat(N1), N is N1 + 1.

carmichaelNumber(Number) :- squareFree(Number), 
                            divCondCar(Number).

genCarmichaelNumbers(N) :- nat(N),
                           carmichaelNumber(N).