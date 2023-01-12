#JEU DU TIC TAC TOE EN UTILISANT UN DICTIONNAIRE COMME TABLEAU DE JEU#
tableau = {1:"1", 2:"2",3:"3",
           4:"4", 5:"5",6:"6",
           7:"7", 8:"8",9:"9"}
def afficheTableau():
    print(" |",tableau[1] , "|" , tableau[2] , "|" , tableau[3] ,"|\n", 
          "|",tableau[4] , "|" , tableau[5] , "|" , tableau[6] ,"|\n", 
          "|",tableau[7] , "|" , tableau[8] , "|" , tableau[9] ,"|\n", 
                                                                 )
def verifTableau():
    #Si le tableau est totalement rempli#
    i = 1
    caserempli=0 
    while(i <= 9):
        if tableau[i] == "X" or tableau[i] == "O":
            caserempli +=1    
            i+=1
        else : 
            i+=1
                      
    if caserempli == 9:
        return True
    else: 
        return False

def winner():
    ###Quand un ligne est rempli horizontalement####
    if tableau[1] == "X" and tableau[2] == "X" and tableau[3] == "X":
        return 1
    elif tableau[4] == "X" and tableau[5] == "X" and tableau[6] == "X":
        return 1
    elif tableau[7] == "X" and tableau[8] == "X" and tableau[9] == "X":
        return 1

    if tableau[1] == "O" and tableau[2] == "O" and tableau[3] == "O":
        return 2
    elif tableau[4] == "O" and tableau[5] == "O" and tableau[6] == "O":
        return 2
    elif tableau[7] == "O" and tableau[8] == "O" and tableau[9] == "O":
        return 2
    
    
    ###Quand une ligne est rempli verticalement### 
    if tableau[1] == "X" and tableau[4] == "X" and tableau[7] == "X":
        return 1
    elif tableau[2] == "X" and tableau[5] == "X" and tableau[8] == "X":
        return 1
    elif tableau[3] == "X" and tableau[6] == "X" and tableau[9] == "X":
        return 1

    if tableau[1] == "O" and tableau[4] == "O" and tableau[7] == "O":
        return 2
    elif tableau[2] == "O" and tableau[5] == "O" and tableau[8] == "O":
        return 2
    elif tableau[3] == "O" and tableau[6] == "O" and tableau[9] == "O":
        return 2
        
    #Ici on vérifie la première diagonale en partant de la gauche#    
    if tableau[1] == "X" and tableau[5] == "X" and tableau[9] == "X" : 
        return 1
    elif tableau[1] == "O" and tableau[5] == "O" and tableau[9] == "O" :
        return 2

    #Ici on vérifie la deuxième diagonale en partant de la droite
    if tableau[3] == "X" and tableau[5] == "X" and tableau[7] == "X" : 
        return 1
    elif tableau[3] == "O" and tableau[5] == "O" and tableau[7] == "O" :
        return 2

    return 0


def messageGagnant(joueur):
    if joueur == 1:
        print("Victoire du joueur 1")
    elif joueur == 2: 
        print("Victoire du joueur 2")
    else: 
        return 0
        
def tourJoueur():
    hasj1Played = False
    hasj2Played = True
    isTabRempli= False
    gagnant = 0
    
    while(isTabRempli == False and gagnant == 0): 
        if hasj1Played == False : 
            afficheTableau()
            j1 = int(input("Au tour du joueur 1 (Donnez un numéro) : "))
            tableau[j1] = "X"
            hasj1Played = True
            hasj2Played = False
            isTabRempli = verifTableau()
            if winner() == 1:
                afficheTableau()
                messageGagnant(1)
            gagnant = winner()
          

        elif hasj2Played == False :
            afficheTableau()
            j2 = int(input("Au tour du joueur 2 (Donnez un numéro): "))
            tableau[j2] = "O"
            hasj1Played = False
            hasj2Played = True
            isTabRempli = verifTableau()
            if winner() == 2:
                 afficheTableau()
                 messageGagnant(2)
            gagnant = winner()

    if isTabRempli == True and gagnant == 0: 
        print("Match nul !!!")

print("----JEU DU TIC-TAC-TOE----  \n")
rejouer = True
while(rejouer == True):
    tourJoueur()
    query = input("Voulez vous rejouer ? (O/N) : ")
    if query == "N" or query == "n": 
        rejouer = False 
    else : 
        tableau = {1:"1", 2:"2",3:"3",
           4:"4", 5:"5",6:"6",
           7:"7", 8:"8",9:"9"}