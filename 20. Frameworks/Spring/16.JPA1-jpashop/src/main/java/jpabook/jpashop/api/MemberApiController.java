package jpabook.jpashop.api;

import jpabook.jpashop.domain.Member;
import jpabook.jpashop.service.MemberService;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.RequiredArgsConstructor;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;
import java.util.stream.Collectors;

@RestController
@RequiredArgsConstructor
public class MemberApiController {

    private final MemberService memberService;

    /**회원 등록 API*/
    @PostMapping("/api/v1/members")
    public CreateMemberResponse saveMemberV1(@RequestBody @Validated Member member){
        //RequestBody로 json 내용을 Member에 넣어준다.
        Long id = memberService.join(member);
        return new CreateMemberResponse(id);
    }
    //문제점
    // 엔티티의 모든 값이 응답값으로 노출 됨 (절대 금지!)
    // 검증을 엔티티에서 하게 되면 나중에 로직에 따른 분리도 힘들고 코드가 지저분해짐
    // 엔티티 수정시 API 고장남


    //해결 : 별도의 DTO 생성으로 전부 해결 가능 (심심해보이지만, 엔티티 변경시 발생하는 사이드 이펙트 및 장애 방지를 위해 필수)
    @PostMapping("/api/v2/members")
    public CreateMemberResponse saveMemberV1(@RequestBody @Validated CreateMemberRequest request) {

        Member member = new Member();
        member.setName(request.getName());

        Long id = memberService.join(member);
        return new CreateMemberResponse(id);
    }

    /**회원 수정 API*/
    //PUT이 POST보다 좋은 점. 같은 걸 여러번 호출해도 결과가 같음
    @PutMapping("/api/v2/members/{id}")
    public UpdateMemberResponse updateMemberV2(@PathVariable("id") Long id,
                                               @RequestBody @Valid UpdateMemberRequest request) {

        memberService.update(id, request.getName());
        Member findMember = memberService.findOne(id);
        return new UpdateMemberResponse(findMember.getId(), findMember.getName());
    }

    /**회원 조회 API*/

    //조회 V1: 안 좋은 버전, 모든 엔티티가 노출, @JsonIgnore -> 이건 정말 최악, api가 이거 하나인가! 화면에 종속적이지 마라!
    @GetMapping("/api/v1/members")
    public List<Member> membersV1() {
        return memberService.findMembers();
    }
    //문제점
    //기본적으로 엔티티의 모든 값(극단적으로 패스워드)이 노출된다.
    //응답 스펙에 맞추기 위해 로직이 끌려다님(@JsonIgnore, 별도의 뷰 로직 등등)
    //엔티티가 변경시의 API 스펙 등사이드 이펙트에도 노출된다.

    //해결 : 엔티티가 아닌 별도의 DTO 반환으로 전부 해결 가능(등록과 비슷한 문제가 발생하고 해결되었다.)
    @GetMapping("/api/v2/members")
    public Result membersV2() {

        List<Member> findMembers = memberService.findMembers();
        //엔티티 리스트 -> DTO 리스트로 변환
        List<MemberDto> collect = findMembers.stream()
                .map(m -> new MemberDto(m.getName()))
                .collect(Collectors.toList());

        return new Result(collect);
    }



    /**기타 Inner Class 등등, DTO는 크게 로직있는것도 아니고 @Data 막씀*/
    @Data
    static class CreateMemberResponse {
        private Long id;

        public CreateMemberResponse(Long id) {
            this.id = id;
        }
    }

    @Data
    private class CreateMemberRequest {
        private String name;
    }

    @Data
    static class UpdateMemberRequest {
        private String name;
    }

    @Data
    @AllArgsConstructor
    static class UpdateMemberResponse {
        private Long id;
        private String name;
    }

    //한번 감싸서 반환해서 유연성이 올라감
    @Data
    @AllArgsConstructor
    static class Result<T> {
        //private int count; 같이 유연하게 늘리고 뺄 수 있음
        private T data;
    }

    //필요한 노출만 골라서 노출 가능
    @Data
    @AllArgsConstructor
    static class MemberDto {
        private String name;
    }
}
