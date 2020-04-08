package pkg_commands;


import java.util.StringTokenizer;
/**
 * @author Jeremy ROS
 * @version 2018
 */


public class Parser 
{

    private CommandWords aCommandWords;  // holds all valid command words

    /**
     * Create a new Parser.
     */
    public Parser() 
    {
        this.aCommandWords = new CommandWords();
    } // Parser()

    /**
     * Get a new command from the user. The command is read by
     * parsing the 'inputLine'.
     */
    public Command getCommand( final String pInputLine ) 
    {
        String vWord1;
        String vWord2;

        StringTokenizer tokenizer = new StringTokenizer( pInputLine );

        if ( tokenizer.hasMoreTokens() )
            vWord1 = tokenizer.nextToken();      // get first word
        else
            vWord1 = null;

        if ( tokenizer.hasMoreTokens() )
            vWord2 = tokenizer.nextToken();      // get second word
        else
            vWord2 = null;

        // note: we just ignore the rest of the input line.

        // Now check whether this word is known. If so, create a command
        // with it. If not, create a "null" command (for unknown command).

        if ( this.aCommandWords.isCommand( vWord1 ) )
            return new Command( vWord1, vWord2 );
        else
            return new Command( null, vWord2 );
    } // getCommand(.)

    /**
     * Returns a String with valid command words.
     */
    public String showCommands() // bad name for this method !
    {
        return this.aCommandWords.getCommandList();
    } // showCommands() // bad name for this method !

} // Parser
