package pkg_item;

import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;

/**
 * @author Jeremy ROS
 * @version 2018
 */
public class Item 
{
    private String aItemDescription;
    private String aItemName;
    private double aPoids;
    
    
    /**
     * Constructeur décrivant le nom de l'item, la quantité de cet item, et son poids
     */
    public Item(final String pItemName,final double pPoids, final String pItemDescription)
    {
        this.aPoids=pPoids;
        this.aItemDescription=pItemDescription;
        this.aItemName=pItemName;
        
        
    }
    
    /**
     * Retourne le nom de l'item
     */
    public String getItemName()
    {
        return this.aItemName;
    }
    
    /**
     * Retourne le poid de l'Item
     */
    public double getPoids()
    {
        return this.aPoids;
    }
    
    /**
     * Retourne la description de l'item
     */
    public String getItemDescription()
    {
        return this.aItemDescription;
    }
    
    
    
    
    
}
