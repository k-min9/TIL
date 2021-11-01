package study.datajpa.dto;

import lombok.Data;
import study.datajpa.entity.Member;

@Data
public class MemberDto {

    private Long id;
    private String username;
    private String teamName;

    public MemberDto(Long id, String username, String teamName) {
        this.id = id;
        this.username = username;
        this.teamName = teamName;
    }

    // 새로운 DTO 제작법 (Page<MemberDto> pageDto = page.map(MemberDto::new);) 등의 문구도 쓸 수 있게 됨
    public MemberDto(Member member) {
        this.id = member.getId();
        this.username = member.getUsername();
    }
}
