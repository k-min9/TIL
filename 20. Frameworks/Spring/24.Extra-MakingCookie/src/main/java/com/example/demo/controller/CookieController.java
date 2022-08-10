package com.example.demo.controller;

import org.springframework.http.ResponseCookie;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletResponse;
import java.util.ArrayList;

@RestController
public class CookieController {

//    @CrossOrigin(origins = "http://localhost:3000", allowCredentials = "true")
    @PostMapping("/login_jwt/{id}")
    public ResponseEntity<?> login_jwt(HttpServletResponse response) {
//        ArrayList<String> data = new ArrayList<>();
//        data.add("minguID");
//        data.add("AAAA");
        ResponseCookie accessTokenCookie = ResponseCookie.from("accessToken", "AAAA")
                .path("/")
                .httpOnly(true)
                .secure(false)
                .sameSite("Lax")
                .build();
        ResponseCookie refreshTokenCookie = ResponseCookie.from("refreshToken", "BBBB")
                .path("/")
                .httpOnly(true)
                .secure(false)
                .sameSite("Lax")
                .build();
        response.setHeader("Set-Cookie", accessTokenCookie.toString());
        response.addHeader("Set-Cookie", refreshTokenCookie.toString());
//            redisService.setStringValue(loginResponse.getRefreshToken(), data, JwtTokenProvider.REFRESH_TOKEN_VALIDATION_SECOND);
        return ResponseEntity.ok(null);
    }
}
