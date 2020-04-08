package pkg_game;


import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.net.URL;
import java.awt.image.*;

/**
 * @author Jeremy ROS
 * @version 2018
 */
public class UserInterface implements ActionListener
{
    private GameEngine aEngine;
    private JFrame     aMyFrame,aMyFrame2;
    private JTextField aEntryField;
    private JTextArea  aLog;
    private JLabel     aImage;
    private JButton    aButtonQuit,aButtonHelp,aButtonLook;

    /**
     * Construct a UserInterface. As a parameter, a Game Engine
     * (an object processing and executing the game commands) is
     * needed.
     * 
     * @param gameEngine  The GameEngine object implementing the game logic.
     */
    public UserInterface( final GameEngine pGameEngine )
    {
        this.aEngine = pGameEngine;
        this.createGUI();
    } // UserInterface(.)

    /**
     * Print out some text into the text area.
     */
    public void print( final String pText )
    {
        this.aLog.append( pText );
        this.aLog.setCaretPosition( this.aLog.getDocument().getLength() );
    } // print(.)

    /**
     * Print out some text into the text area, followed by a line break.
     */
    public void println( final String pText )
    {
        this.print( pText + "\n" );
    } // println(.)

    /**
     * Show an image file in the interface.
     */
    public void showImage( final String pImageName )
    {
        URL vImageURL = this.getClass().getClassLoader().getResource( pImageName );
        if ( vImageURL == null )
            System.out.println( "image not found" );
        else {
            ImageIcon vIcon = new ImageIcon( vImageURL );
            this.aImage.setIcon( vIcon );
            this.aMyFrame.pack();
        }
    } // showImage(.)

    /**
     * Enable or disable input in the input field.
     */
    public void enable( final boolean pOnOff )
    {
        this.aEntryField.setEditable( pOnOff );
        if ( ! pOnOff )
            this.aEntryField.getCaret().setBlinkRate( 0 );
    } // enable(.)

    /**
     * Set up graphical user interface.
     */
    private void createGUI()
    {
        this.aMyFrame = new JFrame( "Let's save christmas" );
        this.aEntryField = new JTextField( 34 );

        this.aLog = new JTextArea();
        this.aLog.setEditable( false );
        JScrollPane vListScroller = new JScrollPane( this.aLog );
        vListScroller.setPreferredSize( new Dimension(200, 200) );
        vListScroller.setMinimumSize( new Dimension(100,100) );
        
        JPanel vPanel = new JPanel();
        this.aImage = new JLabel();

        vPanel.setLayout( new BorderLayout() );
        vPanel.add( this.aImage, BorderLayout.NORTH );

        vPanel.add( vListScroller, BorderLayout.CENTER );
        vPanel.add( this.aEntryField, BorderLayout.SOUTH );

        this.aMyFrame.getContentPane().add( vPanel, BorderLayout.CENTER );

        // add some event listeners to some components
        this.aMyFrame.addWindowListener( new WindowAdapter() {
            public void windowClosing(WindowEvent e) { System.exit(0); }
        } );

        this.aEntryField.addActionListener( this );

        this.aMyFrame.pack();
        this.aMyFrame.setVisible( true );
        this.aEntryField.requestFocus();
        
        aButtonQuit= new JButton("quit");
        this.aMyFrame.getContentPane().add(this.aButtonQuit,BorderLayout.NORTH);
        aButtonQuit.setActionCommand("quit");
        aButtonQuit.addActionListener(this);
        
        aButtonHelp= new JButton("help");
        this.aMyFrame.getContentPane().add(this.aButtonHelp,BorderLayout.SOUTH);
        aButtonHelp.setActionCommand("help");
        aButtonHelp.addActionListener(this);
        
        aButtonLook= new JButton("look");
        this.aMyFrame.getContentPane().add(this.aButtonLook,BorderLayout.EAST);
        aButtonLook.setActionCommand("look");
        aButtonLook.addActionListener(this);
        
        
        
        
       
    } // createGUI()
   

    /**
     * Actionlistener interface for entry textfield.
     */
    public void actionPerformed( final ActionEvent pE ) 
    {
        // no need to check the type of action at the moment.
        // there is only one possible action: text entry
        
        if(pE.getSource()==aButtonLook)
            this.aEngine.interpretCommand("look");
        else if(pE.getSource()==aButtonHelp)
            this.aEngine.interpretCommand("help");
        else if(pE.getSource()==aButtonQuit)
            this.aEngine.interpretCommand("quit");
        else this.processCommand();
    } // actionPerformed(.)

    /**
     * A command has been entered. Read the command and do whatever is 
     * necessary to process it.
     */
    private void processCommand()
    {
        String vInput = this.aEntryField.getText();
        this.aEntryField.setText( "" );

        this.aEngine.interpretCommand( vInput );
    } // processCommand()
} // UserInterface 
