package pkg_room;

import pkg_item.Item;
import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;

/**
 * @author Jeremy ROS
 * @version 2018
 */

public class Room
{
    private String description;
    private HashMap<String,Room> exits;
    private HashMap<String,Item> items;
    private Item aItem;
    private String imageName;

    /**
     * Création d'une room ayant une description et une image  
     */
    public Room(String description, String image) 
    {
        this.description = description;
        this.exits = new HashMap<String,Room>();
        this.imageName = image;
        this.items = new HashMap<String,Item>();
        
        
        
    }

    /**
     * Défini une sortie
     */
    public void setExit(String direction, Room neighbor) 
    {
        exits.put(direction, neighbor);
    }

    /**
     * Getter qui nous retourne le nom de la pièce que l'on veut connaître
    */
    public String getShortDescription()
    {
        return description;
    }

    /**On retourne les sorties possibles*/
    public String getLongDescription()
    {
        return "You are " + description + ".\n" + getExitString()+"\n"+getItemString();
    }

    /** Retourne les sorties de la room en fonction de quelle room nous sommes */
    private String getExitString()
    {
        StringBuilder returnString = new StringBuilder( "Exits:" );
        for ( String vS : exits.keySet() )
            returnString.append( " " + vS );
        return returnString.toString();
    }

    /**
     * Retourne la room en fonction de la direction que l'on donne
     * Si il n'y a aucune room dans la direction donnée alors return null
     */
    public Room getExit(String direction) 
    {
        return exits.get(direction);
    }

    /**
     * Retourne une string décrivant le nom de l'image
     */
    public String getImageName()
    {
        return imageName;
    }
    
    /**
     * Retourne les items qui se trouvent dans la room 
     */
    public String getItemString()
    {
        StringBuilder returnItemString = new StringBuilder( "Items:" );
        for ( String vS : items.keySet() )
            returnItemString.append( " " + vS );
            
        return returnItemString.toString();
    }
    
    /**
     * On associe pour chaque nom d'item un Item
     */
    public void setItem ( final Item pItem )
    {
        items.put(pItem.getItemName(), pItem);
    }
    
    
}
