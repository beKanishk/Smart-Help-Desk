package com.helpdesk.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "orders")
public class Order {

    @Id
    private String id;
    private String status;
    private double amount;
    private String userId;

    public Order(String status, double amount, String userId) {
        this.status = status;
        this.amount = amount;
        this.userId = userId;
    }

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getStatus() {
		return status;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public double getAmount() {
		return amount;
	}

	public void setAmount(double amount) {
		this.amount = amount;
	}

	public String getUser_Id() {
		return userId;
	}

	public void setUser_Id(String user_Id) {
		this.userId = user_Id;
	}

}
