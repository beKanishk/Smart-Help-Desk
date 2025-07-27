package com.helpdesk.dto;

public class Response {
	private String id;
    private String email;
    private String name;
    private String role;
    
	public Response(String id, String email, String name, String role) {
		super();
		this.id = id;
		this.email = email;
		this.name = name;
		this.role = role;
	}
	public String getId() {
		return id;
	}
	public void setId(String id) {
		this.id = id;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getRole() {
		return role;
	}
	public void setRole(String role) {
		this.role = role;
	}
    
    
}
