set produkty;
set maszyny;

param maszyny_info{m in maszyny, {'koszt','dostepnosc'}};
param produkty_info{p in produkty, {'koszt','cena','popyt'}};
param produkty_maszyny{p in produkty, m in maszyny};

var plan_produkcji{p in produkty},>=0,integer;  # ile wyprodukowano danego produktu (w kilogramach)

                                            #zysk ze sprzedaży produktu
maximize zysk: sum{p in produkty}(  plan_produkcji[p]*(produkty_info[p,'cena'] - produkty_info[p,'koszt']) -
               sum{m in maszyny} plan_produkcji[p]*produkty_maszyny[p,m]/60 * maszyny_info[m,'koszt']);
                                        #ile godzin pracuje maszyna             #koszt pracy maszyny

s.t. ograniczenie_popyt {p in produkty} : plan_produkcji[p] <= produkty_info[p,'popyt'];
s.t. ograniczenie_dostepnosci {m in maszyny} : sum{p in produkty} plan_produkcji[p]*produkty_maszyny[p,m] <= maszyny_info[m,'dostepnosc']*60;
                                                    #ile maszyna pracuje w minutach


solve;
printf{p in produkty}:'\nliczba wyprodukowanych kilogramów %s: %d',p,plan_produkcji[p];
printf:"\nzysk:%.2f\n",zysk;