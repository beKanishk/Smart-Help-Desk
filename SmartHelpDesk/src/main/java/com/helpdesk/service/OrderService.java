package com.helpdesk.service;

import com.helpdesk.model.Order;
import com.helpdesk.model.User;
import com.helpdesk.repository.OrderRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class OrderService {

    private final OrderRepository orderRepository;
    @Autowired
    public UserService userService;

    public OrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public Order getOrderById(String id, String jwt) {
    	User user = userService.findUserByJwt(jwt);
    	
    	if(user != null)
    		return orderRepository.findById(id)
                .orElse(new Order("Not Found", 0, ""));
    	
    	throw new RuntimeException("Not able to get order - user not found");
    }

    public Order issueRefund(String id, String jwt) {
    	User user = userService.findUserByJwt(jwt);
    	
    	if(user != null) {
    		Optional<Order> orderOpt = orderRepository.findById(id);
	        
	        if (orderOpt.isPresent()) {
	            Order order = orderOpt.get();
	            if (!"Refunded".equals(order.getStatus())) {
	                order.setStatus("Refunded");
	                return orderRepository.save(order);
	            }
	            return new Order("Refund Already Issued", 0, "");
	        }
	        return new Order("Refund Failed", 0, "");
    	}
    	
    	throw new RuntimeException("Not able to issue refund - user not found");
    }

    public Order saveOrder(Order order) {
        return orderRepository.save(order);
    }

	public List<Order> getUserOrders(String jwt) {
		User user = userService.findUserByJwt(jwt);
		
		return orderRepository.findByUserId(user.getId());
	}

	public Order createOrder(Order order, String jwt) {
	    User user = userService.findUserByJwt(jwt);

	    if (user == null) {
	        throw new RuntimeException("Not able to create order - user not found");
	    }

	    order.setUser_Id(user.getId());
	    return orderRepository.save(order);
	}

	
	public Order cancelOrder(String id, String jwt) {
		User user = userService.findUserByJwt(jwt);
		
		if(user == null) throw new RuntimeException("Not able to cancel order - user not found");
		
		Optional<Order> opt = orderRepository.findById(id);
		
		if(opt.isPresent()) {
			Order order = opt.get();
			if(!"Cancelled".equals(order.getStatus())) {
				order.setStatus("Cancelled");
				return orderRepository.save(order);
			}
			return new Order("Order is already cancelled", 0, "");
		}
		
		return new Order("Order not found", 0, "");
	}
}
