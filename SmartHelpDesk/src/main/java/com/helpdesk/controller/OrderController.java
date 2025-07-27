package com.helpdesk.controller;

import com.helpdesk.model.Order;
import com.helpdesk.service.OrderService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/orders")
public class OrderController {

    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    @GetMapping
    public List<Order> getUserOrders(@RequestHeader("Authorization") String jwt) {
        return orderService.getUserOrders(jwt);
    }

    @GetMapping("/{id}")
    public ResponseEntity<Order> getOrderById(@PathVariable String id, @RequestHeader("Authorization") String jwt) {
        Order order = orderService.getOrderById(id, jwt);
        return (order != null) ? ResponseEntity.ok(order) : ResponseEntity.notFound().build();
    }

    @PostMapping
    public Order createOrder(@RequestBody Order order, @RequestHeader("Authorization") String jwt) {
        return orderService.createOrder(order, jwt);
    }

    @PostMapping("/{id}/refund")
    public ResponseEntity<Order> refundOrder(@PathVariable String id, @RequestHeader("Authorization") String jwt) {
        Order refundedOrder = orderService.issueRefund(id, jwt);
        return (refundedOrder != null) ? ResponseEntity.ok(refundedOrder) : ResponseEntity.notFound().build();
    }
    
    @PostMapping("/{id}/cancel")
    public ResponseEntity<Order> cancelOrder(@RequestHeader("Authorization") String jwt, @PathVariable String id) {
        Order cancelledOrder = orderService.cancelOrder(id, jwt);
        return (cancelledOrder != null) ? ResponseEntity.ok(cancelledOrder) : ResponseEntity.notFound().build();
    }
}
