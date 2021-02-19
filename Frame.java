import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class Frame extends JFrame implements ActionListener {

    private static final int width = 715;
    private static final int height = 550;
    static String[] frequency;
    private JTextArea inputTextArea;
    private JList frequencyList;


    public Frame() {

        setTitle("WordCount");
        setSize(width, height);
        setLocationRelativeTo(null);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setFocusable(true);

        //labels
        JLabel labelInput = new JLabel("Input Text");
        labelInput.setLocation(150,20);
        labelInput.setSize(100,20);

        JLabel labelOutput = new JLabel("Output Text");
        labelOutput.setLocation(475,20);
        labelOutput.setSize(100,20);


        //button
        JButton but = new JButton("Count");
        but.setLocation(300,20);
        but.setSize(100,20);
        but.addActionListener(this);
        but.setBackground(new Color(185,185,185));
        //400 / 50


        //scrollable textarea
        inputTextArea = new JTextArea();
        inputTextArea.setLineWrap(true);
        inputTextArea.setWrapStyleWord(true);

        JScrollPane scrollInput = new JScrollPane (inputTextArea,
                JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
        scrollInput.setLocation(10,60);
        scrollInput.setSize(330,425);


        //liste
        String[] dummy = new String[1];
        dummy[0] = "Plese insert Text!";
        frequencyList = new JList(dummy);

        JScrollPane scrollOutput = new JScrollPane (frequencyList,
                JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_NEVER);
        scrollOutput.setLocation(360,60);
        scrollOutput.setSize(330,425);


        //panel
        JPanel panel = new JPanel();
        panel.setLayout(null);
        panel.setFocusable(true);

        panel.add(labelInput);
        panel.add(labelOutput);
        panel.add(but);
        panel.add(scrollInput);
        panel.add(scrollOutput);

        add(panel);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        frequency = Main.count(inputTextArea.getText());

        frequencyList.setListData(frequency);
        repaint();
    }
}
