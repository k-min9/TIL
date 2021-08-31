package hello.springmvc.basic.requestmapping;

import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/mapping/users")
public class MappingClassController {

//    회원 관리를 HTTP API로 만든다 생각하고 매핑을 어떻게 하는지 알아보자.
//    회원 목록 조회: GET /users
//    회원 등록: POST /users
//    회원 조회: GET /users/{userId}
//    회원 수정: PATCH /users/{userId}
//    회원 삭제: DELETE /users/{userId}

    @GetMapping
    public String user(){
        return "get users";
    }

    @PostMapping
    public String addUser(){
        return "post users";
    }

    @GetMapping("/{userid}")
    public String findUser(@PathVariable String userId){
        return "get userId=" + userId;
    }

    @PatchMapping("/{userId}")
    public String updateUser(@PathVariable String userId){
        return "update userId=" + userId;
    }

    @DeleteMapping("/{userId}")
    public String deleteUser(@PathVariable String userId){
        return "delete userId=" + userId;
    }


}
