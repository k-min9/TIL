package study.datajpa.entity;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.CreatedDate;
import org.springframework.data.domain.Persistable;
import org.springframework.data.jpa.domain.support.AuditingEntityListener;

import javax.persistence.Entity;
import javax.persistence.EntityListeners;
import javax.persistence.Id;
import java.time.LocalDateTime;

/** 스프링데이터 세이브 관련 이슈 merge&persist*/
@Entity
@EntityListeners(AuditingEntityListener.class)
@NoArgsConstructor(access = AccessLevel.PROTECTED)
// id가 String 형태 >> @GeneratedValue 못씀 >> 스프링데이터가 Persistable 인터페이스 제공
public class Item implements Persistable<String> {

    // @GeneratedValue를 못쓰는 상황에서는
    // 스프링데이터는 새로운 객체를 인식하지 못하고, save시 persist가 아닌 merge를 계속 호출함
    // 인식에 판단되는 isNew를 override하고,
    @Id
    private String id;

    @CreatedDate  // 이걸 이용해서 inNew를 판별하고, @GeneratedValue 대체
    private LocalDateTime createdDate;

    public Item(String id) {
        this.id = id;
    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public boolean isNew() {
        return createdDate == null;
    }


}
