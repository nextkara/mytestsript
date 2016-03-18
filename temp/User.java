package com.Joke.entity;
/*用户名、密码、邮箱、生日*/
public class User implements java.io.Serializable{

	private static final long serialVersionUID = 1L;  //版本序列化，可以不用理会
	private String ID;  //登陆ID
	private String name; //姓名
	private String passwd;//密码
	
	
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
