package study.querydsl.dto;

import com.querydsl.core.annotations.QueryProjection;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class MemberDto {

    private String username;
    private int age;

    @QueryProjection  // 구조적으로 Querydsl에 대한 의존성이 생김...
    public MemberDto(String username, int age) {
        this.username = username;
        this.age = age;
    }

    public MemberDto(String username) {
        this.username = username;
    }
}
