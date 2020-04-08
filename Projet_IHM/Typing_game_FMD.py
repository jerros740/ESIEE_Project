
import encodings
from tkinter import *
from tkinter.messagebox import *
import time,random,subprocess,threading

# On récupère les arguments 
pseudo = sys.argv[1]
niveau = sys.argv[2]
police = sys.argv[3]
taille = sys.argv[4]
background = sys.argv[5]
tot_mot = sys.argv[6]

root = Tk()
root.title(str(niveau)+" (Bonjour, "+pseudo+") "+ " Appuyer sur 'espace' pour valider le mot")
frame = Frame(root, relief=SUNKEN,width=700, height=700, bg=background)
frame.pack()
root.iconbitmap('image/icon_jeu.ico')

####Images####

home = PhotoImage(file = 'image/home.png').subsample(25)
res = PhotoImage(file = 'image/reset.png').subsample(16)

#Ouverture et lecture du fichier contenant tous les mot que l'on va afficher 
f =  open('info/mot_'+niveau+'.txt', 'r',encoding = 'utf-8')
p = f.readlines()
f.close()

#Transforme tous les mots en une liste que l'on va 'mixer'

paragraphe_bis = p[0].split()
random.shuffle(paragraphe_bis)
paragraphe = paragraphe_bis[0:int(tot_mot)]
mot_affiche = paragraphe[0]

#Variable
texte = StringVar()
t,fin_mot,fin_game= False,False,True
Tstart, erreur, tot_lettre, indice, mot_restant = 0, 0, 0, 0, len(paragraphe)
temps_sec = '0.0'

#creation des entree,label,button etc...
ent_ecriture = Text(frame, width=30, height=7, bg='#AEFFBC', fg='#002A69', font=('Arial', 14))

l_para = Label(frame,text = mot_affiche, bg=background,fg='#2f7000', font=(police, 35))
l_mot_restants = Label(frame, text = 'Mot(s) restant(s) : ' + str(mot_restant),  bg=background, font=(police, 15), fg='#002357')
#label_temps=Label(frame,text='Temps : 0.00', bg=background, font=('Arial', 15), fg='#002357')
l_mot_suivant0 = Label(frame, text = paragraphe[indice+1], bg=background, font=(police, 20))
l_mot_suivant1 = Label(frame, text = paragraphe[indice+2], bg=background, font=(police, 15))
l_mot_suivant2 = Label(frame, text = paragraphe[indice+3], bg=background, font=(police, 10))
l_mot_suivant3 = Label(frame, text = paragraphe[indice+4], bg=background, font=(police, 5))
l_temps = Label(frame,text = 'Temps : '+temps_sec+' sec', bg = background, font = (police,20))
l_temps.grid(row = 0,column = 4)
l_erreur = Label(frame, text = 'Erreur(s) : '+ str(erreur), bg = background, font = (police,15), fg = '#002357')
b_home=Button(frame, bg = background, image = home , activebackground ='#010092', bd=2, relief= FLAT)
b_reset = Button(frame,image = res, activebackground = '#010092', bd = 2, relief = FLAT)

#Modifications
ent_ecriture.insert(INSERT,"")
ent_ecriture.config(font = ('Arial',20), highlightthickness = 1)
l_mot_restants.config(font = (police,15))

#Affichage
l_para.grid(row=1, column=2, columnspan=2, padx=5, pady=5)
ent_ecriture.grid(row=2, column=2, columnspan=2,rowspan=7 , padx=5, pady=5)
l_mot_restants.grid(row=10, column=1,columnspan=2, padx=5, pady=5)
l_erreur.grid(row = 10, column = 3)
b_home.grid(row=0, column=0)
b_reset.grid(row = 0,column = 1)
#label_temps.grid(row=0, column=4, padx=5, pady=5)
l_mot_suivant0.grid(row = 2, column = 4)
l_mot_suivant1.grid(row = 3, column = 4)
l_mot_suivant2.grid(row = 4, column = 4)
l_mot_suivant3.grid(row = 5, column = 4)

#Fonctions
    
def menu() : # Procédure qui affiche un message pour le retour du menu
    a = askyesno("Retour au menu","Etes-vous sûr ?")

    if a is True : # Si on appuie sur Oui
        root.destroy() # Destruction de la fenêtre 
        subprocess.call([sys.executable,"./Accueil.py",sys.argv[1]]) # Retour à l'accueil
        
def reset() : # Procédure pour recommencer une partie 
    a = askyesno("Recommencer","Voulez-vous recommencer")
    if a is True : # Si on appuie sur Oui
        root.destroy() # Destruction de la fenêtre 
        subprocess.call([sys.executable,"./Typing_game_FMD.py",pseudo,niveau,police,taille,background,tot_mot]) # Relance le jeu
    


def change_word() : # procédure pour afficher les mots suivants sur le coté 
    global indice,paragraphe,l_mot_suivant0,l_mot_suivant1,l_mot_suivant2,l_mot_suivant3

    if indice == len(paragraphe) - 1:  # Si Le mot affiché est l'avant dernier on affiche seulement le dernier 
        l_mot_suivant0.config(text = "")
        l_mot_suivant0.update()

        l_mot_suivant1.config(text = "")
        l_mot_suivant1.update()

        l_mot_suivant2.config(text = "")
        l_mot_suivant2.update()

        l_mot_suivant3.config(text = "")
        l_mot_suivant3.update()
        return
    mot1 = paragraphe[indice+1]
    l_mot_suivant0.config(text = mot1)
    l_mot_suivant0.update()

    if indice == len(paragraphe) - 2: # Si Le mot affiché est l'avant - avant dernier on affiche seulement les 2 derniers
        l_mot_suivant2.config(text = "")
        l_mot_suivant2.update()

        l_mot_suivant3.config(text = "")
        l_mot_suivant3.update()

        l_mot_suivant1.config(text = "")
        l_mot_suivant1.update()

        return
    mot2 = paragraphe[indice+2]
    l_mot_suivant1.config(text = mot2)
    l_mot_suivant1.update()

    if indice == len(paragraphe) - 3: # Si Le mot affiché est le 3eme en partant de la fin on affiche seulement les 3 derniers
        l_mot_suivant2.config(text = "")
        l_mot_suivant2.update()

        l_mot_suivant3.config(text = "")
        l_mot_suivant3.update()
        return
    mot3 = paragraphe[indice+3]
    l_mot_suivant2.config(text = mot3)
    l_mot_suivant2.update()

    if indice == len(paragraphe) - 4: # Sinon on affiche les 4 suivants

        l_mot_suivant3.config(text = "")
        l_mot_suivant3.update()
        return
    mot4 = paragraphe[indice+4]
    l_mot_suivant3.config(text = mot4)
    l_mot_suivant3.update()

def key(event) : # Callback pour executer les instructions lorsque nous appuyons sur le claver
    global t, Tstart, indice,cpt, mot_affiche, fin_mot, fin_game
    touche = event.keysym
    if t == False and (touche !='Shift_L' or touche !='BackSpace'): # Si la partie n'a pas encore commencer et qu'on appuie sur une touche de clavier (hors shift_l et backspace) on lance le timer
        fin_game = False
        timer = threading.Timer(0.1,chrono,[0])
        timer.start()
        Tstart = time.time()
        t = True

    mot_ecrit = ent_ecriture.get(1.0,END).strip('\n')
    if fin_game == False and touche != 'Shift_L': #On vérifie la lettre et si le mot est fini 
        check_letter(mot_ecrit,touche) # Verification du la lettre
        end_word(mot_ecrit,mot_affiche) # Verification du mot 


    #2
def end_word(mot1,mot2) :    
    global fin_mot, tot_lettre

    if len(mot1) == len(mot2) : # Si la taille des 2 mots sont identiques
        tot_lettre += len(mot1)
        fin_mot = True 


def check_letter(mot1,touche) : 
    global erreur, mot_affiche, l_erreur
    if touche == 'BackSpace' or touche == 'Shift_L': # On ne prend pas en compte le backspace et shift_l pour les erreurs
        return

    last_char = len(mot1) - 1 # On récupère l'index du dernier caractère du mot écrit
    if mot1[-1] != mot_affiche[last_char] :  # On compare la lettre du dernier caractère écrit à la lettre correspondante
        erreur += 1 
        l_erreur.config(text = "Erreur(s) : " + str(erreur))
        l_erreur.update()
        l_para.config(fg = '#ff3b1e',bg = "#8DD3FF")
        l_para.update()
    else : 
        l_para.config(fg = '#2f7000',bg = background)
        l_para.update()



    #5
def espace(event) :
    global fin_mot, indice, l_para, mot_affiche, mot_restant, l_mot_restants, fin_game, niveau, temps_sec
    save = None
    if fin_mot == True and fin_game == False : # Si le mot est fini mais que la partie n'est pas fini
        if mot_affiche == paragraphe[-1] :
            mot_restant -= 1
            l_mot_restants.config(text = 'Mot(s) restant(s) : ' + str(mot_restant))
            l_mot_restants.update()
            temps = time.time() - Tstart
            fin_game = True
            scoreT = "Temps : " +str("%.2f"%float(temps_sec))+" secondes \n"
            scoreE = "Erreurs : " + str(erreur) + "/"+ str(tot_lettre)+" caractères \n"
            scoreP = "Précision (en pourcentage) : "+ str("%.2f"%((tot_lettre-erreur)*100/tot_lettre))+"% \n"
            scoreM = 'Mot(s) par minute : '+ str(int((len(paragraphe)*60)/temps)) +'\n'
    
            sure = askyesno("Voulez-vous sauvegarder votre score ?", "Voici votre score : \n"+scoreT + scoreE + scoreP + scoreM)
            if sure is True : 
                save = askyesno("Etes-vous sûr ?", "Voici votre score : \n"+scoreT + scoreE + scoreP + scoreM)
                if save is True : 
                    f = open('info/partie_'+niveau+'.txt','a')
                    f.write("{\"user\" : \"" + str(pseudo)+"\", \"MPM\" : " + str(int((len(paragraphe)*60)/temps))+", \"PRE\" : "+str("%.2f"%((tot_lettre-erreur)*100/tot_lettre))+"}\n")
                    f.close()
                
            time.sleep(1)
            root.destroy()
            subprocess.call([sys.executable,'./Accueil.py',str(pseudo)])
            return
        indice += 1

        mot_affiche = paragraphe[indice]# On passe au mot suivant 
        l_para.config(text = mot_affiche, bg = background)
        ent_ecriture.delete(1.0,END) # Reset de l'entree du texte
        mot_restant -= 1
        l_mot_restants.config(text = 'Mot(s) restant(s) : ' + str(mot_restant))
        change_word() # On actualise l'affichage des mots suivants
       
        #Mis à jours des éléments de la fenêtre

        l_para.update()
        l_mot_restants.update()

        #On remet fin_mot a false pour le prochain mot
        fin_mot = False
    
def chrono(i) :
    global l_temps,temps_sec, fin_game
    if fin_game == True :
        return
    i += 0.1  
    temps_sec = str(i)  
    timer = threading.Timer(0.1, chrono, [i]) # Tous les 0.1 sec on appelle la fonction chrono avec i en parametre
        #Affichage du chronomètre
    if i < 10 : 
        temps_sec = str(i)[0:3]
         # 3 digit
    elif i >= 10 and i < 100 :
        temps_sec = str(i)[0:4] # idem
    else : 
        temps_sec = str(i)[0:5] # idem
        
    l_temps.config(text = "Temps : "+temps_sec+ ' sec')
    l_temps.update() # Mis à jour du label 
    timer.start() # lance le chrono
    
#Modif
b_reset.config(command = reset)
b_home.config(command = menu)

    
#binding
root.bind('<KeyPress>',key)
root.bind('<space>',espace)

fenrw = root.winfo_reqwidth()
fenrh = root.winfo_reqheight()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("+%d+%d" % ((sw-fenrw)/2, (sh-fenrh)/2))
root.resizable(0,0)
#Creation de la fenêtre
root.mainloop()

    


    
