#---------- Initialisation des ressources ----------
    
baseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#---------- Programme Principale ----------
    
incrementation = 2 #variable globale pour le pas d'incrémentation

def shuffleSet(oldSet, incrementation): #fonction pour mélanger et ramasser les cartes jusqu'à ce qu'il reste une seule carte dans l'ancien paquet
    newSet = [] #initialisation du nouveau paquet
    tempSet = oldSet.copy() #copie de l'ancien paquet pour traiter les données de celui-ci sans le modifier
    i = 0 #initialisation du curseur
    while len(tempSet) != 0: #répétition du script jusqu'à ce qu'il reste plus aucune carte  
        currentCard = tempSet[i] #variabilisation de la carte sur laquelle le curseur se trouve actuellement pour faciliter le traitement par la suite    
        tempSet.remove(currentCard) #suppression de la carte actuelle dans le paquet temporaire (pour ne pas avoir à revenir sur la même carte plus tard)    
        newSet.append(currentCard) #ajout de la carte actuelle dans le nouveau paquet
        i += incrementation-1 #incrémentation du compteur pour déplacer le curseur (-1 car l'élément currentCard a été enlevé)
        if len(tempSet) != 0: #vérification pour éviter modulo 0
            i = i%len(tempSet) #recalibrage du compteur pour qu'il reste dans la range 0-(len(tempSet)) en calculant le modulo
    return newSet #retourne le nouveau paquet mélangé

def main(): 
    n = input("Nombre de mélanges: ") #saisie du nombre N de mélanges par l'utilisateur
    if n.isdigit(): #vérification que n soit bien un nombre entier
        cardSet = baseList.copy() #copie de la liste de base pour garder l'originale intacte
        for i in range(int(n)) : #répétition du mélange n fois
            cardSet = shuffleSet(cardSet, incrementation) #mélange du paquet
            print("p" + str(i) + "= " + str(cardSet))
        print("Pour " + str(n) + " paquets: " + str(cardSet))
        return cardSet #retourne le paquet après n mélanges
    else: #cas où l'utilisateur a saisi autre chose qu'un nombre entier
        print("please enter an int")
        return

main()