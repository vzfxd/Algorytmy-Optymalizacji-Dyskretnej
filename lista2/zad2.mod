param n, integer;
param T, integer;
set vertices := {1..n};
set edges within vertices cross vertices;
param cost{(i,j) in edges};
param time{(i,j) in edges};
param i0;
param j0;


var selected{(i,j) in edges},binary;


minimize koszt_sciezki: sum{(i,j) in edges} selected[i,j]*cost[i,j];


s.t. ograniczenie_czasu: sum{(i,j) in edges} selected[i,j] * time[i,j] <= T;
s.t. ograniczenie_sciezki{v in vertices}: sum{(j,v) in edges} selected[j,v] + (if v==i0 then 1) == sum{(v,j) in edges} selected[v,j] + (if v==j0 then 1);

solve;

display selected;
display koszt_sciezki;



