def cislo_pal():

    cislo_pal = "abc"
    while cislo_pal.isnumeric() == False or int(cislo_pal) > 205:
        cislo_pal = input("zadej číslo palety (1-205): ")

        if cislo_pal.isnumeric() == False or int(cislo_pal) > 205:
            print("Prosím vkládat pouze čísla 1 - 205.")
    
    return int(cislo_pal)      

def pocet_opakovani():       
       
    opakovani = "xyz"
    while opakovani.isnumeric() == False:  
        opakovani = input("zadej počet opakování dané palety (1-35): ")

        if opakovani.isnumeric() == False:
            print("Prosím vkládat pouze čísla 1 - 35.")

    return int(opakovani) 

def vystup(obj):
    ven = {}
    for (key, value) in obj.items():
   
        if value != []:
            ven[key] = len(value)  
    return ven          
