print ("Entrez le nombre d'échecs : " ) 
echecs = int(input())             
if echecs < 0:
    print("Erreur : le nombre d'échecs ne peut pas être négatif.")
elif echecs >= 20:
    print("CRITIQUE")
elif echecs >= 5:
    print("A SURVEILLER")
else:
    print("NORMAL")