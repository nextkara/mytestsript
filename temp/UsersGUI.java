import java.awt.Color;
import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

import javax.swing.JButton;
import javax.swing.JEditorPane;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JInternalFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTabbedPane;
import javax.swing.JTextField;
import javax.swing.JTextPane;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;

import com.Joke.util.Diary;

public class UsersGUI extends JFrame {

	private static final long serialVersionUID = -3130465509415076348L;
	private JPanel contentPane;
	private JTextField textField;
	private JFileChooser chooser;
	private static String pathname;

	public static void init(String path) {
		pathname = path;
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					UsersGUI frame = new UsersGUI();
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
	public UsersGUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 600, 400);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JTabbedPane tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane.setToolTipText("KonwYou");
		tabbedPane.setBounds(0, 0, 574, 67);
		contentPane.add(tabbedPane);

		final JPanel panel = new JPanel();
		tabbedPane.addTab("Management Journal", null, panel, null);

		chooser = new JFileChooser(".\\"+pathname);//��ʼ��JFileChooser��������Ĭ��Ŀ¼Ϊ�û�Ŀ¼
		FileNameExtensionFilter filter=new FileNameExtensionFilter("Allowed","ky");//�ļ�ѡ������ֻ����ѡ��.ky�ļ�
		chooser.setFileFilter(filter);//Ϊ�ļ�����ѡ����

		JButton readButton = new JButton("Read the diary");
		readButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int value = chooser.showOpenDialog(panel);
				JInternalFrame internalFrame_Read = new JInternalFrame("Read the diary",
						false, true, false, false);
				internalFrame_Read.setBounds(0, 77, 584, 275);
				contentPane.add(internalFrame_Read);
				internalFrame_Read.getContentPane().setLayout(null);
				JTextPane txtDiary = new JTextPane();
				txtDiary.setBounds(0, 0, 568, 246);
				internalFrame_Read.getContentPane().add(txtDiary);
				javax.swing.text.Document doc=txtDiary.getDocument();//JTextPaneû��append����������ʹ��Document�����ϲ����ı�
				txtDiary.setBackground(Color.GREEN);
				
				if (value == JFileChooser.APPROVE_OPTION) {
					File file = chooser.getSelectedFile();
					if(file.exists())
					{
						
					try {
						String txt=null;
						BufferedReader bufr = new BufferedReader(new FileReader(file));
						String line= System.getProperty("line.separator");//��ȡ���з�
						while((txt=bufr.readLine())!=null)
						{
							
							doc.insertString(doc.getLength(), txt+line, null);
							
						}
						
						txtDiary.setEditable(false);//����Ϊ���ɱ༭
					} catch (Exception e1) {
						// TODO Auto-generated catch block
						e1.printStackTrace();
					}
					
					internalFrame_Read.setVisible(true);
					}
				}
			}
		});
		panel.add(readButton);

		JButton addButton = new JButton("Create a diary");
		addButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				final JInternalFrame internalFrame_Write = new JInternalFrame("Create a diary",
						false, true, false, false);
				internalFrame_Write.setBounds(0, 77, 584, 275);
				contentPane.add(internalFrame_Write);
				internalFrame_Write.getContentPane().setLayout(null);

				textField = new JTextField();
				textField.setBounds(76, 0, 492, 21);
				internalFrame_Write.getContentPane().add(textField);
				textField.setColumns(10);

				JLabel label = new JLabel("Title");
				label.setFont(new Font("����", Font.PLAIN, 12));
				label.setBounds(46, 3, 52, 15);
				internalFrame_Write.getContentPane().add(label);

				final JEditorPane editorPane = new JEditorPane();
				editorPane.setBounds(0, 31, 568, 179);
				internalFrame_Write.getContentPane().add(editorPane);

				JButton save = new JButton("SAVE");
				save.setBounds(465, 213, 93, 23);
				save.addMouseListener(new MouseAdapter() {
					public void mouseClicked(MouseEvent e) {
						String title = textField.getText();
						String txt = editorPane.getText();
						Diary.addDiary(pathname, title, txt);
						internalFrame_Write.setVisible(false);
					}
				});
				internalFrame_Write.getContentPane().add(save);
				internalFrame_Write.setVisible(true);

			}
		});
		panel.add(addButton);

		JButton delButton = new JButton("Delete");
		delButton.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				File file=null;
				chooser.setMultiSelectionEnabled(true);//���ö�ѡ
				int value=chooser.showOpenDialog(panel);
				if(value==JFileChooser.APPROVE_OPTION)
				{
					file=chooser.getSelectedFile();
					int x=JOptionPane.showConfirmDialog(panel,"Confirm delete?","Please confirm",JOptionPane.OK_CANCEL_OPTION,JOptionPane.QUESTION_MESSAGE);
					if(file.exists())
					{
						if(x==JOptionPane.OK_OPTION)
						{
							file.delete();
						}
					
					}
					
				}
				
			}
		});
		panel.add(delButton);

		JButton back = new JButton("BACK");
		back.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				IndexGUI.init();
				setVisible(false);
			}
		});
		panel.add(back);
	}
}
