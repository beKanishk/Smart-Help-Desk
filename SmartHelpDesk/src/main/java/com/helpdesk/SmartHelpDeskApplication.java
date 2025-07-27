package com.helpdesk;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.helpdesk.model.Order;
import com.helpdesk.repository.OrderRepository;

@SpringBootApplication
public class SmartHelpDeskApplication {

	public static void main(String[] args) {
		SpringApplication.run(SmartHelpDeskApplication.class, args);
	}
	
	@Bean
	CommandLineRunner initData(OrderRepository repository) {
	    return args -> {
	        if (repository.count() == 0) { // Only insert if no orders exist
	            repository.save(new Order("Shipped", 99.99, "6885cfe085624c2312aaee4e"));
	            repository.save(new Order("Delivered", 149.99, "6885cfe085624c2312aaee4e"));
	        }
	    };
	}

}
