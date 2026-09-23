print ("Entrez le prix unitaire de l'acticle : ")
pn = int(input())
print (" Entrez la quantité achetée : ")
qua = int(input())
print ("Entrez le taux de remise")
txr = int(input())

#calcule du montant brut
mntbr = int(pn*qua)
print (" Le montant brut est : ", mntbr, )

#calcule de la remise 
remise = int(mntbr * txr / 100)
print (" La remise est : ", remise )

#calcule du montant net
mntnet = int(mntbr - remise)
print (" Le montant net est : ", mntnet)


