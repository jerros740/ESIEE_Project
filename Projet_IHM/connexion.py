from tkinter import *
import subprocess


#Creation de la fenêtre
root = Tk()
root.title("Speed Game")
root.iconbitmap('image/icon_jeu.ico')
fenrw = root.winfo_reqwidth()
fenrh = root.winfo_reqheight()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("+%d+%d" % ((sw/2)-(fenrw/2), (sh/2)-(fenrh/2))) #affichage de la fenêtre au milieu de l'écran 
root.resizable(0,0)
frame = Frame(root)
frame2 = Frame(root)
frame.grid(row =0,column = 0)
frame2.grid(row=2,column =0)


#Image
oeil_ouvert = PhotoImage(file = 'image/ouvert.PNG').subsample(11)
oeil_ferme = PhotoImage(file = 'image/ferme.PNG').subsample(11)

#Variable
message = StringVar()
montre = 'non'
usr = StringVar()
mdp = StringVar()
val=IntVar()

#Creation des labels,boutons,frames etc...
l_connexion = Label(frame, text = "Connexion")
l_user = Label(frame, text = "Nom d'utilisateur :")
l_password = Label(frame, text = "Mot de passe : ")
ent_user = Entry(frame,textvariable = usr)
ent_password = Entry(frame, show = '*', textvariable = mdp)
b_connexion = Button(frame, text = "Se connecter")
b_creer = Button(frame, text = "Pas de compte ?")
b_show = Button(frame, image = oeil_ferme)
b_ressayer = Button(root, text = 'Ressayer')
l_message = Label(frame2, text = "")
check_b=Checkbutton(frame, text ="Sans compte", variable=val)


#Fonction/procédure/callback

def show_pass() : # Cette procédure permet d'afficher le mot de passe sous forme de '*****' ou en string
    global montre,b_show # Variable globale : montre vaut oui par défaut et b_show contient l'image oeil ouvert
    # Si montre vaut non, on fait en sorte que le mot de passe est en string,on modifie l'image et montre vaudra oui et idem pour l'inverse
    if montre == 'non' : 
        ent_password.config(show = '') # Le mot de passe est affiché sans être caché
        b_show.config(image = oeil_ouvert)
        montre = 'oui'
        return

    if montre == 'oui' :
        ent_password.config(show = '*') # Le mot de passe est  affiché en étant caché. Mot de passe du type : ****
        b_show.config( image = oeil_ferme)
        montre = 'non'
        return

def connect() : # Cette procédure permet de nous connecter au jeu avec nos identifiants
    ent_user['state'] = 'disabled'
    ent_password['state'] = 'disabled'
    b_show['state'] = 'disabled'
    
    if val.get()==1: #Connexion en mode invite
        l_message.config(text ='Connexion réussie')
        root.destroy()
        subprocess.call([sys.executable,'./Accueil.py', "Invité"])
        return

    #On récupère le nom d'utilisateur et le mot de passe ecrit dans les entrées user et password
    user = usr.get()
    password = mdp.get()
    
    # Ouverture du fichier 
    f = open("info/donnees.txt",'r+') # Le fichier contient les mots de passes associé à chaque utilisateur 
    lecture = f.readlines() # Le fichier contient des donnees de type : (user,password)
    f.close()
    # Fermeture du fichier

    if('('+str(user)+','+str(password)+')\n') in lecture : # L'utilisateur et le mot de passe est dans le fichier 
        l_message.config(text ='Connexion réussie')
        root.destroy()
        subprocess.call([sys.executable,'./Accueil.py',str(user)])

    else : # L'utilisateur ou le mot de passe n'est pas dans le fichier
        l_message.config(text = "   Nom d'utilisateur inconnue ou mauvais mot de passe")
        b_ressayer.grid(row = 5,column = 0,pady = 5)
        
    

def connect_b(event) : # Création d'un callback pour valider nos info (user,password) en appuyant aussi sur un bouton
    connect()

def cree(): # Création d'un callback pour ouvrir la fenêtre pour creér son compte
    root.destroy()
    subprocess.call([sys.executable,'./creer_compte.py']) # Excution de la ligne de commande python creer_compte.py 

def ressayer() : # Procédure pour réecrire son pseudo et mot de passe 
    usr.set('')
    mdp.set('')
    l_message.config(text = '')
    ent_user['state'] = 'normal'
    ent_password['state'] = 'normal'
    b_ressayer.grid_forget() # On cache le bouton

def sans_compte():
    if val.get()==1:
        ent_user.config(state=DISABLED)
        ent_password.config(state=DISABLED)
        
    if val.get() == 0 :
        ent_user.config(state=NORMAL)
        ent_password.config(state=NORMAL)


    
#Modif avec config
b_show.config(command = show_pass)
b_connexion.config(command = connect)
b_ressayer.config(command = ressayer)
b_creer.config(command = cree)
check_b.config(command=sans_compte)

#binding 
root.bind('<Return>',connect_b)

#Affichage
l_user.grid(row = 1, column = 0, padx = 2,sticky = NSEW )
l_password.grid(row = 2, column = 0, sticky = NSEW )
l_connexion.grid(row = 0, column = 0, columnspan = 4,pady = 5)
ent_user.grid(row = 1, column = 1, columnspan = 2, padx = 4)
ent_password.grid(row = 2, column = 1, columnspan = 2, pady = 4)
frame.grid(row = 1, column = 0)
b_connexion.grid(row = 4, column = 2, pady = 10,sticky = NSEW)
b_creer.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = NSEW)
b_show.grid(row = 2, column = 3, padx = 5)
l_message.grid(row = 5, column = 0, columnspan = 4)
check_b.grid(row=3, column=0, columnspan=4)
    



root.mainloop()



