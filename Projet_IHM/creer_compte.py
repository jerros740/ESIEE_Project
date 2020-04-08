from tkinter import *
from tkinter import ttk
import time, subprocess
from tkinter.messagebox import *

root =Tk()
root.title('Créer un compte')
root.iconbitmap('image/icon_jeu.ico')
fenrw = root.winfo_reqwidth()
fenrh = root.winfo_reqheight()
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry("+%d+%d" % ((sw-fenrw)/2, (sh-fenrh)/2))
root.resizable(0,0)

########## Variables #########

nom = StringVar()
mdp = StringVar()
verif_mdp = StringVar()


###### Label et Entré de texte #########

creer=Label(root, text='Créer')
creer.grid(row=0, column=1)

vide=Label(root, text='')
vide.grid(row=5, column=0, columnspan=3,padx=5, pady=5)

nom_txt = Label(root, text='Nom d\'utilisateur: ')
mdp_txt = Label(root, text='Mot de passe: ')
verif_mdp_txt = Label(root, text='Confirmation mot de passe: ')

nom_txt.grid(row=1, column=0, padx=5, pady=5)
mdp_txt.grid(row=2, column=0, padx=5, pady=5)
verif_mdp_txt.grid(row=3, column=0, padx=5, pady=5)

nom_entre=Entry(root, width=30, textvariable=nom)
mdp_entre=Entry(root, width=30, textvariable=mdp, show='*')
verif_mdp_entre=Entry(root, width=30, textvariable=verif_mdp, show='*')

nom_entre.grid(row=1, column=1, padx=5, pady=5)
mdp_entre.grid(row=2, column=1, padx=5, pady=5)
verif_mdp_entre.grid(row=3, column=1, padx=5, pady=5)

##### Boutons #######

bouton_creer= Button(root, text="Créer le compte")
bouton_creer.grid(row=4, column=1, padx=5, pady=5)

bouton_annuler = Button(root, text = "Annuler")
bouton_annuler.grid(row=4, column=0, padx=5, pady=5)

######### Fonctions ##############

def add_compte(fichier,user,password) : # On ajoute dans le fichier une ligne de type : (user,password)
    fichier.write('('+user+','+password+')\n')
    showinfo("Succès", "Bienvenue, votre compte est créé!") # On affiche sur l'écran que le compte a été créer 

def creer():
    global verif_mdp, mdp, nom, vide, nom_txt, nom_entre, verif_mdp_entre, verif_mdp

    # Ouverture des fichiers
    f = open("info/donnees.txt",'a')
    f1 = open("info/donnees.txt",'r')
    lecture = f1.readlines()
    f1.close()
    # Fermeture du 2 eme fichier

    if verif_mdp.get() == "" or mdp.get() == "" or nom.get() == "" : # Si on valide alors qu'il y a rien d'entrée on ne fait rien et on sort de la fonction
        return

    if len(lecture) == 0 : # Le fichier est vide et on a pas besoin de verifier s'il existe des utilisateurs identiques
        if mdp.get()==verif_mdp.get() : #  Les mots de passe sont identiques
            add_compte(f,nom.get(), mdp.get())
            f.close() # Fermeture du fichier
            root.destroy()
            subprocess.call([sys.executable,'./connexion.py'])
            return

        else : # Affichage d'une erreur si les mots de passe sont pas identiques  
            mdp_txt.config(text="Mot de passe*: ")
            verif_mdp_txt.config(text="Confirmation mot de passe*: ")
            mdp_entre.config(bg ='#FF9B9B')
            verif_mdp_entre.config(bg ='#FF9B9B')
            vide.config(text="* : Mots de passe différents")
        f.close() # Fermeture du fichier

    else : # Le fichier n'est pas vide donc on verifie si le nom d'utilisateur 
        for i in lecture: # On parcourt les données du fichiers (stockées dans la variable lecture)
            index_virg=i.index(',')     # On repère la virgule ( car les données sont sous la forme : (user,password) )
            nom_utilise=i[1:index_virg] # On stocke le nom d'utilisateur

            vide.config(text="")

            if nom_utilise==nom.get(): # Affichage d'une erreur si le nom d'utilisateur est déja pris
                nom_txt.config(text="Nom d'utilisateur*: ")
                nom_entre.config(bg ='#FF9B9B')
                vide.config(text="* : Nom déjà pris")
                f.close() # Fermeture du fichier
                return

        if mdp.get()==verif_mdp.get(): # Création du compte si les mdp sont identiques
            add_compte(f,nom.get(), mdp.get())
            f.close() # Fermeture du fichier
            root.destroy()
            subprocess.call([sys.executable,'./connexion.py']) # On relance la page de connexion

        else : # Affichage d'une erreur si les mots de passe sont pas identiques  
                
            mdp_txt.config(text="Mot de passe*: ")
            verif_mdp_txt.config(text="Confirmation mot de passe*: ")
            mdp_entre.config(bg ='#FF9B9B')
            verif_mdp_entre.config(bg ='#FF9B9B')
            vide.config(text="* : Mots de passe différents")

        f.close() # Fermeture du fichier

def annuler() :
    root.destroy()
    subprocess.call([sys.executable, "./connexion.py"])
    
def reset_color(event) :
    global nom_entre,mdp_entre,verif_mdp_entre,vide
    mdp_entre.config(bg ='#FFFFFF')
    verif_mdp_entre.config(bg ='#FFFFFF')
    nom_entre.config(bg ='#FFFFFF')
    vide.config(text = "")


##### Config ########
bouton_creer.config(command = creer)
bouton_annuler.config(command = annuler)

##### Binding #######
nom_entre.bind('<Button-1>' , reset_color)
verif_mdp_entre.bind('<Button-1>' , reset_color)
mdp_entre.bind('<Button-1>' , reset_color)

#Creation de la fenêtre
root.mainloop()
