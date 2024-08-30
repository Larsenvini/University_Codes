% Define animals
animal(urso).
animal(peixe).
animal(peixinho).
animal(guaxinim).
animal(raposa).
animal(coelho).
animal(veado).
animal(lince).

% Define plants
planta(alga).
planta(grama).

% Define what each animal eats
come(urso, peixe).
come(peixe, peixinho).
come(peixe, alga).
come(peixinho, alga).
come(guaxinim, peixe).
come(urso, guaxinim).
come(urso, raposa).
come(raposa, coelho).
come(coelho, grama).
come(urso, veado).
come(veado, grama).
come(lince, veado).

% Define herbivore as an animal that eats only plants
herbivoro(X) :-
    forall(come(X, Y), planta(Y)).
