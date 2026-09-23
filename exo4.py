print("Entrez votre âge : ")

age = int(input())

if age < 6:
    print("Le tarif est gratuit")

elif 6 <= age <= 12:
    print("Le tarif est à 500 FCFA")

elif 13 <= age <= 17:
    print("Le tarif est à 1000 FCFA")

elif age >= 18:
    print("Le tarif est à 2000 FCFA")

else:
    print("VOUS N'AVEZ PAS DROIT AU TARIF")

