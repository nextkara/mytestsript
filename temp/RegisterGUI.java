import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.border.EmptyBorder;

import com.Joke.util.Register;

public class RegisterGUI extends JFrame {

	private static final long serialVersionUID = 3250371445038102261L;
	private JPanel contentPane;
	private JTextField nametext;
	private JTextField IDtext;
	private JTextField passwdtext;

	/**
	 * Launch the application.
	 */
	public void registerGUI() {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					RegisterGUI frame = new RegisterGUI();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public RegisterGUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 650, 400);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel namelabel = new JLabel("Please input user name");
		namelabel.setBounds(102, 91, 151, 23);
		contentPane.add(namelabel);

		JLabel IDlabel = new JLabel("Please input user ID");
		IDlabel.setBounds(102, 160, 151, 23);
		contentPane.add(IDlabel);

		JLabel passwdlaber = new JLabel("Please input user password");
		passwdlaber.setBounds(102, 224, 163, 23);
		contentPane.add(passwdlaber);

		nametext = new JTextField();
		nametext.setBounds(271, 92, 92, 21);
		contentPane.add(nametext);
		nametext.setColumns(10);

		IDtext = new JTextField();
		IDtext.setBounds(271, 161, 92, 21);
		contentPane.add(IDtext);
		IDtext.setColumns(8);

		passwdtext = new JTextField();
		passwdtext.setBounds(271, 225, 92, 21);
		contentPane.add(passwdtext);
		passwdtext.setColumns(10);

		JButton register = new JButton("Sign Up");
		register.addMouseListener(new MouseAdapter() {
			@SuppressWarnings("static-access")
			@Override
			public void mouseClicked(MouseEvent e) {
				String name = nametext.getText();
				String ID = IDtext.getText();
				String passwd = passwdtext.getText();
				if (Register.checkID(ID) == null) {
					if (Register.checkPasswd(passwd) == null) {
						String srt = Register.register(name, passwd, ID);
						JOptionPane.showMessageDialog(contentPane, srt,
								"information", JOptionPane.PLAIN_MESSAGE);
						setVisible(false);
						 new IndexGUI().init();
					
					} else {
						JOptionPane.showMessageDialog(contentPane,
								Register.checkPasswd(passwd), "ERROR",
								JOptionPane.ERROR_MESSAGE);
					}
				} else {
					JOptionPane.showMessageDialog(contentPane,
							Register.checkID(ID), "ERROR",
							JOptionPane.ERROR_MESSAGE);
				}
			}
		});
		register.setBounds(321, 305, 93, 23);
		contentPane.add(register);

		JButton back = new JButton("BACK");
		back.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		back.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				IndexGUI.init();
				setVisible(false);
			}
		});
		back.setBounds(531, 305, 93, 23);
		contentPane.add(back);

		JLabel label = new JLabel("Welcome to use KnowYou");
		label.setFont(new Font("ºÚÌå", Font.BOLD | Font.ITALIC, 30));
		label.setBounds(143, 26, 374, 35);
		contentPane.add(label);

		JLabel lblNewLabel = new JLabel("(There are 1 to 8 numbers)");
		lblNewLabel.setBounds(373, 164, 163, 15);
		contentPane.add(lblNewLabel);

		JLabel lblNewLabel_1 = new JLabel("(There are 6 to 15 numbers)");
		lblNewLabel_1.setBounds(373, 228, 163, 15);
		contentPane.add(lblNewLabel_1);
	}
}
