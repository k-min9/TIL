package com.example.disccoveryService;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer;

@SpringBootApplication
@EnableEurekaServer
public class DisccoveryServiceApplication {

	public static void main(String[] args) {
		SpringApplication.run(DisccoveryServiceApplication.class, args);
	}

}
