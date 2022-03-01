#---------- Initialisation des ressources ----------
    
baseList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#---------- Programme Principale ----------
    
def shuffleSet(oldSet, incrementation): #fonction pour mélanger et ramasser les cartes jusqu'à ce qu'il reste une seule carte dans l'ancien paquet
    newSet = [] #initialisation du nouveau paquet
    tempSet = oldSet.copy() #copie de l'ancien paquet pour traiter les données de celui-ci sans le modifier
    i = 0 #initialisation du curseur
    while len(tempSet) != 0: #répétition du script jusqu'à ce qu'il reste plus aucune carte  
        currentCard = tempSet[i] #variabilisation de la carte sur laquelle le curseur se trouve actuellement pour faciliter le traitement par la suite    
        tempSet.remove(currentCard) #suppression de la carte actuelle dans le paquet temporaire (pour ne pas avoir à revenir sur la même carte plus tard)    
        newSet.append(currentCard) #ajout de la carte actuelle dans le nouveau paquet
        i += incrementation-1 #incrémentation du compteur pour déplacer le curseur
        if len(tempSet) > 2: #vérification du nombre de cartes, lorsqu'il reste moins de 2 cartes il faut pointer la première carte à chaque fois
            i = i%len(tempSet) #recalibrage du compteur pour qu'il reste dans la range 0-(len(tempSet)-1) en calculant le modulo
        else:
            i = 0 #lorsqu'il reste moins de 2 cartes, c'est sur la première que le curseur doit pointer à chaque fois,
                  #or le recalibrage juste au dessus ne le permet pas à cause du fait que l'on compte à partir de 0 et pas 1
                  #qui implique le [-1] dans [i += incrementation-1] ligne 15
    return newSet #retourne le nouveau paquet mélangé

def main():
    n = input("Nombre de mélanges: ") #saisie du nombre N de mélanges par l'utilisateur
    if n.isdigit(): #vérification que n soit bien un nombre entier
        cardSet = baseList.copy() #copie de la liste de base pour garder l'originale intacte
        for i in range(int(n)) : #répétition du mélange n fois
            cardSet = shuffleSet(cardSet, 3) #mélange du paquet
            print("p" + str(i) + "= " + str(cardSet))
        print("Pour " + str(n) + " paquets: " + str(cardSet))
        return cardSet #retourne le paquet après n mélanges
    else: #cas où l'utilisateur a saisi autre chose qu'un nombre entier
        print("please enter an int")
        return

main()