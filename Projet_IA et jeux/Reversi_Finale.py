import tkinter,random,numpy,time

#  Parametres du jeu

canvas = None   # zone de dessin
Aide = False
#Grille[0][0] désigne la case en haut à gauche
#Grille[2][0] désigne la case en haut à droite
#Grille[0][2] désigne la case en bas à gauche
J1,Ia = False,False
jouer = False
Exit = False
Grille = [ [0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0],
           [0,0,0,1,2,0,0,0],
           [0,0,0,2,1,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
            ]  
Menu = True
Regles = False
Joueur = False
Niveau = False
Tour1 = False
Direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]] # Direction possibles pour vérifier les cases autour d'un pion

Scores = [0,0] # Scores du Joueur1 et du Joueur2 (ou Joueur1 et Ordi)

# Fonction 

def Reset() : #Reinitialiser la grille
    global Grille,J1,Ia

    J1,Ia = False,False
    Grille = [ [0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0], 
           [0,0,0,0,0,0,0,0],
           [0,0,0,1,2,0,0,0],
           [0,0,0,2,1,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0],
            ]
    
def CaseValide(Grille1,Joueur,x,y) : # On vérifie si on peut jouer sur une case de coordonnées (x,y) et on retourne une liste contenant les pions à bouger
    global Direction

    if Joueur == 'J1' :
        P1 = 2
        P2 = 1

    if Joueur == 'J2' or Joueur == 'Ia': 
        P1 = 1
        P2 = 2
    PionABouger = []

    for x2,y2 in Direction : 
            x1 = x+x2
            y1 = y+y2
            PionStock = [[x1,y1]]

            if x1 < 8 and x1 >= 0 and y1 < 8 and y1 >= 0 :
                while Grille1[x1][y1] == P1 : 
                    x1 += x2
                    y1 += y2
                    PionStock.append([x1,y1])

                    if (x1<0) or (x1>7) or (y1<0) or (y1>7) :
                        break

                    if Grille1[x1][y1] == P2 :
                        PionABouger.append(PionStock)
                    
     
    return PionABouger 

def CaseDispoIa(Grille2) : #On retourne les cases où l'ordi peut jouer
    CaseDispo = []

    for x in range(8) : 
        for y in range (8) :  
            if  CaseValide(Grille2,'Ia',x,y)!= [] and CaseValide(Grille2,'Ia',x,y) not in CaseDispo and Grille2[x][y] == 0 :
                CaseDispo.append([x,y])

    if CaseDispo != [] :
        return CaseDispo

def CaseDispoJ1(Grille2) : #On retourne les cases où le joueur peut jouer
    CaseDispo = []

    for x in range(8) : 
        for y in range (8) :  
            if  CaseValide(Grille2,'J1',x,y)!= [] and CaseValide(Grille2,'J1',x,y) not in CaseDispo and Grille2[x][y] == 0 :
                CaseDispo.append([x,y])

    if CaseDispo != [] :
        return CaseDispo

def Compteur(Grille2) :
    Compteur = [0,0]

    for x in range(8) : 
            for y in range (8) : 
                if Grille2[x][y] == 1 :
                    Compteur[0] += 1 #Compteur de case pour J1
                if Grille2[x][y] == 2 :
                    Compteur[1] += 1 #Compteur de case pour Ia

    return Compteur

def Winner(Grille2) : # Vérifier qui gagne et on augmente le score si besoin
    End = False

    if ( CaseDispoIa(Grille2) == None and CaseDispoJ1(Grille2) == None ):
        End = True
    else : 
        End = False

    return End
    

def Points(Grille2) : 
    global J1,Ia,Scores

    if Winner(Grille2) == True :
        C = Compteur(Grille2)
        if C[0] == C[1] :
            J1,Ia = False,False
            

        if C[0] > C[1] : 
            J1,Ia = True,False
            Scores[0] += 1
            
        if C[0] < C[1] :
            J1,Ia = False,True
            Scores[1] += 1 

        time.sleep(2)
        Reset()



def Simulation(Grille2,x,y) : 
    i = 0
    while(CaseDispoIa(Grille2) is not None and CaseDispoJ1(Grille2) is not  None ) :
        ListeCoupsIa = CaseDispoIa(Grille2)
        ListeCoupsJ1 = CaseDispoJ1(Grille2)

        if ListeCoupsIa is not None :
            
            
            if i == 0 :
                CoupsIa = CaseValide(Grille2,'Ia',x,y)
                Grille2[x][y] = 2
                i = 1
            else : 
                C1=random.choice(ListeCoupsIa)
                CoupsIa = CaseValide(Grille2,'Ia',C1[0],C1[1])
                Grille2[C1[0]][C1[1]] = 2
            

            for x1y1 in CoupsIa :
                for xy1 in x1y1 :
                    Grille2[xy1[0]][xy1[1]] = 2
                    
        
        if ListeCoupsJ1 is not None : 
            C2 = random.choice(ListeCoupsJ1)
            CoupsJ1 = CaseValide(Grille2,'Ia',C2[0],C2[1])
            
            for x2y2 in CoupsJ1 :
                for xy2 in x2y2 :
                    Grille2[xy2[0]][xy2[1]] = 1
                    Grille2[C2[0]][C2[1]] = 1

def MonteCarlo(NbreDeSimulation,Grille2) :
    Score = 0
    ScoreMoy = 0
    P = CaseDispoIa(Grille2)
    print('Il y a '+str(len(P))+' case(s) à tester')
    P1 = random.choice(P)
    for a in P : 
        for i in range(0,NbreDeSimulation) : 
            CopyGrille = numpy.copy(Grille2)
            Simulation(CopyGrille,a[0],a[1])
            Score +=  Compteur(CopyGrille)[1] - Compteur(CopyGrille)[0] 
        if Score/NbreDeSimulation > ScoreMoy : 
            ScoreMoy = Score/NbreDeSimulation
            P1 = a
    return P1


def OrdiMax() : 
    global Grille
    time.sleep(0.5)
    ListeIa = CaseDispoIa(Grille) # On apelle la fonction qui nous indique les cases jouables par l'ordinateur
    Points = 0 

    for coup in ListeIa :
        NbrP = CaseValide(Grille,'Ia',coup[0],coup[1]) # On regarde le nombre de pion que l'on peut retourner en fonction de la case
        if len(NbrP) > Points : #On va stocker la case où l'on peut retourner le plus de case possible
            Points = len(NbrP)
            x = coup[0]
            y = coup[1]

    Grille[x][y] = 2
    Affiche()
    # On va jouer le pion à l'endroit où l'on peut retourner le plus de case possible
    CaseIa = CaseValide(Grille,'Ia',x,y)
    for x2y2 in CaseIa :
        for xy in x2y2 :
            if CaseIa != [] :
                Grille[xy[0]][xy[1]] = 2
    time.sleep(0.5)
    Affiche()             

def OrdiCarlo() : 
    global Grille
    T = time.time()
    
    C = MonteCarlo(75,Grille)
    print('Le tour de l\'Ia duré '+str(time.time()-T)+'secondes')
    x = C[0]
    y = C[1]
    print('x = ' +str(x))
    print('y = ' +str(y)+'\n')
    CaseIa = CaseValide(Grille,'Ia',x,y)
    Grille[x][y] = 2
    Affiche()
    for x2y2 in CaseIa :
        for xy1 in x2y2 :
                Grille[xy1[0]][xy1[1]] = 2
    time.sleep(0.5)
    Affiche()            

    
def Play(x,y) : 
    global Grille,jouer 

    CaseJ1 = CaseValide(Grille,'J1',x,y)
    i = 0
    if Grille[x][y] == 0 and CaseJ1 != []  :    
        Grille[x][y] = 1
        Affiche()
        time.sleep(0.5)
        for x2y2 in CaseJ1 :
            for xy in x2y2 :
                if CaseJ1 != [] : #On retourne les pions
                    Grille[xy[0]][xy[1]] = 1
                    
         # Fin du tour de J1
        jouer = True
    else : 
        jouer = False
    Points(Grille)
    Affiche()
    
    if jouer == True and CaseDispoIa(Grille) is not None: #Début du tour pour l'ordinateur
        if Niveau == True :
            OrdiCarlo() #L'ordinateur joue 
        else : 
            OrdiMax()
        while CaseDispoJ1(Grille) is None and not Winner(Grille): #Lorsque J1 ne peut pas jouer 
            if Niveau == True :
                OrdiCarlo() #L'ordinateur joue 
            else : 
                OrdiMax()
        
        jouer = False #Fin du tour pour l'ordinateur
    else : 
        jouer = False
    Points(Grille)
    Affiche()
    
def Play2(x,y) : 

    global Grille,Tour1 

    CaseJ1 = CaseValide(Grille,'J1',x,y)
    i = 0
    if Grille[x][y] == 0 and CaseJ1 != []  :    
        Grille[x][y] = 1
        Affiche()
        time.sleep(0.5)
        for x2y2 in CaseJ1 :
            for xy in x2y2 :
                if CaseJ1 != [] : #On retourne les pions
                    Grille[xy[0]][xy[1]] = 1
                    
        Tour1 = False # Fin du tour de J1
    Points(Grille)
    Affiche()

def Play3(x,y) : 
 
    global Grille,Tour1 

    CaseJ2 = CaseValide(Grille,'Ia',x,y)
    i = 0
    if Grille[x][y] == 0 and CaseJ2 != []  :    
        Grille[x][y] = 2
        Affiche()
        time.sleep(0.5)
        for x2y2 in CaseJ2 :
            for xy in x2y2 :
                if CaseJ2 != [] : #On retourne les pions
                    Grille[xy[0]][xy[1]] = 2
                    
        Tour1 = True # Fin du tour de J1
    Points(Grille)
    Affiche()

def MouseClick(event):
    global Grille,Aide,Menu,Exit,Regles,Niveau,Joueur,Tour1

    window.focus_set()
    x = event.x // 80  # convertit une coordonée pixel écran en coord grille de jeu
    y = event.y // 80
    a = False
    if ( (x>=0) and (x<8) and (y>=0) and (y<8) ) and Menu == False and Regles == False:
        if Joueur == False :
            Play(x,y)   
        else : 
            if Tour1 == False :
                Play2(x,y)
                a = False
            else : 
                Play3(x,y)
                a = True

            if a == False :
                Tour1 = True
            else :
                Tour1 = False
        
    if event.x >= 730 and event.x <= 820 and event.y >= 590 and event.y <= 630  and Menu == False and Regles == False: # Quand on appuie sur le bouton Menu pendant la partie
        Menu = True    
        Affiche()

    if event.x >= 345 and event.x <= 515 and event.y >= 175 and event.y <= 225 and Menu == True and Regles == False : # Quand on appuie sur le bouuton jouer
        Menu = False
        Reset()
        Affiche()
    
    if event.x >= 345 and event.x <= 515 and event.y >= 245 and event.y <= 295 and Menu == True and Regles == False  : # Quand on appuie sur le bouton Règles
        Regles = True
        Menu = False
        Affiche()

    if event.x >= 730 and event.x <= 820 and event.y >= 30 and event.y <= 70 and Menu == False and Regles == True  : # Quand on appuie sur le bouton menu dans les règles
        Regles = False
        Menu = True
        Affiche()

    if event.x >= 700 and event.x <= 850 and event.y >= 535 and event.y <= 575 : # Quand on appuie sur le bouton aide
        if Aide == True :
            Aide = False 
            Affiche()
        else :
            Aide = True
            Affiche()

    if event.x >= 445 and event.x <= 595 and event.y >= 460 and event.y <= 500 and Menu == True : 
        if Niveau == True :
            Niveau = False
        else :
            Niveau = True
        Affiche()

    
    if event.x >= 445 and event.x <= 595 and event.y >= 550 and event.y <= 590 and Menu == True : 
        if Joueur == False :
            Joueur = True
        else :
            Joueur = False
        Affiche()

    if ( (x<0) or (x>8) or (y<0) or (y>8) ) : return
    
      # gestion du joueur humain et de l'IA
    
   

def Affiche(PartieGagnee = False):
    global Grille,jouer,Aide,Menu,Joueur,Regles,Niveau,Tour1,Joueur

    Case = CaseDispoJ1(Grille)
    canvas.delete("all")
    if Menu == True and Regles == False  : # création du menu
        canvas.create_text(430,100, font=('Helvetica', 60), text = 'REVERSI', fill='black')

        canvas.create_rectangle(345,175,515,225, fill='#b0bca4')
        canvas.create_text(430,200,font=('Helvetica', 30), text = 'Jouer', fill = 'black',activefill = 'red')

        canvas.create_rectangle(345,245,515,295, fill='#b0bca4')
        canvas.create_text(430,270,font=('Helvetica', 30), text = 'Règles', fill = 'black',activefill = 'red')
        
        canvas.create_text(330,480,font=('Helvetica', 30), text = 'Ordi   :', fill = 'black')
        canvas.create_text(330,570,font=('Helvetica', 30), text = 'Joueur :', fill = 'black')

        if Niveau == False :
            canvas.create_oval(445,460,595,500,outline = 'black',fill = 'white', width = '1')
            canvas.create_text(520,480, font=('Helvetica', 18), text = 'Niveau 1', fill='black', activefill = 'red' )
        if Niveau == True : 
            canvas.create_oval(445,460,595,500,outline = 'black',fill = 'white', width = '1')
            canvas.create_text(520,480, font=('Helvetica', 18), text = 'Niveau 2', fill='black', activefill = 'red' )

        if Joueur == False :
            canvas.create_oval(445,550,595,590,outline = 'black',fill = 'white', width = '1')
            canvas.create_text(520,570, font=('Helvetica', 18), text = '1 Joueur', fill='black', activefill = 'red' )
        if Joueur == True : 
            canvas.create_oval(445,550,595,590,outline = 'black',fill = 'white', width = '1')
            canvas.create_text(520,570, font=('Helvetica', 18), text = '2 Joueurs', fill='black', activefill = 'red' )

        canvas.create_rectangle(200,0,230,800,fill = 'grey',width='4')
        canvas.create_rectangle(635,0,665,800,fill = 'grey',width='4')
        canvas.create_rectangle(0,335,1000,365,fill = 'grey',width='4')

    elif Regles == True and Menu == False : # Création de la page avec les règles
        canvas.create_text(85,50, font=('Helvetica', 30), text = 'Règles :', fill='darkgreen')
    
        canvas.create_text(450,100, font=('Helvetica', 15), text = ' - Le but du jeu est d\'avoir plus de pions de sa couleur que l\'adversaire à la fin de la partie.', fill='black')
        canvas.create_text(435,140, font=('Helvetica', 15), text = ' - La capture d\'un ou plusieurs pion adverse se fait en l\'encerclant avec 2 de ses pions.', fill='black')
        canvas.create_text(430,180, font=('Helvetica', 15), text = ' - Les alignements considérés peuvent être une colonne, une ligne, ou une diagonale. ', fill='black')

        canvas.create_oval(40,240,100,300,outline="white", width="2")
        canvas.create_text(230,270, font=('Helvetica', 15), text = ' : Cases possibles où jouer ', fill='black')

        for i in range(4):
            canvas.create_line(30+i*80,350,30+i*80,590,fill="green", width="4" )
            canvas.create_line(30,350+i*80,270,350+i*80,fill="green", width="4" )

            canvas.create_line(330+i*80,350,330+i*80,590,fill="green", width="4" )
            canvas.create_line(330,350+i*80,570,350+i*80,fill="green", width="4" )

            canvas.create_line(630+i*80,350,630+i*80,590,fill="green", width="4" )
            canvas.create_line(630,350+i*80,870,350+i*80,fill="green", width="4" )

        canvas.create_rectangle(730,30,820,70,outline = 'black',fill = '#b0bca4', width = '1')
        canvas.create_text(775,50, font=('Helvetica', 18), text = 'Menu', fill='white', activefill = 'red' )
    
        canvas.create_oval(40,440,100,500,outline="white", width="4",fill = "white" )
        canvas.create_oval(120,440,180,500,outline="black", width="4",fill = "black" )
        canvas.create_oval(200,440,260,500,outline="white", width="2")
    
        canvas.create_oval(420,360,480,420,outline="white", width="4",fill = "white" )
        canvas.create_oval(420,440,480,500,outline="black", width="4",fill = "black" )
        canvas.create_oval(420,520,480,580,outline="white", width="2")

        canvas.create_oval(640,360,700,420,outline="white", width="4",fill = "white" )
        canvas.create_oval(720,440,780,500,outline="black", width="4",fill = "black" )
        canvas.create_oval(800,520,860,580,outline="white", width="2")
    
    else :  # création de du jeu (Grille + affichage du jeu)      
        for i in range(9):
            canvas.create_line(i*80,0,i*80,640,fill="green", width="4" )
            canvas.create_line(0,i*80,640,i*80,fill="green", width="4" )
        
        for x in range(8):
            for y in range(8):
                xc = x * 80 
                yc = y * 80 
                
                if ( Grille[x][y] == 1): #pion J1
                    canvas.create_oval(xc+10,yc+10,xc+70,yc+70,outline="white", width="4",fill = "white" )
                
                if ( Grille[x][y] == 2): #pion J2/Ia
                    canvas.create_oval(xc+10,yc+10,xc+70,yc+70,outline="black", width="4",fill = "black" )
                
                if Aide == True and Case != None and Joueur == False:
                    #affichage d'une aide pour savoir où il est possible de jouer
                    for a in Case : 
                        if x == a[0] and y == a[1] and  jouer == False  :
                            canvas.create_oval(xc+10,yc+10,xc+70,yc+70,outline="white", width="2")
                    
        
            canvas.create_text(775,50, font=('Helvetica', 20), text = 'SCORES : ' + str(Scores[0]) + '-' + str(Scores[1]), fill='black')  
        
            canvas.create_text(775,150, font=('Helvetica', 20), text = 'Pion J1: ' +str(Compteur(Grille)[0]), fill='white')  
            canvas.create_text(775,180, font=('Helvetica', 20), text = 'Pion J2: ' +str(Compteur(Grille)[1]), fill='black')  


            if Aide == False and Joueur == False:
                canvas.create_oval(700,535,850,575,outline = 'black',fill = 'white', width = '1')
                canvas.create_text(775,555, font=('Helvetica', 18), text = 'AIDE : OFF', fill='black', activefill = 'red' )
            
            if Aide == True and Joueur == False: 
                canvas.create_oval(700,535,850,575,outline = 'black',fill = 'black', width = '1')
                canvas.create_text(775,555, font=('Helvetica', 18), text = 'AIDE : ON', fill='white', activefill = 'red' )
            
            if J1 == True and Winner(Grille) is True : 
                canvas.create_text(775,450, font=('Helvetica', 18),text = 'J1 à gagné. ' , fill = 'red')
            
            if jouer == True :
                canvas.create_text(775,450, font=('Helvetica', 18),text = 'L\'ordinateur réfléchi. ' , fill = 'Black')
            else :
                canvas.create_text(775,450, font=('Helvetica', 18),text = 'C\'est à vous de jouer. ' , fill = 'Black')



            canvas.create_rectangle(730,590,820,630,outline = 'black',fill = '#b0bca4', width = '1')
            canvas.create_text(775,610, font=('Helvetica', 18), text = 'Menu', fill='white', activefill = 'red' )


    canvas.update()   # force la mise a jour de la zone de dessin
        



# fenetre
window = tkinter.Tk()
window.geometry("900x640") 
window.title('Reversi')

window.protocol("WM_DELETE_WINDOW", lambda : window.destroy())

window.bind("<Button-1>", MouseClick)
# zone de dessin

WIDTH = 900
HEIGHT = 640
canvas = tkinter.Canvas(window, width=WIDTH , height=HEIGHT, bg="#B2FF66")
canvas.place(x=0,y=0)
Affiche()
 
# active la fenetre 

window.mainloop()


