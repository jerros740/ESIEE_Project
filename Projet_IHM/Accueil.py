#Import
from tkinter import *
from tkinter import ttk, font
import webbrowser,subprocess,json,time
from tkinter.messagebox import *

#Variable
    #Arguments
pseudo = sys.argv[1] #arguments d'entrée, d'il n'y a pas de pseudo, on ne peut pas ouvrir le fichier

#Fenetre

root=Tk()
root.title("Accueil / Utilisateur : "+str(pseudo))
fenrw = root.winfo_reqwidth()
fenrh = root.winfo_reqheight()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("+%d+%d" % ((sw-fenrw)/2, (sh-fenrh)/2)) #affichage de la fenêtre au milieu de l'écran 
root.resizable(0,0)
root.iconbitmap('image/icon_jeu.ico')

#Variable
    #Arguments
pseudo = sys.argv[1] #arguments d'entrée, d'il n'y a pas de pseudo, on ne peut pas ouvrir le fichier

    #Initialisation d'autre variable
police_1 = 'Arial'
taille_1 = 15
background = '#8DD3FF'
nom = StringVar()
nom_db=StringVar()
nv_nom = StringVar()
mdp = StringVar()
verif_mdp = StringVar()



####Images####

param = PhotoImage(file = 'image/parametre.png').subsample(7)
podium = PhotoImage(file = 'image/podium.png').subsample(3)
profil = PhotoImage(file = 'image/compte.png').subsample(35)
home = PhotoImage(file = 'image/home.png').subsample(65)

######### Fonction #########
def valider(): #fonction pour changer la police de l'interface de jeu à partir de la combobox
    global police_1,taille_1,label_change
    ma_police=combo_police.get()
    ma_taille=combo_taille.get()
    
    if ma_taille == 'Petit' : #Si la valeur de la combobox est petit alors la taille correspondante est 5
        taille_1 = 5
    if ma_taille == 'Moyen' :#Si la valeur de la combobox est moyen alors la taille correspondante est 15
        taille_1 = 15
    if ma_taille == 'Grand' : #Si la valeur de la combobox est grand alors la taille correspondante est 25
        taille_1 = 25

    police_1 = ma_police
    label_change.config(font=(ma_police, taille_1)) #le texte correspondant au label est écrit avec la police de la combo_police et la taille de la combo_taille
    label_change.update()


#### Boutton ######

tabs=ttk.Notebook(root)

tabs.pack(fill=BOTH, expand=True)

accueil=Frame(tabs,bg='#8DD3FF')
classement=Frame(tabs, bg='#8DD3FF')
compte=Frame(tabs, bg='#8DD3FF')
parametre=Frame(tabs, bg='#8DD3FF')

tabs.add(accueil, text='Accueil',image = home, compound=LEFT)
tabs.add(classement, text='Classement',image = podium, compound=LEFT)
tabs.add(compte, text='Compte',image = profil, compound=LEFT)
tabs.add(parametre, text='Paramètre',image = param, compound=LEFT)

########## Accueil ############

    ##### Variables ########

nbm= StringVar()
tot_mot = 30

    ####### Fonction ########

def nb_mot(): # Callback pour les radiobuttons 
    global tot_mot,nbm
    
    if nbm.get()== '0':
        tot_mot = 15
    if nbm.get() == '1':
        tot_mot = 30
    if nbm.get() == '2':
        tot_mot = 60

    
    ######Label et Bouton##########

b_quitter = Button(accueil, text = "Quitter", font = ("Salina",10),bg ="#AEFFBC" )
b_quitter.grid(row = 0, column = 3)

vide1=Label(accueil, text="           ", bg='#8DD3FF')
vide1.grid(row=0, column=0, padx=5, pady=5)

vide2=Label(accueil, text="           ", bg='#8DD3FF')
vide2.grid(row=6, column=2, padx=5, pady=5)

mdj=Label(accueil, text=" Modes de jeu: ", font=("Hollywood Hills", 40),foreground='#970000', bg='#8DD3FF')
mdj.grid(row=1, column=1, padx=5, pady=5, sticky=NSEW)

b_facile=Button(accueil, text="Facile", font=("Splash", 20), bg="#FFEFBC", activebackground='#FFD44A',command = lambda : game('facile'))
b_facile.grid(row=2, column=1, padx=5, pady=5)

b_inter=Button(accueil, text="Intermédiaire", font=("Splash", 20), bg="#FFB18A", activebackground='#FF9C4A',command = lambda : game('Intermédiaire'))
b_inter.grid(row=3, column=1, padx=5, pady=5)

b_dif=Button(accueil, text="Difficile", font=("Splash", 20), bg="#FF6262", activebackground='#FF2828',command = lambda : game('difficile'))
b_dif.grid(row=4, column=1, padx=5, pady=5)

b_clm=Button(accueil, text="Contre-la-montre", font=("Splash", 20), bg="#0029A2",foreground='white', activebackground='#4A599C', activeforeground='white',command = lambda : game('clc'))
b_clm.grid(row=5, column=1, padx=5, pady=5, sticky=NSEW)

rb1 = Radiobutton(accueil, text= "15 mots ( Hors contre-la-montre )", background='#8DD3FF', value=0, var=nbm, command=nb_mot)
rb2 = Radiobutton(accueil, text= "30 mots ( Hors contre-la-montre )", background='#8DD3FF', value=1, var=nbm, command=nb_mot)
rb3 = Radiobutton(accueil, text= "60 mots ( Hors contre-la-montre )", background='#8DD3FF', value=2, var=nbm, command=nb_mot)

rb1.grid(row=2, column=0, padx=3)
rb2.grid(row=3, column=0 ,padx=3)
rb3.grid(row=4, column=0 ,padx=3)

#######Radiobutton par defaut
nbm.set(1)
   
    

################ Parametres ##############

    ###### Label variable ##########

label_change=Label(parametre,text="Changer la police et la taille du mot à écire",font=('Arial', 15), bg='#8DD3FF' )
label_change.grid(row=0, column=0, pady=5, padx=10, columnspan=3)

label_police=Label(parametre, text = 'Police', font=('Arial' ,8), bg='#8DD3FF' )
label_police.grid(row=1, column=0)
label_taille=Label(parametre, text = 'Taille', font=('Arial' ,8), bg='#8DD3FF' )
label_taille.grid(row=2, column=0)

link1 = Label(parametre, text="Changer la couleur de fond avec ces codes couleurs ", fg="blue", cursor="hand2", bg='#8DD3FF',
              font=('Arial' ,12))
link1.bind("<Button-1>", lambda e: callback("https://htmlcolorcodes.com"))


link1.grid(row=4, column=0,padx=5, pady=5 ,columnspan=3)

police = StringVar()
taille= StringVar()
couleur=StringVar()

    #######combo bouton##########

liste_police=list(font.families())
liste_police.sort()

combo_police=ttk.Combobox(parametre, textvariable=police, values= liste_police, state='readonly')
combo_police.grid(row=1, column = 1,columnspan=2, pady=10, padx=10)
combo_police.set("Arial")

b_valide1 = ttk.Button(parametre, text='Valider')
b_valide1.grid(row=3, column=0, columnspan=3)

liste_taille=['Petit','Moyen','Grand']

combo_taille=ttk.Combobox(parametre, textvariable=taille, values= liste_taille, state='readonly')
combo_taille.grid(row=2, column=1,columnspan=2, pady=5, padx=10)
combo_taille.set("Moyen")
ent_couleur=Entry(parametre, textvariable=couleur, width=30)
ent_couleur.grid(row=5, column=0, columnspan=2, pady=5, padx=5)
b_valide = ttk.Button(parametre, text='Valider')
b_valide.grid(row=5, column=2, pady=5)



######## Fonction ##########

def quitter_fct(): #fonction quitter qui permet de se déconnecter du jeu
    a = askyesno("Deconnexion","Etes-vous sûr ?") #message box avec pour reponse à la question oui ou non
    if a is True : #si la réponse est oui alors on ferme la fenêtre et on ouvre la page de connexion
        root.destroy()
        subprocess.call([sys.executable,"./connexion.py"])
#
def modif_mdp() : # fonction qui permet de modifier le mot de passe 
    global nom_db_entre,mdp_entre,verif_mdp_entre

    f=open('info/donnees.txt', 'r+') #ouvre le fichier donnees.txt
    cpt = 0
    lecture=f.readlines()
    ligne = ""

    for i in lecture:
        index_virg=i.index(',') #retrouve l'indice de la virgule
        nom_utilise=i[1:index_virg] #le nom est ce que l'on trouve avant la virgule
        if pseudo == nom_utilise : #si le pseudo est dans le fichier il retourne la position
            ind = cpt
            ligne = i
        cpt += 1 
    f.seek(0)
    if mdp_entre.get()== verif_mdp.get() and pseudo == nom_db.get(): #si le mot de passe est identique à la verification et le pseudo identique au non de base 
        for line in lecture :
            if line != ligne :
                f.write(line) 
            else : 
                f.write(line[0:index_virg+1]+verif_mdp_entre.get()+')\n') # alors on retrouve la ligne et on écrit dedans à la place
        f.truncate()
        f.close()
        
        showinfo('Reussie','Veuillez vous reconnecter.')
        root.destroy()
        subprocess.call([sys.executable,'./connexion.py'])
        
        
    else :
        showinfo('Erreur','Ce n\'est pas votre pseudo ou les mots de passes ne correspondent pas.') # sinon on avertit que le pseudo n'existe pas 
        f.close()
        return

def modif_nom(): #fonction pour modifier le nom
    global nom, nv_nom,pseudo
    f=open('info/donnees.txt', 'r+') 
    cpt = 0
    lecture=f.readlines()
    ligne = ""

    for i in lecture: #on parcourt le dossier 
        index_virg=i.index(',')
        nom_utilise=i[1:index_virg]
        if pseudo == nom_utilise :# on verifie que le nom existe et on le remplace une foi qu'on l'a trouvé
            ind = cpt
            ligne = i
        if nv_nom.get() == nom_utilise : 
            return
        cpt += 1 
    f.seek(0)
    if pseudo == nom.get() : # Si le pseudo ( avec lequel on s'est connecté ) est le meme que celui renseigné on va vérifier si il n'y a pas de double dans le fichier
        for line in lecture :
            if line != ligne :
                f.write(line)
            else : 
                f.write('('+nv_nom.get()+line[index_virg:])
        f.truncate()
        f.close()
        
        showinfo('Reussie','Veuillez vous reconnecter.')
        root.destroy()
        subprocess.call([sys.executable,'./connexion.py'])
        
    else : # Message d'erreur si le pseudo n'est pas le meme que celui écrit
        showinfo('Erreur','Ce n\'est pas votre pseudo. ')
        f.close()
        return
            
def game(niveau) : #ouvre l'interface de jeu en fonction du niveau
    root.destroy()
    if niveau == 'clc' :
        subprocess.call([sys.executable,'./Typing_game_'+str(niveau)+'.py',pseudo,str(police_1),str(taille_1),background])
    else : 
        subprocess.call([sys.executable,'./Typing_game_FMD.py',pseudo,niveau,str(police_1),str(taille_1),background,str(tot_mot)])

def callback(url): # fonction qui permet d'ouvrir un lien hypertexte
    webbrowser.open_new(url) 

    ########## Variables #########



    ###### Label et Entré de texte #########

change_id=Label(compte, text="Changer nom d'utilisateur", bg='#8DD3FF')
change_id.grid(row=0, column=1)
change_mdp=Label(compte, text="Changer le mot de passe", bg='#8DD3FF')
change_mdp.grid(row=4, column=1)
vide=Label(compte, text='', bg='#8DD3FF')
vide.grid(row=9, column=1, padx=5, pady=5)


nom_txt = Label(compte, text='Nom d\'utilisateur: ',  bg='#8DD3FF')
nv_nom_txt= Label(compte, text='Nouveau nom d\'utilisateur: ',  bg='#8DD3FF')
mdp_txt = Label(compte, text='Nouveau mot de passe: ',  bg='#8DD3FF')
verif_mdp_txt = Label(compte, text='Confirmation mot de passe: ',  bg='#8DD3FF')
nom_db_txt = Label(compte, text='Nom d\'utilisateur: ',  bg='#8DD3FF')

nom_txt.grid(row=1, column=0, padx=5, pady=5)
nv_nom_txt.grid(row=2, column=0, padx=5, pady=5)
nom_db_txt.grid(row=5, column=0, padx=5, pady=5)
mdp_txt.grid(row=6, column=0, padx=5, pady=5)
verif_mdp_txt.grid(row=7, column=0, padx=5, pady=5)

nom_entre=Entry(compte, width=30, textvariable=nom)
nv_nom_entre=Entry(compte, width=30, textvariable=nv_nom)
nom_db_entre=Entry(compte, width=30, textvariable=nom_db)
mdp_entre=Entry(compte, width=30, textvariable=mdp, show='*')
verif_mdp_entre=Entry(compte, width=30, textvariable=verif_mdp, show='*')

nom_entre.grid(row=1, column=1, padx=5, pady=5)
nv_nom_entre.grid(row=2, column=1, padx=5, pady=5)
nom_db_entre.grid(row=5, column=1, padx=5, pady=5)
mdp_entre.grid(row=6, column=1, padx=5, pady=5)
verif_mdp_entre.grid(row=7, column=1, padx=5, pady=5)

    ##### Boutons #######

bouton_creer1= Button(compte, text="Changer le mot de passe")
bouton_creer1.grid(row=8, column=1, padx=5, pady=5)

bouton_creer2= Button(compte, text="Changer le nom", command=modif_nom)
bouton_creer2.grid(row=3, column=1, padx=5, pady=5)

########## Classement #############

    ######## Combo #######
class_var = StringVar()
liste_class=["Facile", "Intermédiaire", "Difficile", "Contre-la-montre"]
combo_class=ttk.Combobox(classement, textvariable=class_var, values= liste_class, state='readonly')
combo_class.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
combo_class.set(liste_class[0])

b_valider_niveau = Button(classement,text = 'Valider')
b_valider_niveau.grid(row = 0, column = 3, columnspan = 2)

    ######## creation tableau #########

pw=PanedWindow(classement, orient=HORIZONTAL, bg='grey')
pw.grid(row=2, column=0,rowspan=10, columnspan=2, pady=5, padx=5)

frame0=Frame(pw, width=30, height=320, relief=FLAT)
frame1=Frame(pw, width=100, height=320, relief=FLAT)
frame2=Frame(pw, width=100, height=320, relief=FLAT)


pw.add(frame0)
pw.add(frame1)
pw.add(frame2)

pw2=PanedWindow(classement, orient=HORIZONTAL, bg='grey')
pw2.grid(row=2, column=3,rowspan=10, columnspan=2, padx=10)

frame5=Frame(pw2, width=30, height=320, relief=FLAT)
frame3=Frame(pw2, width=100, height=320, relief=FLAT)
frame4=Frame(pw2, width=100, height=320, relief=FLAT)

pw2.add(frame5)
pw2.add(frame3)
pw2.add(frame4)

   ######## Label ##########

user=Label(frame1, text="Nom d'utilisateur", bg='#8AB5FF')
user.grid(row=1, column=1, sticky=NSEW)
mpm=Label(frame2, text="Mot par minute", bg='#8AB5FF')
mpm.grid(row=1, column=2, sticky=NSEW)
c0=Label(frame0, text="", bg='#8AB5FF')
c0.grid(row=1, column=0, sticky=NSEW)

ligne1=Label(frame1, text="", bg='#C0FFBF')
ligne1.grid(row=2, column=1, sticky=NSEW)
perf1=Label(frame2, text="", bg='#C0FFBF')
perf1.grid(row=2, column=2, sticky=NSEW)
c1=Label(frame0, text="1", bg='#C0FFBF')
c1.grid(row=2, column=0, sticky=NSEW)

ligne2=Label(frame1, text="", bg='#8AB5FF')
ligne2.grid(row=3, column=1, sticky=NSEW)
perf2=Label(frame2, text="", bg='#8AB5FF')
perf2.grid(row=3, column=2, sticky=NSEW)
c2=Label(frame0, text="2", bg='#8AB5FF')
c2.grid(row=3, column=0, sticky=NSEW)

ligne3=Label(frame1, text="", bg='#C0FFBF')
ligne3.grid(row=4, column=1, sticky=NSEW)
perf3=Label(frame2, text="", bg='#C0FFBF')
perf3.grid(row=4, column=2, sticky=NSEW)
c3=Label(frame0, text="3", bg='#C0FFBF')
c3.grid(row=4, column=0, sticky=NSEW)

ligne4=Label(frame1, text="", bg='#8AB5FF')
ligne4.grid(row=5, column=1, sticky=NSEW)
perf4=Label(frame2, text="", bg='#8AB5FF')
perf4.grid(row=5, column=2, sticky=NSEW)
c4=Label(frame0, text="4", bg='#8AB5FF')
c4.grid(row=5, column=0, sticky=NSEW)

ligne5=Label(frame1, text="", bg='#C0FFBF')
ligne5.grid(row=6, column=1, sticky=NSEW)
perf5=Label(frame2, text="", bg='#C0FFBF')
perf5.grid(row=6, column=2, sticky=NSEW)
c5=Label(frame0, text="5", bg='#C0FFBF')
c5.grid(row=6, column=0, sticky=NSEW)

ligne6=Label(frame1, text="", bg='#8AB5FF')
ligne6.grid(row=7, column=1, sticky=NSEW)
perf6=Label(frame2, text="", bg='#8AB5FF')
perf6.grid(row=7, column=2, sticky=NSEW)
c6=Label(frame0, text="6", bg='#8AB5FF')
c6.grid(row=7, column=0, sticky=NSEW)

ligne7=Label(frame1, text="", bg='#C0FFBF')
ligne7.grid(row=8, column=1, sticky=NSEW)
perf7=Label(frame2, text="", bg='#C0FFBF')
perf7.grid(row=8, column=2, sticky=NSEW)
c7=Label(frame0, text="7", bg='#C0FFBF')
c7.grid(row=8, column=0, sticky=NSEW)

ligne8=Label(frame1, text="", bg='#8AB5FF')
ligne8.grid(row=9, column=1, sticky=NSEW)
perf8=Label(frame2, text="", bg='#8AB5FF')
perf8.grid(row=9, column=2, sticky=NSEW)
c8=Label(frame0, text="8", bg='#8AB5FF')
c8.grid(row=9, column=0, sticky=NSEW)

ligne9=Label(frame1, text="", bg='#C0FFBF')
ligne9.grid(row=10, column=1, sticky=NSEW)
perf9=Label(frame2, text="", bg='#C0FFBF')
perf9.grid(row=10, column=2, sticky=NSEW)
c9=Label(frame0, text="9", bg='#C0FFBF')
c9.grid(row=10, column=0, sticky=NSEW)

ligne10=Label(frame1, text="", bg='#8AB5FF')
ligne10.grid(row=11, column=1, sticky=NSEW)
perf10=Label(frame2, text="", bg='#8AB5FF')
perf10.grid(row=11, column=2, sticky=NSEW)
c10=Label(frame0, text="10", bg='#8AB5FF')
c10.grid(row=11, column=0, sticky=NSEW)


user2=Label(frame3, text="Nom d'utilisateur", bg='#8AB5FF')
user2.grid(row=1, column=3, sticky=NSEW)
prec=Label(frame4, text="Précision (en %)", bg='#8AB5FF')
prec.grid(row=1, column=4, sticky=NSEW)
c02=Label(frame5, text="", bg='#8AB5FF')
c02.grid(row=1, column=0, sticky=NSEW)

ligne12=Label(frame3, text="", bg='#C0FFBF')
ligne12.grid(row=2, column=3, sticky=NSEW)
perf12=Label(frame4, text="", bg='#C0FFBF')
perf12.grid(row=2, column=4, sticky=NSEW)
c12=Label(frame5, text="1", bg='#C0FFBF')
c12.grid(row=2, column=0, sticky=NSEW)

ligne22=Label(frame3, text="", bg='#8AB5FF')
ligne22.grid(row=3, column=3, sticky=NSEW)
perf22=Label(frame4, text="", bg='#8AB5FF')
perf22.grid(row=3, column=4, sticky=NSEW)
c22=Label(frame5, text="2", bg='#8AB5FF')
c22.grid(row=3, column=0, sticky=NSEW)

ligne32=Label(frame3, text="", bg='#C0FFBF')
ligne32.grid(row=4, column=3, sticky=NSEW)
perf32=Label(frame4, text="", bg='#C0FFBF')
perf32.grid(row=4, column=4, sticky=NSEW)
c32=Label(frame5, text="3", bg='#C0FFBF')
c32.grid(row=4, column=0, sticky=NSEW)

ligne42=Label(frame3, text="", bg='#8AB5FF')
ligne42.grid(row=5, column=3, sticky=NSEW)
perf42=Label(frame4, text="", bg='#8AB5FF')
perf42.grid(row=5, column=4, sticky=NSEW)
c42=Label(frame5, text="4", bg='#8AB5FF')
c42.grid(row=5, column=0, sticky=NSEW)

ligne52=Label(frame3, text="", bg='#C0FFBF')
ligne52.grid(row=6, column=3, sticky=NSEW)
perf52=Label(frame4, text="", bg='#C0FFBF')
perf52.grid(row=6, column=4, sticky=NSEW)
c52=Label(frame5, text="5", bg='#C0FFBF')
c52.grid(row=6, column=0, sticky=NSEW)

ligne62=Label(frame3, text="", bg='#8AB5FF')
ligne62.grid(row=7, column=3, sticky=NSEW)
perf62=Label(frame4, text="", bg='#8AB5FF')
perf62.grid(row=7, column=4, sticky=NSEW)
c62=Label(frame5, text="6", bg='#8AB5FF')
c62.grid(row=7, column=0, sticky=NSEW)

ligne72=Label(frame3, text="", bg='#C0FFBF')
ligne72.grid(row=8, column=3, sticky=NSEW)
perf72=Label(frame4, text="", bg='#C0FFBF')
perf72.grid(row=8, column=4, sticky=NSEW)
c72=Label(frame5, text="7", bg='#C0FFBF')
c72.grid(row=8, column=0, sticky=NSEW)

ligne82=Label(frame3, text="", bg='#8AB5FF')
ligne82.grid(row=9, column=3, sticky=NSEW)
perf82=Label(frame4, text="", bg='#8AB5FF')
perf82.grid(row=9, column=4, sticky=NSEW)
c82=Label(frame5, text="8", bg='#8AB5FF')
c82.grid(row=9, column=0, sticky=NSEW)

ligne92=Label(frame3, text="", bg='#C0FFBF')
ligne92.grid(row=10, column=3, sticky=NSEW)
perf92=Label(frame4, text="", bg='#C0FFBF')
perf92.grid(row=10, column=4, sticky=NSEW)
c92=Label(frame5, text="9", bg='#C0FFBF')
c92.grid(row=10, column=0, sticky=NSEW)

ligne102=Label(frame3, text="", bg='#8AB5FF')
ligne102.grid(row=11, column=3, sticky=NSEW)
perf102=Label(frame4, text="", bg='#8AB5FF')
perf102.grid(row=11, column=4, sticky=NSEW)
c102=Label(frame5, text="10", bg='#8AB5FF')
c102.grid(row=11, column=0, sticky=NSEW)

#Fonctions pour l'affichage du classement

def tri_MPM(e): #permet de trier en mot par minute 
    return e['MPM']

def tri_PRE(e) : 
    return e['PRE']#permet de trier par précision

def classement_fct(type_score) : #permet de mettre les résultats dans l'onglet classement après avoir trier l'historique
    rank = []
    utilisateur = []
    score = []
    res = []
    f = open("info/partie_"+str(class_var.get())+".txt",'r')
    ligne = []
    for i in f.readlines() :
        ligne.append(i.strip()) #écrit les performances dans le fichier 
    for i in ligne :
        res.append(json.loads(i)) #convertit le fichier en dictionnaire

    if type_score == 'MPM': #trie en mot par minute
        res.sort(key = tri_MPM)
        
    if type_score == 'PRE':#trie par précision
        res.sort(key = tri_PRE)
    res.reverse()
    f.close()

    cpt = 0
    for i in res :  #récupération du user en fonction de ses performances 
        user = i.get("user")
        if type_score == 'MPM' :
            M = i.get("MPM")
        if type_score == 'PRE' : 
            M = i.get("PRE")

        if user not in utilisateur : #prend le meilleur résultat de l'utilisateur car déjà trier 
            utilisateur.append(user)
            score.append(M)
    
    for i in range(len(score)) : #ajout dans la liste rang une liste de tuple
        rank.append([utilisateur[i],str(score[i])])
    
    return rank[0:10]

def affichage_classement() : #affiche les performance triées dans le tableau 
    global ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10, perf1,perf2,perf3,perf4,perf5,perf6,perf7,perf8,perf9,perf10 #On récupere les labels
    global ligne12,ligne22,ligne32,ligne42,ligne52,ligne62,ligne72,ligne82,ligne92,ligne102, perf12,perf22,perf32,perf42,perf52,perf62,perf72,perf82,perf92,perf102
    

    ligne_1 = [ligne1,ligne2,ligne3,ligne4,ligne5,ligne6,ligne7,ligne8,ligne9,ligne10]
    perf_1 = [perf1,perf2,perf3,perf4,perf5,perf6,perf7,perf8,perf9,perf10]

    ligne_2 = [ligne12,ligne22,ligne32,ligne42,ligne52,ligne62,ligne72,ligne82,ligne92,ligne102]
    perf_2 = [perf12,perf22,perf32,perf42,perf52,perf62,perf72,perf82,perf92,perf102]

    for i in range(0,10) : #On reset l'affichage du classement car dans le cas où le classement est vide, l'appli garde l'affichage précédent par défaut 
        ligne_1[i].config(text = "")
        perf_1[i].config(text = "")
        ligne_2[i].config(text = "")
        perf_2[i].config(text = "")

    rang_MPM = classement_fct('MPM')     
    rang_PRE = classement_fct('PRE')   

    cpt = 0   
    for i in rang_MPM : # classe les performances dans la colonne mot par minute 
        ligne_1[cpt].config(text = i[0])
        perf_1[cpt].config(text = i[1])
        cpt += 1

    cpt = 0
    for i in rang_PRE : # classe les performances dans la colonne pécision 
        ligne_2[cpt].config(text = i[0])
        perf_2[cpt].config(text = i[1])
        cpt += 1
    
def valider_couleur(): #permet de modifier la couleur de fond dans chacun des onglets
    global ent_couleur,link1,label_change,label_taille,label_police,background

    ma_couleur=ent_couleur.get()
    background = ma_couleur

    accueil.config(bg=ma_couleur)
    parametre.config(bg=ma_couleur)
    compte.config(bg=ma_couleur)
    classement.config(bg=ma_couleur)

    label_police.config(bg=ma_couleur)
    label_taille.config(bg=ma_couleur)
    link1.config(bg=ma_couleur)
    label_change.config(bg=ma_couleur)

    vide1.config(bg=ma_couleur)
    vide2.config(bg=ma_couleur)
    vide.config(bg=ma_couleur)

    mdj.config(bg=ma_couleur)

    change_id.config(bg = ma_couleur)
    change_mdp.config(bg = ma_couleur)
    nom_txt.config(bg = ma_couleur)
    nv_nom_txt.config(bg = ma_couleur)
    mdp_txt.config(bg = ma_couleur)
    verif_mdp_txt.config(bg = ma_couleur)
    nom_db_txt.config(bg = ma_couleur)
####Appel de la fonction affichge_classement pour afficher directement sans appuyer sur valider
affichage_classement()
###Modif command button
b_valider_niveau.config(command = affichage_classement )
bouton_creer1.config(command= modif_mdp)
b_quitter.config(command = quitter_fct)
b_valide.config(command=valider_couleur)
b_valide1.config(command=valider)

###### Config #########
#root.resizable(0,0)
root.mainloop()
