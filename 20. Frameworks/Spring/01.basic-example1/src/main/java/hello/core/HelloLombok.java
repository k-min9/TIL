package hello.core;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@NoArgsConstructor
@ToString
public class HelloLombok {

    private String name;
    private int age;
}
//여러분들은 이미 getter setter 생성자 tostring을 구현하셨습니다!
