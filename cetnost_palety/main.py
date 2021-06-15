from package import modul
from itertools import repeat
import yaml

obj = {}
for i in range(1, 206):
    obj['P '+str(i)] = []

x = []

while True:
    pal = modul.cislo_pal()
    opakovani = modul.pocet_opakovani()
    x.extend(repeat(pal, opakovani))
    
    pokracovat = input("chceš zadat další paletu? (y/n) ")
        
    if pokracovat == "y" or pokracovat == "Y":
        continue
    else:
        break   

for num in x:
    obj["P "+str(num)].append(num)

vystup = modul.vystup(obj)

print(yaml.dump(vystup, default_flow_style=False))