package hellojpa;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Date;

@Entity
public class Member {

    @Id
    private Long id;

    //DB에서는 name 객체 필드명은 username
    @Column(name = "name")
    private String username;

    //어떤 타입도 변환 해주고 생각한대로 돌아감
    private Integer age;

    //DB에는 enum 개념이 없지만, 여기서 쓰면 알아서 변환되어 들어간다.
    @Enumerated(EnumType.STRING)
    private RoleType roleType;

    //DATE, TIME, TIMESTAMP 세 종류로 구분 됨
    @Temporal(TemporalType.TIMESTAMP)
    private Date createdDate;

    @Temporal(TemporalType.TIMESTAMP)
    private Date lastModifiedDate;

    //이 두 타입은 Temporal 없어도 자동으로 매핑해준다.
    private LocalDate test1;
    private LocalDateTime test2;


    //VARCHAR을 넘는 큰 컨텐츠를 넣고 싶을때
    @Lob
    private String description;

    //이건 DB에 매핑하지마라(컬럼 생성 안됨)
    @Transient
    public int temp;

    public Member() {
    }


}
