

import java.awt.image.BufferedImage;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.io.File;
import java.awt.Color;
import java.io.FileOutputStream;
import java.io.OutputStream;
// Source du site pour comprendre le fonctionnement du SeamCarving 
// https://www.cs.princeton.edu/courses/archive/spr13/cos226/assignments/seamCarving.html


// Mettez l'image que vous voulez réduire  dans le meme dossier que SeamCarving.java.

public class SeamCarving{
    private BufferedImage image;

    /*
    * Constructeur par defaut
    * @param String nom_fichier : Nom du fichier que l'on va lire.
    * @throws IOException : On ne peut pas lire le fichier car celui-ci n'existe pas.
    */
    public SeamCarving(String nom_fichier){
        try{
            File input = new File(nom_fichier);
            this.image = ImageIO.read(input);
            System.out.println("Lecture du fichier reussi");    
        }
        catch(IOException e){
            System.out.println("Erreur dans la lecture du fichier suivant : " + nom_fichier);
        }
    }

    /*
    * La fonction converti une image en un tableau contenant 3 tableau de 2 dimensions
    * @param BufferedImage imagep : L'image qu'on va transcrire dans un tableau 3D
    * @return : Un talbeau qui contient 3 tableau correspondant au valeurs Red dans le 1er, Green dans le 2eme et Blue dans le 3eme. 
    */
    static int [][][]convertImageToArray(BufferedImage imagep){ // Transcription de l'image dans un tableau pour mieux manipuler
        int w = imagep.getWidth(), h = imagep.getHeight();
        int [][]red = new int[h][w], green = new int[h][w], blue = new int[h][w];
        int [][][] res = {red,green,blue};

        // Chaque case de chaque tableau contiendra la valeur R, G ou B en fonction du tableau 
        for(int hp = 0; hp < h; hp++){
            for(int wp = 0; wp < w; wp++){
                Color c = new Color(imagep.getRGB(wp, hp));
                red[hp][wp] = c.getRed();
                green[hp][wp] = c.getGreen();
                blue[hp][wp] = c.getBlue();
            }
        }
        return res;
    }

    /*
    * La fonction converti un tableau en une image
    * @param int[][][] arrayImage : Un tableau 3D contenant le 1er tableau contenant les valeurs R, le 2eme contenant les valeurs G et le 3eme contenant les valeurs B. ( RGB )
    * @return Buffered newImage : Une image 
    */
    static BufferedImage convertArrayToImage(int[][][] arrayImage){
        int [][]red = arrayImage[0], green = arrayImage[1], blue = arrayImage[2];
        int w = red[0].length, h = red.length;
        BufferedImage newImage = new BufferedImage(w,h, BufferedImage.TYPE_INT_RGB);
        
        //On associe chaque pixel à sa valeur RGB contenu dans arrayImage
        for(int hp = 0; hp < h; hp++){
            for(int wp = 0; wp < w; wp++){
                int r = red[hp][wp], g = green[hp][wp], b = blue[hp][wp];
                int rgb = (r << 16) | (g << 8) | b;
                newImage.setRGB(wp, hp, rgb);
            }
        }
        return newImage;
    }

    /*
    * La procédure créer un fichier contenant une image
    * @param BufferedImage imagep : Image qui sera stocke dans le fichier
    * String []command : Chaîne de caractères qui contient la ligne de commande 
    */
    static void createImage(BufferedImage imagep, String []command){ 
        try{
            String nomF = command[0];
            String rx = command[1];
            String ry = command[2];
            // Nom du fichier sans ".png"
            String newName = nomF.substring(0,nomF.length()-4); 

            File file = new File(newName+"_resized_"+rx+"_"+ry+".png");
            
            OutputStream out = new FileOutputStream(file);
            ImageIO.write(imagep, "png", file);
            out.close();
           
            System.out.println("Redimensionnement reussi");

        }catch(IOException e){ System.out.println("Erreur");}
    }

    /*
    * La fonction qui calcul l'energie de chaque pixel
    * @param int [][][]arrayImage : L'image, converti sous forme de tableau, contenant les valeurs RGB
    * @return int [][]E : un tableau contenant l'energie de chaque pixel
    */
    static int[][] calculEnergie(int [][][]arrayImage){
        int [][]red = arrayImage[0];
        int w = red[0].length, h = red.length;
        int [][]E = new int[h][w];

        for(int hp = 0; hp < h; hp++){
            for(int wp = 0; wp < w; wp++){
                //Calcul du gradient à l'horizontal
                int droite_gauche = calculPixelDG(arrayImage,wp,hp);
                //Calcul du gradient à la vertical
                int haut_bas = calculPixelHB(arrayImage,wp,hp);
                //Addition du gradient à l'horizontal et du gradient à la vertical 
                E[hp][wp] = droite_gauche + haut_bas;
            }
        }
        return E;
    }

    /*
    * La fonction qui calcul le gradient à l'horizontal
    * @param int [][][]arrayImage : L'image, converti sous forme de tableau, contenant les valeurs RGB
    * int w : coordonées à l'abscisse du pixel où l'on veut calculer son gradient/energie
    * int h : coordonées à l'ordonné du pixel où l'on veut calculer son gradient/energie
    * @return La valeur du  gradient à l'horizontal
    */
    static int calculPixelDG(int [][][]arrayImage, int w, int h){
        int [][]red = arrayImage[0], green = arrayImage[1], blue = arrayImage[2];
        int width = red[0].length;

        int RD = 0, GD = 0, BD = 0;
        int RG = 0, GG = 0, BG = 0;
        
        //Cas où le pixel se trouve en bordure 
        if(w != width-1){
            RD = red[h][w+1];
            GD = green[h][w+1];
            BD = blue[h][w+1];
        //Cas où le pixel se trouve "pas" en bordure 
        }else{
            RD = red[h][0];
            GD = green[h][0];
            BD = blue[h][0];
        }
        //Cas où le pixel se trouve en bordure 
        if(w != 0){
            RG = red[h][w-1];
            GG = green[h][w-1];
            BG = blue[h][w-1];
        }
        //Cas où le pixel se trouve "pas" en bordure 
        else{
            RG = red[h][width-1];
            GG = green[h][width-1];
            BG = blue[h][width-1];
        }
        
        int R = RG - RD,G = GG - GD,B = BG - BD;

        return (int)Math.pow(R,2)+(int)Math.pow(G,2)+(int)Math.pow(B,2);
    }

    /*
    * La fonction qui le calcul le gradient à la vertical
    * @param int [][][]arrayImage : L'image, converti sous forme de tableau, contenant les valeurs RGB
    * int w : coordonées à l'abscisse du pixel où l'on veut calculer son gradient/energie
    * int h : coordonées à l'ordonné du pixel où l'on veut calculer son gradient/energie
    * @return : La valeur du gradient à la vertical
    */
    static int calculPixelHB(int [][][]arrayImage, int w, int h){
        int [][]red = arrayImage[0], green = arrayImage[1], blue = arrayImage[2];
        int height = red.length;

        int RB = 0, GB = 0, BB = 0;
        int RH = 0, GH = 0, BH = 0;
        //Cas où le pixel se trouve en bordure 
        if(h != height-1){
            RH = red[h+1][w];
            GH = green[h+1][w];
            BH = blue[h+1][w];

        //Cas où le pixel se trouve "pas" en bordure 
        }else{
            RH = red[0][w];
            GH = green[0][w];
            BH = blue[0][w];
        }

        //Cas où le pixel se trouve en bordure 
        if(h != 0){
            RB = red[h-1][w];
            GB = green[h-1][w];
            BB = blue[h-1][w];

        //Cas où le pixel se trouve "pas" en bordure 
        }else{
            RB = red[height-1][w];
            GB = green[height-1][w];
            BB = blue[height-1][w];
        }

        int R = RH - RB, G = GH - GB, B = BH - BB;
        return (int)Math.pow(R,2)+(int)Math.pow(G,2)+(int)Math.pow(B,2);
    }
 
    /* Les 3 methode suivantes vont nous permettre de savoir les valeurs des 3 cases adjacentes et precedentes dans M. */
    static int N(int lp, int cp,int [][]Mp) { 
        // Aucun probleme d'indice
        return Mp[lp - 1][cp];
    }

    static int NE(int lp, int cp,int [][]Mp) { 
        // Problème d'indice dans le cas où la colonne vaut 0
        if (cp == 0) {
            return -1;
        }
        return Mp[lp - 1][cp - 1];
    }

    static int NO(int lp, int cp,int [][]Mp) { 
        // Problème d'indice dans le cas où la colonne se situe au bord max du tableau.
        if (cp == Mp[0].length-1) {
            return -1;
        }
        return Mp[lp - 1][cp + 1];
    }

    /*
    * La fonction qui le calcul le tableau M ( Energie minimum en allant d'une case de la ligne 0 jusqu'à j tel que 0 <= j <= l )
    * @param int [][]ep : tableau contenant ici l'energie de chaque pixel 
    * @return : Le tableau M
    */
    static int[][] calculM(int [][]ep) {
        int width = ep[0].length, height = ep.length;
        int [][]Mp = new int[height][width];
        // Cas de base : m(0,cp) = g(0,cp) avec 0 <= cp < c.  
        Mp[0] = ep[0]; 
                          
        int lpp = height-1;
        int cpp = width-1;

        // Cas general : m(lp,cp) = min( m(lp-1, cp-1), m(lp-1, cp), m(lp-1, cp+1) ) + g(lp,cp) si 0 < cp < c-1
        //               m(lp,cp) = min( m(lp-1, cp), m(lp-1, cp+1) ) + g(lp,cp) si cp = 0
        //               m(lp,cp) = min( m(lp-1, cp-1), m(lp-1, cp) ) + g(lp,cp) si cp = c-1
        for (int lp = 1; lp <= lpp; lp++) {
            for (int cp = 0; cp <= cpp; cp++) {
                 int Mn = N(lp, cp, Mp) + ep[lp][cp]; // Somme d'énergie des pixels en venant du nord
                                                           
                 int Mno = NO(lp, cp, Mp) + ep[lp][cp]; // Somme d'énergie des pixels en venant de l'ouest
                                                             
                 int Mne = NE(lp, cp, Mp) + ep[lp][cp]; // Somme d'énergie des pixels en venant de l'est
                                                             
                Mp[lp][cp] = (int) Math.min(Mne, (int) Math.min(Mn, Mno)); 

                // Cas où il y a seulement 2 pixels adjacent et précédent.
                if(NE(lp, cp, Mp) == -1){ // cp = 0
                    Mp[lp][cp] = (int) Math.min(Mn, Mno);
                }
                if(NO(lp, cp,Mp) == -1){ // cp = c-1
                    Mp[lp][cp] = (int) Math.min(Mn, Mne);
                }
            }
        }
        return Mp;
    }

    /*
    * La fonction qui recherche le minimum de la derniere ligne d'un tableau 2D.
    * @param int [][]Mp : tableau contenant M ( Energie minimum en allant d'une case de la ligne 0 jusqu'à j tel que 0 <= j <= l ).
    * @return : Le minimum et sa colonne.
    */
    static int[] Min_colonne(int [][]Mp) {

        int cp = 0;
        int lpp = Mp.length-1;

        // Cas de base : Le minimum d'un tableau contenant 1 valeur est le 1er element de ce tableau.
        int min = Mp[lpp][cp]; 

        // min = min(min, m(l-1,i)) avec 1 <= i <= c-1
        for (int i = 1; i <= Mp[0].length-1; i++){
            if (!(min == Math.min(min, Mp[lpp][i]))){ 
                min = Mp[lpp][i];
                cp = i;
            }
        }

        return new int[]{min,cp};
    }

    /*
    * La fonction qui recherche une valeur parmi 3 valeurs adjacente et precedente à un pixel.
    * @param int valeur : la valeur que l'on recherche
    *        int ligne : La ligne où se situe la valeur qu'on recherche
    *        int colonne : La colonne où se situe le pixel precedent
    *        int [][]Mp : Tableau dans lequel on va chercher la valeur
    * @return : L'indice de la colonne où se situe la valeur qu'on recherche
    */
    static int ind_x( int valeur, int ligne, int colonne, int [][]Mp) { 
        int x = 0;
        int cp = Mp[0].length;
        int ip = colonne -1;
        int ipp = colonne +1;

        // La colonne correspond à la colonne où se situe le max de la ligne +1 et on recherche seulement les 3 cases en dessous de celle ci
            // On regarde seulement le sud et sud-est de la case max de la ligne+1
        if(colonne == 0){ ip = 0;} 
            // On regarde seulement le sud et sud-ouest de la case max de la ligne+1
        if(colonne == cp-1){ ipp = cp-1;} 

        for ( int i = ip; i <= ipp; i++) { 
            if (Mp[ligne][i] == valeur) {
                x = i;
                break;
            }
        }
        return x;
    }

    /*
    * La procedure qui recherche le chemin minimum.
    * @param int lp : ligne où on recherche la case precedente.
    *        int cp : colonne où on recherche la case precedente.
    *        int [][]energiep : tableau 2d contenant l'energie de chaque pixel.
    *        int [][]Mp : tableau 2d contenant M ( Energie minimum en allant d'une case de la ligne 0 jusqu'à j tel que 0 <= j <= l ).
    *        int [][][]array : tableau 3d contenant 3 tableau representant l'image ( Tableau 1 : valeurs R, tableau 2 : valeurs G, tableau 3 : valeurs B).
    */
    static void CheminMin(int lp, int cp, int[][]energiep, int[][]Mp, int[][][]array) {
        int [][]R = array[0];int [][]G = array[1];int [][]B = array[2];

        // Fin
        if (lp == 0) {
            
            R[lp][cp] = Integer.MAX_VALUE;
            G[lp][cp] = Integer.MAX_VALUE;
            B[lp][cp] = Integer.MAX_VALUE;
           
        } 
        else {
            // Valeur de la case suivante 
            int v = Mp[lp][cp] - energiep[lp][cp];
            // On cherche les coordonnees de la valeur dans M pour la ligne-1.
            int vx = ind_x(v, lp - 1, cp, Mp); 
             
            CheminMin(lp - 1, vx, energiep, Mp,array);

            R[lp][cp] = Integer.MAX_VALUE;
            G[lp][cp] = Integer.MAX_VALUE;
            B[lp][cp] = Integer.MAX_VALUE;
        }
    }

    /*
    * La procedure qui calcul le chemin en faisant appel à la fonction CheminMin
    * @param int [][]energiep : tableau 2d contenant l'energie de chaque pixel.
    *        int [][]Mp : tableau 2d contenant M ( Energie minimum en allant d'une case de la ligne 0 jusqu'à j tel que 0 <= j <= l ).
    *        int [][][]array : tableau 3d contenant 3 tableau representant l'image ( Tableau 1 : valeurs R, tableau 2 : valeurs G, tableau 3 : valeurs B).
    */
    static void calculChemin(int [][]Mp,int [][]Ep,int [][][]array) {
        
        // Colonne du min
        int c_min = Min_colonne(Mp)[1]; 
        int lp = Mp.length-1;
        // Recherche du chemin à partir de la seam minimale.
        CheminMin(lp, c_min,Ep,Mp,array); 
    }
    
    /*
    * La fonction qui supprime une seam.
    * @param int [][]array : Un tableau contenant des valeurs valant Integer.Max_Value à supprimer.
    * @return : Un nouveau tableau contenant l'image (converti en tableau) après avoir enleve la seam minimale.
    */
    static int[][] deleteSeam(int [][]array){
        int l = array.length-1;
        int c = array[0].length-1;
        int [][] copyArray = new int[l+1][c];
        
        for(int lp = 0; lp <= l; lp++){
            // Valeur qui passera a True quand on tombe sur l'element à supprimer.
            Boolean supp = false;
            for(int cp = 0; cp < c; cp++){
                if( array[lp][cp] == Integer.MAX_VALUE){
                    supp = true;
                }
                //Copie des elements avant la case à supprimer.
                if(supp == false){
                    copyArray[lp][cp] = array[lp][cp];
                }
                //Copie des elements après la case à supprimer.
                else{
                    copyArray[lp][cp] = array[lp][cp+1];
                }
            }
        }
        return copyArray;
    }

    /*
    * La fonction rotation_90 l'image(deja converti dans un tableau) à 90° 
    * @param int [][][]array : tableau 3d contenant 3 tableau representant l'image (Tableau 1 : valeurs R, tableau 2 : valeurs G, tableau 3 : valeurs B).
    * @return : Un nouveau tableau contenant l'image (converti en tableau).
    */
    static int[][][] rotation_90(int [][][]array){
        int [][]R = array[0]; int [][]G = array[1]; int [][]B = array[2];
        int width = R[0].length; int height = R.length;
        int [][]R_copy = new int[width][height]; int [][]G_copy = new int[width][height]; int [][]B_copy = new int[width][height];

        //Rotation de l'image à 90° en echangeant les valeurs de la colonne et de la ligne
        for(int wp = 0; wp <= height-1; wp++){
            for(int hp = 0; hp <= width -1; hp++){
                R_copy[hp][wp] = R[wp][hp];
                G_copy[hp][wp] = G[wp][hp];
                B_copy[hp][wp] = B[wp][hp];
            }
        }
        return new int[][][]{R_copy,G_copy,B_copy};
    }

    /*
    * La fonction qui reduit l'image selon le nombre de pixel en largeur et longueur que l'on doit enlever. 
    * @param int [][][]array : tableau 3d contenant 3 tableau representant l'image (Tableau 1 : valeurs R, tableau 2 : valeurs G, tableau 3 : valeurs B).
    *        int h : nombre de seam (chemin de pixels) à l'horizontal que l'on doit enlever.
    *        int h : nombre de seam (chemin de pixels) à la vertical que l'on doit enlever.
    * @return L'image, après reduction, sous forme d'un tableau 3d contenant 3 tableau representant l'image (Tableau 1 : valeurs R, tableau 2 : valeurs G, tableau 3 : valeurs B).
    */
    static int[][][] reduction(int [][][]array, int h, int v){
        //Initialisation des differents tableaux.
        int [][][]copyArray = array;
        int [][][]verticalArray; int [][][]horizontalArray;
        int [][]EV; int [][]EH;
        int [][]MV; int [][]MH;
        int [][]R;int [][]G;int [][]B;
        //Nombre de chemin au total à supprimer
        int N = h+v;

        for(int i = N; i > 0; i--){
            verticalArray = copyArray;
            horizontalArray = rotation_90(copyArray);

            EV = calculEnergie(verticalArray);
            EH = calculEnergie(horizontalArray);

            MV = calculM(EV);
            MH = calculM(EH);

            int min_MV = Min_colonne(MV)[0];
            int min_MH = Min_colonne(MH)[0];

            // On supprime la seam minimale entre la seam horizontal et vertical.
                // Seam horizontale
            if((Math.min(min_MH,min_MV) == min_MH && h != 0) || v == 0 ){
                calculChemin(MH, EH, horizontalArray);
                R = horizontalArray[0];
                G = horizontalArray[1];
                B = horizontalArray[2];
                copyArray = new int[][][]{deleteSeam(R),deleteSeam(G),deleteSeam(B)};
                copyArray = rotation_90(copyArray);
                // Nombre de seams horizontales restantes à supprimer
                h = h-1;
            }
                // Seam verticale
            if((Math.min(min_MH,min_MV) == min_MV && v != 0) || h == 0){
                calculChemin(MV, EV, verticalArray);
                R = verticalArray[0];
                G = verticalArray[1];
                B = verticalArray[2];
                copyArray = new int[][][]{deleteSeam(R),deleteSeam(G),deleteSeam(B)};
                // Nombre de seams verticales restantes à supprimer.
                v = v-1;
            }
             
        }
        return copyArray;
    }

    /*
    * La fonction qui retourne le nombre de seams à l'horizontal et à la verticale que l'on doit supprimer
    * @param SeamCarving Sp : L'objet SeamCarving contenant l'image d'origine
    *        String []command : Ligne de commande du terminal
    * @return Le nombre de seams à l'horizontal et à la verticale que l'on doit supprimer dans un tableau
    */
    static int[] getPixelReduction(SeamCarving Sp, String []command){

        // On recupere la largeur de l'image et la longueur de l'image
        int width = Sp.image.getWidth(); 
        int height = Sp.image.getHeight();

        int rpx = Integer.parseInt(command[1]); int rpy = Integer.parseInt(command[2]); 
        
        // Nombre de seam en largeur et longueur que l'on doit retirer
        int w = (int)(width * ((double)rpx/100)); 
        int h = (int)(height * ((double)rpy/100)); 

        return new int[]{w,h};
    }

   public static void main(String[] args) {

    // On recupere le nom du fichier
    String nom_fichier = args[0]; 
 
    SeamCarving echantillon = new SeamCarving(nom_fichier); 
    
    // On recupere le nombre de seam(chemin de pixel) en largeur et longueur que l'on doit retirer
    int w = getPixelReduction(echantillon,args)[0]; 
    int h = getPixelReduction(echantillon,args)[1]; 
    
    // On recupere l'image du fichier
    BufferedImage image = echantillon.image; 
    
    // On transforme l'image en plusieurs tableau qui contiendra les valeurs RGB
    int [][][]arrayImage = convertImageToArray(image); 

    // On redimensionne l'image originale en fonction de h et w ( toujours en manipulant des arrays)
    int [][][]finalArrayImage = reduction(arrayImage, h, w); 
    
     // On transforme les tableaux en une image
    BufferedImage finalImage = convertArrayToImage(finalArrayImage);
   
    // On enregistre l'image en .png et sous forme suivante : NomDuFichier_w_h.png
    createImage(finalImage, args); 
    System.out.println("Image d'origine : "+image.getWidth()+"x"+image.getHeight());
    System.out.println("Image reduite : "+finalImage.getWidth()+"x"+finalImage.getHeight());
   }
}