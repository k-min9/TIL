package study.datajpa.entity;

import lombok.Getter;

import javax.persistence.Column;
import javax.persistence.MappedSuperclass;
import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;
import java.time.LocalDateTime;

@Getter
@MappedSuperclass  // 진짜 상속이 아니고, 속성들을 내려서 정의하겠다는 뜻
public class JpaBaseEntity {

    @Column(updatable = false)  // 실수로라도 바꿔도 DB값이 변경되지 않음
    private LocalDateTime createdDate;
    private LocalDateTime updatedDate;

    // 이벤트 : persist전에 작동
    @PrePersist
    public void prePersist() {
        LocalDateTime now = LocalDateTime.now();
        createdDate = now;
        updatedDate = now;
    }

    // 이벤트 : update전에 작동
    @PreUpdate
    public void preUpdate() {
        updatedDate = LocalDateTime.now();
    }


}
