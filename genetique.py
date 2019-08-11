import json

# chargement du code génétique depuis le fichier dico.txt
# code est une table d'association codon -> proteine

code = json.load(open("dico.txt"))

# chargement de la sequence d'ARN
# on suppose la sequence correctement formée
f = open ("seq1.txt", "r")
sequence = f.read().replace("\n", "")
print("sequence a décoder : >"+sequence+"<")
if len(sequence)%3>0 :
    print("Attention : la séquence est invalide")


# on itere sur la sequence d'ARN
proteine = ""
acide_amine=""

for position in range(len(sequence)//3) :
    codon = sequence[3*position : 3*position+3]
    print("decoding codon "+codon)
    if codon in code:
        acide_amine = code[codon]
    else:
        print("codon "+codon+" is missing in genetic code")

    if acide_amine == "STOP" :
        break
    else:
        proteine = proteine + " " + acide_amine

# on affiche la proteine
print("Proteine : "+proteine)
