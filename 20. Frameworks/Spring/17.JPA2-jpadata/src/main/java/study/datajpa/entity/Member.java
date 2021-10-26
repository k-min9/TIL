package study.datajpa.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

@Entity
@Getter @Setter// setter은 진짜 써도 안써도 상관없는 상황이 아니면 안쓰는게 기본 (changeUsername 참조)
public class Member {

    @Id @GeneratedValue
    private Long id;
    private String username;

    // Entity는 기본 생성자 하나 있어야 하고, 무분별한 객체 생성도 막을 수 있음.
    // private은 proxy 생성을 막기때문에 protected 사용
    protected Member () {
    }

    public Member(String username) {
        this.username = username;
    }

    // 이렇게 함수 만들고 setter 비활성화 하는것 추천
//    public void changeUsername(String username){
//        this.username = username;
//    }
}
