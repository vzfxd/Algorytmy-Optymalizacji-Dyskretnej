set zmiany;
set dzielnice;
param min_radiowozy{p in dzielnice, z in zmiany};
param max_radiowozy{p in dzielnice, z in zmiany};
param zmiany_radiowozy{z in zmiany};
param dzielnice_radiowozy{p in dzielnice};


var wyslane_radiowozy{p in dzielnice, z in zmiany},>=0,integer;


minimize wyslane: sum{p in dzielnice} sum{z in zmiany} wyslane_radiowozy[p,z];


s.t. min_wyslane_zmiana {p in dzielnice,z in zmiany}: wyslane_radiowozy[p,z] >= min_radiowozy[p,z];
s.t. max_wyslane_zmiana {p in dzielnice,z in zmiany}: wyslane_radiowozy[p,z] <= max_radiowozy[p,z];

s.t. min_dostepne_zmiana {z in zmiany}: sum{p in dzielnice} wyslane_radiowozy[p,z] >= zmiany_radiowozy[z];
s.t. min_dostepne_dzielnice {p in dzielnice}: sum{z in zmiany} wyslane_radiowozy[p,z] >= dzielnice_radiowozy[p];

solve;

printf{p in dzielnice, z in zmiany}:"\ndo dzielnicy %s na zmianie %s wyslano %d radiowozow",p,z,wyslane_radiowozy[p,z];
printf:"\nliczba wykorzystywanych radiowozow:%d\n",wyslane;
