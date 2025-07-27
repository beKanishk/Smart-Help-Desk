package com.helpdesk.controller;

import com.helpdesk.model.User;
import com.helpdesk.service.UserService;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("api/users")
public class UserController {

	private final UserService userService;

	public UserController(UserService userService) {
		this.userService = userService;
	}

	@PostMapping("/register")
	public ResponseEntity<?> register(@RequestBody Map<String, String> request) {
		try {
			userService.register(
					request.get("email"),
					request.get("password"),
					request.getOrDefault("role", "USER"),
					request.get("name")
					);
			return ResponseEntity.ok("Registration Successful");
		} catch (Exception e) {
			return ResponseEntity.badRequest().body("Registration failed: " + e.getMessage());
		}
	}


	@PostMapping("/login")
	public Map<String, String> login(@RequestBody Map<String, String> request) {
		String token = userService.login(request.get("email"), request.get("password"));
		return Map.of("token", token);
	}

	@GetMapping("/{email}")
	public Optional<User> getUserByEmail(@PathVariable String email) {
		return userService.getUserByEmail(email);
	}

	@GetMapping
	public List<User> getAllUsers() {
		return userService.getAllUsers();
	}

}
