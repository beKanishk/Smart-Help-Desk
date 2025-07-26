package com.helpdesk.service;

import com.helpdesk.model.Order;
import com.helpdesk.repository.OrderRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class OrderService {

    private final OrderRepository orderRepository;

    public OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public Order getOrderById(String id) {
        return orderRepository.findById(id)
                .orElse(new Order("Not Found", 0));
    }

    public Order issueRefund(String id) {
        Optional<Order> orderOpt = orderRepository.findById(id);
        
        if (orderOpt.isPresent()) {
            Order order = orderOpt.get();
            if (!"Refunded".equals(order.getStatus())) {
                order.setStatus("Refunded");
                return orderRepository.save(order);
            }
            return new Order("Refund Already Issued", 0);
        }
        
        return new Order("Refund Failed", 0);
    }

    public Order saveOrder(Order order) {
        return orderRepository.save(order);
    }

	public List<Order> getAllOrders() {
		return orderRepository.findAll();
	}

	public Order createOrder(Order order) {
		return orderRepository.save(order);
	}
}
