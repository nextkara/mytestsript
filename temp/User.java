package com.Joke.entity;
/*�û��������롢���䡢����*/
public class User implements java.io.Serializable{

	private static final long serialVersionUID = 1L;  //�汾���л������Բ������
	private String ID;  //��½ID
	private String name; //����
	private String passwd;//����
	
	
	public String getName() {
		return name;
	}
	public void setID(String iD) {
		ID = iD;
	}
	public String getID() {
		return ID;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPasswd() {
		return passwd;
	}
	public void setPasswd(String passwd) {
		this.passwd = passwd;
	}
	
}
