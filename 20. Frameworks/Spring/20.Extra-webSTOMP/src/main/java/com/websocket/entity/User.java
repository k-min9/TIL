package com.websocket.entity;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;
import javax.validation.constraints.Email;
import javax.validation.constraints.Size;

@Entity
@Table(name = "user")
@Getter @Setter
@NoArgsConstructor
@AllArgsConstructor
public class User {

    @Id @GeneratedValue
    private Long id;

    @Size(max=150)
    private String username;

    @Size(max=150)
    private String nickname;

    @Size(max=128)
    private String password;

    @Email
    @Size(max=254)
    private String email = "";

    @Size(max = 100)
    @Column(name = "profile_image")
    private String profileImage = "";
}
