import pkg_game.UserInterface;
import pkg_game.GameEngine;


/**
 * @author Jeremy ROS
 * @version 2018
 */
public class Game
{
	private UserInterface gui;
	private GameEngine engine;

    /**
     * Création de la partie
     */
    public Game() 
    {
		engine = new GameEngine();
		gui = new UserInterface(engine);
		engine.setGUI(gui);
    }
}
