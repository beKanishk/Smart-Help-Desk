package com.helpdesk.repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.helpdesk.model.Order;

public interface OrderRepository extends MongoRepository<Order, String>{

}
