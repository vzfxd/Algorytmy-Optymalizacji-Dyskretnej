set lotniska;
set firmy;
param zapotrzebowanie{l in lotniska};
param dostawa{f in firmy};
param ceny{l in lotniska,f in firmy};

var kupione{l in lotniska,f in firmy},>=0,integer;

minimize koszt: sum{l in lotniska} sum{f in firmy} ceny[l,f]*kupione[l,f];

s.t. ograniczenie_dostawy {f in firmy}: sum{l in lotniska} kupione[l,f] <= dostawa[f];
s.t. ograczenie_zapotrzebowania {l in lotniska}: sum{f in firmy} kupione[l,f] == zapotrzebowanie[l];

solve;
printf:'\nminimalny koszt:%d\n',koszt;
printf{f in firmy}:'paliwo kupione od %s : %d\n',f,sum{l in lotniska}kupione[l,f];