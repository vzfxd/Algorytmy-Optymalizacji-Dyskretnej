param cols, integer;
param rows, integer;
param k, integer;
param containers{i in 1..rows, j in 1..cols},binary;

var cams{1..rows,1..cols},>=0 binary;


minimize cam_numbers: sum{i in 1..rows, j in 1..cols} cams[i,j];


subject to same_position{i in 1..rows, j in 1..cols}: containers[i,j] + cams[i,j] <= 1;
subject to cam_coverage{i in 1..rows, j in 1..cols}:
    if(containers[i,j]==1) then
        sum{a in max(1,i-k)..min(rows,i+k)} cams[a,j] +
        sum{b in max(1,j-k)..min(cols,j+k)} cams[i,b] >= containers[i,j];



solve;

printf:"\nliczba kamer: %d\n",cam_numbers;
for{i in 1..rows}
{
    for{j in 1..cols}
    {
        printf (if cams[i,j] then 'cam ' else if containers[i,j] then 'con ' else 'xxx ');
    }
    printf:"\n";
}


