package pkg_commands;

/**
 * @author Jeremy ROS
 * @version 2018
 */
public class CommandWords
{
    // un tableau qui contient toutes les commandes valides
    private static final String validCommands[] = {
        "go", "quit", "help" , "look" , "back" , "test"
    };

    /**
     * Constructeur
     */
    public CommandWords()
    {
        // nothing to do at the moment...
    }

    /**
     * Vérifie si la commande est valide
     **/
    public boolean isCommand(String aString)
    {
        for(int i = 0; i < validCommands.length; i++) {
            if(validCommands[i].equals(aString))
                return true;
        }
        
        return false; //-> string qui n'est pas une commande connue
    }

    /**
     * retourne les string des commandes contenu dans le tableau validCommands[]
     */
    public String getCommandList() 
    {
        StringBuilder commands = new StringBuilder();
        for(int i = 0; i < validCommands.length; i++) {
            commands.append( validCommands[i] + "  " );
        }
        return commands.toString();
    }
}
