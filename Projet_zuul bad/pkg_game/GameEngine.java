package pkg_game;

import pkg_commands.Parser;
import pkg_room.Room;
import pkg_item.Item;
import pkg_commands.Command;

import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Stack;
import java.util.HashMap;
/**
 * @author Jeremy ROS
 * @version 2018
 */

public class GameEngine
{
    private Parser aParser;
    private Room aCurrentRoom;
    private UserInterface gui;
    private Room aPreviousRoom;
    private Stack<Room> aStackRoom;
    
    
    
    

    /**
     * Constructeur
     */
    public GameEngine()
    {
        this.aParser = new Parser();
        createRooms();
        this.aStackRoom = new Stack<Room>();

        

       
    }

    public void setGUI(UserInterface userInterface)
    {
        gui = userInterface;
        printWelcome();
    }
    
    /**
     * Affiche le message de bienvenue
     */
    private void printWelcome()
    {
        gui.println("\"Let's save Christmas\"");
        gui.println("Welcome to the World of Santa claus!");
        gui.println("You have to protect the magic of Christmas.");
        gui.println("Type 'help' if you need help.");
        gui.println("");
        gui.println("");
        gui.println(this.aCurrentRoom.getLongDescription());
        gui.showImage(this.aCurrentRoom.getImageName());
        
    }
    
    /**
         * Création des rooms et des items
    */
        
    private void createRooms()//Cette méthode nous permet de créer les pièce différentes du jeu 
    {
        Item vCoffre=new Item("Box",5.0,"This box is old and mysterious");
        Item vChoco=new Item("Chocolate",0.1,"This chocolate looks yummy");
        Item vBonbon=new Item("Candy",0.1,"This candy looks yummy");
        Item vLettre=new Item("Letter",0.5,"No information");
        Item vBois=new Item("Wood",1,"It's wood, nothing special");
        Item vPelle=new Item("Shovel",6,"A dirty shovel");
        Item vGant=new Item("Gloves",0.5,"Nothing special about these gloves");
        Item vBotte=new Item("Boots",0.5,"Nothing special about these boots");
        Item vManteau=new Item("Coat",0.8,"Nothing special about this coat" );
        Item vSapin=new Item("Christmas tree",10,"Magic tree");
        Item vLoukoum=new Item("Loukoum",0.5,"Looks yummy");
        Item vVin=new Item("Wine",2,"You should be powerful drinking this");
        
        
        
        //Création de nos pièces
        Room vZone=new Room("the takeoff area","zone.png");
        Room vAccueil=new Room("the reception","accueil.png");
        Room vJardin=new Room("the garden","jardin.png");
        Room vCave=new Room("the cavern","cave.png");
        Room vFabrique=new Room("the toy factory","Fabrique.png");
        Room vChambresanta=new Room("the Santa Claus's room","Chambre.png");
        Room vDortoire=new Room("the elfes'dormitory","Dortoire.png");
        Room vCouloir1=new Room("the hallway","Hallway.png");
        Room vCouloir2=new Room("the hallway","Hallway.png");
        Room vCouloir3=new Room("the hallway","Hallway.png");
        Room vCouloir4=new Room("the hallway","Hallway.png");
        Room vOutside=new Room("the snowy forest","Foret.png");
        
        vZone.setItem(vCoffre);
        vDortoire.setItem(vChoco);
        vAccueil.setItem(vChoco);
        vOutside.setItem(vChoco);
        vAccueil.setItem(vLettre);
        vOutside.setItem(vBois);
        vFabrique.setItem(vBois);
        vCave.setItem(vBois);
        vJardin.setItem(vBois);
        vOutside.setItem(vPelle);
        vDortoire.setItem(vGant);
        vAccueil.setItem(vBotte);
        vZone.setItem(vManteau);
        vJardin.setItem(vSapin);
        vAccueil.setItem(vLoukoum);
        vCouloir1.setItem(vLoukoum);
        vCouloir2.setItem(vLoukoum);
        vCouloir3.setItem(vLoukoum);
        vCouloir4.setItem(vLoukoum);
        vDortoire.setItem(vVin);
        
        //On détermine les sorties de chaque pièces
        vZone.setExit("west",vAccueil);
        vAccueil.setExit("north",vCouloir1);
        vAccueil.setExit("east",vZone);
        vAccueil.setExit("west",vCouloir4);
        vAccueil.setExit("south",vCouloir3);
        vJardin.setExit("north",vZone);
        vCave.setExit("up",vCouloir4);
        vCave.setExit("west",vOutside);
        vOutside.setExit("east", vCave);
        vFabrique.setExit("down",vCouloir4);
        vChambresanta.setExit("east",vDortoire);
        vDortoire.setExit("east",vCouloir3);
        vDortoire.setExit("west",vChambresanta);
        vCouloir1.setExit("south",vAccueil);
        vCouloir1.setExit("west",vCouloir2);
        vCouloir2.setExit("east",vCouloir1);
        vCouloir2.setExit("south",vChambresanta);
        vCouloir3.setExit("west",vDortoire);
        vCouloir3.setExit("north",vAccueil);
        vCouloir4.setExit("down",vCave);
        vCouloir4.setExit("up",vFabrique);
        vCouloir4.setExit("east",vAccueil);
        

        
        //Lorsqu'on lance le jeu on se trouve dans cette pièce
        this.aCurrentRoom = vDortoire;
    }
      
   /** 
    * On change de room/pièce
    */
   public void goRoom(Command command) 
   {
     if(!command.hasSecondWord()) {
       // if there is no second word, we don't know where to go...
       gui.println("Go where?");
       return;
   }

        String direction = command.getSecondWord();

        // Try to leave current room.
        Room nextRoom = aCurrentRoom.getExit(direction);
        
        if (nextRoom == null)
            gui.println("There is no door!");
        else {
            this.aStackRoom.push(this.aCurrentRoom);
            this.aCurrentRoom = nextRoom;
            gui.println(aCurrentRoom.getLongDescription());

            if(aCurrentRoom.getImageName() != null)
                gui.showImage(aCurrentRoom.getImageName());
        }
    }
    
    /**
     * Selon la commande, on éxécute des instructions
     */
    public void interpretCommand(String commandLine) 
    {
        gui.println(commandLine);
        Command command = aParser.getCommand(commandLine);

        if(command.isUnknown()) {
            gui.println("I don't know what you mean...");
            return;
        }
        
        String commandWord = command.getCommandWord();
        
        if (commandWord.equals("help"))
            printHelp();
        else if (commandWord.equals("test"))
            test(command);
        else if (commandWord.equals("back"))
            back();
        else if (commandWord.equals("go"))
            goRoom(command);
        else if(commandWord.equals("look"))
            look();
        else if (commandWord.equals("quit")) {
            if(command.hasSecondWord())
                gui.println("Quit what?");
            else
                endGame();
        }
    }
    
    /**
   * Reviens en arrière et si cela n'est pas possible, on affiche un message d'erreur
   */
  public void back()
  {
        if( !aStackRoom.isEmpty())
        {    
            this.aCurrentRoom = aStackRoom.pop();
            gui.println(aCurrentRoom.getLongDescription());
            if(aCurrentRoom.getImageName() != null)
                gui.showImage(aCurrentRoom.getImageName());
        }
        else
            gui.println("You can't back anymore");
          
  }
    // implementations of user commands:

    /**
     * Affiche de l'aide qui contient les commandes possibles et une phrase qui décrit la situation
     */
    private void printHelp() 
    {
        gui.println("You just woke up. It's soon christmas and \n you have to take care of it !");
        gui.println("There is some problem in the factory. \nYou have to resolve it , otherwise there won't \nbe Christmas this year \n \n ");
        gui.println("Your command words are:");
        //On appel la méthode qui se trouve dans la classe Parser pour afficher les commandes possibles
        gui.println(aParser.showCommands());
    }

    /**
    * Message lorsque la partie se termine
    */
    private void endGame()
    {
        gui.println("Thank you for playing.  Good bye.");
        gui.enable(false);
    }
    
    /**
     * Affiche les informations de la room où nous sommes
     */
    public  void look()
    {
        gui.println(aCurrentRoom.getLongDescription());
    }
    
    /**
     * On effectue tous les commandes dans le fichier
     */
    public void  test( final Command pNomFichier )
    {
        String vNomFichier = pNomFichier.getSecondWord();
        if(!pNomFichier.hasSecondWord())
        { 
            gui.println("File missing"); 
            
        } 
        
        Scanner vSc=null;
        try 
        {
            vSc = new Scanner ( new File (vNomFichier));
            while(vSc.hasNextLine())
        { 
            String vLine = vSc.nextLine();
            interpretCommand(vSc.nextLine());
        }
        
                 
        }
        catch ( final FileNotFoundException pFNFE )
        {
            gui.println("File not found");
            
        }
        
        
    }
    
}
