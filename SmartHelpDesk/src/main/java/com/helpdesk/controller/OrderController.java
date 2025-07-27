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
    public List<Order> getAllOrders() {
        return orderService.getAllOrders();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Order> getOrder(@PathVariable String id) {
        Order order = orderService.getOrderById(id);
        return (order != null) ? ResponseEntity.ok(order) : ResponseEntity.notFound().build();
    }

    @PostMapping
    public Order createOrder(@RequestBody Order order, @RequestHeader("Authorization") String jwt) {
        return orderService.createOrder(order);
    }

    @PostMapping("/{id}/refund")
    public ResponseEntity<Order> refundOrder(@PathVariable String id) {
        Order refundedOrder = orderService.issueRefund(id);
        return (refundedOrder != null) ? ResponseEntity.ok(refundedOrder) : ResponseEntity.notFound().build();
    }
    
    @PostMapping("/{id}/cancel")
    public ResponseEntity<Order> cancelOrder(@PathVariable String id) {
        Order cancelledOrder = orderService.cancelOrder(id);
        return (cancelledOrder != null) ? ResponseEntity.ok(cancelledOrder) : ResponseEntity.notFound().build();
    }
}
