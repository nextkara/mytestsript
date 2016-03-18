package com.Joke.util;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.TreeMap;

import org.jdom.Attribute;
import org.jdom.Document;
import org.jdom.Element;
import org.jdom.JDOMException;
import org.jdom.input.SAXBuilder;
import org.jdom.output.XMLOutputter;

public class JDOM {
	static Scanner sc = new Scanner(System.in);

	public static String write(String n, String p, String id) {
		// TODO Auto-generated method stub
		String path = ".\\UserInfo.xml";
		File file = new File(path);
		SAXBuilder saxBuilder = new SAXBuilder();
		Document doc;
		try {
			doc = saxBuilder.build(file);
			Element root = doc.getRootElement();
			Element user = new Element("User");
			Element name = new Element("name");
			Element passwd = new Element("passwd");
			if (checkID(id, root)) {
				user.setAttribute(new Attribute("id", id));
				name.setText(n);
				passwd.setText(p);
				user.addContent(name);
				user.addContent(passwd);
				root.addContent(user);
				XMLOutputter out = new XMLOutputter();
				out.output(doc, new FileOutputStream(file));
				return "Successful registration";
			} else
				return "ID already exists, please input again";

		} catch (JDOMException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "ERROR";

	}

	public static boolean checkID(String id, Element root) {
		// ºÏ≤‚ID «∑Ò¥Ê‘⁄
		boolean flag = true;
		@SuppressWarnings("unchecked")
		List<Element> list = root.getChildren("User");
		Iterator<Element> it = list.iterator();
		while (it.hasNext()) {
			Element e = (Element) it.next();
			if (e.getAttributeValue("id").equals(id)) {
				flag = false;
			}
		}
		return flag;

	}

	public static String read(String id, String passwd) {
		String path = ".\\UserInfo.xml";
		File file = new File(path);
		SAXBuilder saxBuilder = new SAXBuilder();

		try {
			Document doc = saxBuilder.build(file);
			Element root = doc.getRootElement();
			String info = getPasswd(root).get(id);
			if (info == null) {
				return "User does not exist!!";
			}
			String[] buf = info.split("/");

			if (buf[0].equals(passwd)) {
				return "Successful landing/" + buf[1];
			}

		} catch (JDOMException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return "Wrong password!!";
	}

	@SuppressWarnings("unchecked")
	private static Map<String, String> getPasswd(Element root) {
		Map<String, String> map = new TreeMap<String, String>();
		List<Element> list = new ArrayList<Element>();
		list = root.getChildren("User");
		Iterator<Element> it = list.iterator();
		while (it.hasNext()) {
			Element e = it.next();
			String id = e.getAttributeValue("id");
			String passwd = e.getChildText("passwd");
			String name = e.getChildText("name");
			map.put(id, getInfo(passwd, name));
		}

		return map;

	}

	private static String getInfo(String passwd, String name) {

		return passwd + "/" + name;

	}
}
