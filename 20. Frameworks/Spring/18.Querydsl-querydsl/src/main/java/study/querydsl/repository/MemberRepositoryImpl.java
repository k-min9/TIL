package study.querydsl.repository;

import com.querydsl.core.QueryResults;
import com.querydsl.core.types.dsl.BooleanExpression;
import com.querydsl.jpa.impl.JPAQueryFactory;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageImpl;
import org.springframework.data.domain.Pageable;
import study.querydsl.dto.MemberSearchCondition;
import study.querydsl.dto.MemberTeamDto;
import study.querydsl.dto.QMemberTeamDto;

import javax.persistence.EntityManager;
import java.util.List;

import static org.springframework.util.StringUtils.hasText;
import static study.querydsl.entity.QMember.member;
import static study.querydsl.entity.QTeam.team;

// 최신버전(2.x 이후)은 Interface 이름 + Impl로 구현하는 방식 추가됨
public class MemberRepositoryImpl implements MemberRepositoryCustom{

    private final JPAQueryFactory queryFactory;

    public MemberRepositoryImpl(EntityManager em) {
        this.queryFactory = new JPAQueryFactory(em);
    }

    // MemberJPARepository 함수와 내용 동일 함
    @Override
    public List<MemberTeamDto> search(MemberSearchCondition condition) {
        return queryFactory
                .select(new QMemberTeamDto(
                        member.id,  // 생성자 쓰고 있기 때문에 필드 이름 자동으로 맞춰짐 (=member.id.as("memberId"))
                        member.username,
                        member.age,
                        team.id,
                        team.name
                ))
                .from(member)
                .leftJoin(member.team, team)
                .where(usernameEq(condition.getUsername()),
                        teamNameEq(condition.getTeamName()),
                        ageGoe(condition.getAgeGoe()),
                        ageLoe(condition.getAgeLoe()))
                .fetch();
    }

    private BooleanExpression usernameEq(String username) {
        return hasText(username) ? member.username.eq(username) : null;
    }
    private BooleanExpression teamNameEq(String teamName) {
        return hasText(teamName) ? team.name.eq(teamName) : null;
    }
    private BooleanExpression ageGoe(Integer ageGoe) {
        return ageGoe == null ? null : member.age.goe(ageGoe);
    }
    private BooleanExpression ageLoe(Integer ageLoe) { return ageLoe == null ? null : member.age.loe(ageLoe); }


    /** 스프링 데이터 페이징 활용 */

    @Override
    public Page<MemberTeamDto> searchPageSimple(MemberSearchCondition condition, Pageable pageable) {
        QueryResults<MemberTeamDto> results = queryFactory
                .select(new QMemberTeamDto(
                        member.id,  // 생성자 쓰고 있기 때문에 필드 이름 자동으로 맞춰짐 (=member.id.as("memberId"))
                        member.username,
                        member.age,
                        team.id,
                        team.name
                ))
                .from(member)
                .leftJoin(member.team, team)
                .where(usernameEq(condition.getUsername()),
                        teamNameEq(condition.getTeamName()),
                        ageGoe(condition.getAgeGoe()),
                        ageLoe(condition.getAgeLoe()))
                .offset(pageable.getOffset())  // 여기서부터 시작할거야
                .limit(pageable.getPageSize())  // 이 사이즈만큼 표기할거야
                .fetchResults();// fetch 아니다!, fetchResults는 컨텐츠용 쿼리 + 카운트용 쿼리 두 개 날림

        List<MemberTeamDto> content = results.getResults();  // 실제 데이터로 변경
        long total = results.getTotal();  // 카운트 쿼리 결과물

        return new PageImpl<>(content, pageable, total);
    }

    // 내가 직접 토탈 카운트 쿼리를 날림
    @Override
    public Page<MemberTeamDto> searchPageComplex(MemberSearchCondition condition, Pageable pageable) {
        // 내용만 받으니 QueryResult가 아닌 List 반환
        List<MemberTeamDto> content = queryFactory
                .select(new QMemberTeamDto(
                        member.id,  // 생성자 쓰고 있기 때문에 필드 이름 자동으로 맞춰짐 (=member.id.as("memberId"))
                        member.username,
                        member.age,
                        team.id,
                        team.name
                ))
                .from(member)
                .leftJoin(member.team, team)
                .where(usernameEq(condition.getUsername()),
                        teamNameEq(condition.getTeamName()),
                        ageGoe(condition.getAgeGoe()),
                        ageLoe(condition.getAgeLoe()))
                .offset(pageable.getOffset())  // 여기서부터 시작할거야
                .limit(pageable.getPageSize())  // 이 사이즈만큼 표기할거야
                .fetch();// simple과 다르게 fetch로 가져오고 카운트 쿼리를 분리

        // 카운트 쿼리
        long total = queryFactory
                .select(member)
                .from(member)
                .leftJoin(member.team, team)
                .where(usernameEq(condition.getUsername()),
                        teamNameEq(condition.getTeamName()),
                        ageGoe(condition.getAgeGoe()),
                        ageLoe(condition.getAgeLoe())
                )
                .fetchCount();

        return new PageImpl<>(content, pageable, total);
        //return PageableExecutionUtils.getpage(content, pageable, () -> countQuery.fetchCount()); 시 여기서 추가로 최적화 가능
    }
}
