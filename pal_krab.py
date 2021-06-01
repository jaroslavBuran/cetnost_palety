from itertools import repeat
import yaml

obj = {}
for i in range(1, 206):
    obj['P '+str(i)] = []
    
x = []

while True:
    cislo_pal = int(input("zadej číslo palety: "))
    opakovani = int(input("zadej počet opakování dané palety: "))
    x.extend(repeat(cislo_pal, opakovani))
    pokracovat = input("chceš zadat další paletu? (y/n) ")
        
    if pokracovat == "y" or pokracovat == "Y":
        continue
    else:
        break

    


for num in x:
    obj["P "+str(num)].append(num)
    
koko = {}
for (key, value) in obj.items():
   # Check if key is even then add pair to new dictionary
    if value != []:
        koko[key] = len(value)
        

print(yaml.dump(koko, default_flow_style=False))