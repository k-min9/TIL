package hello.jdbc.domain;

import lombok.Data;

/**
 * 회원 번호와 소지액만 나타내는 단순한 도메인
 */
@Data
public class Member {

    private String memberId;
    private int money;

    public Member() {
    }

    public Member(String memberId, int money) {
        this.memberId = memberId;
        this.money = money;
    }
}
