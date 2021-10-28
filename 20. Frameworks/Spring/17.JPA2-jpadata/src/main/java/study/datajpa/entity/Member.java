package study.datajpa.entity;

import lombok.*;

import javax.persistence.*;

@Entity
@Getter @Setter// setter은 진짜 써도 안써도 상관없는 상황이 아니면 안쓰는게 기본 (changeUsername 참조)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@ToString(of = {"id", "username", "age"})  // 객체 출력 명령시 나오는 것
public class Member {

    @Id @GeneratedValue
    @Column(name = "member_id")
    private Long id;
    private String username;
    private int age;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "team_id")
    private Team team;

    // Entity는 기본 생성자 하나 있어야 하고, 무분별한 객체 생성도 막을 수 있음.
    // private은 proxy 생성을 막기때문에 protected 사용
    /** 이걸 줄이면 noargsconstructor*/
//    protected Member () {
//    }

    public Member(String username) {
        this.username = username;
    }

    public Member(String username, int age, Team team) {
        this.username = username;
        this.age = age;
        if (team!= null){
            changeTeam(team);
        }
    }

    public Member(String username, int age) {
        this.username = username;
        this.age = age;
    }

// 이렇게 함수 만들고 setter 비활성화 하는것 추천
//    public void changeUsername(String username){
//        this.username = username;
//    }

    public void changeTeam(Team team){
        this.team = team;
        team.getMembers().add(this);  // 반대쪽도 잊지 않고
    }


}
