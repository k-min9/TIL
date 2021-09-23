package hello.login.web.filter;

import lombok.extern.slf4j.Slf4j;

import javax.servlet.*;
import javax.servlet.http.HttpServletRequest;
import java.io.IOException;
import java.util.UUID;

@Slf4j
public class LogFilter implements Filter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        log.info("고객요청으로 필터 호출");

        //그냥 ServletRequest는 기능이 부족해서 다운 캐스팅
        HttpServletRequest httpRequest = (HttpServletRequest) request;
        String requestURI = httpRequest.getRequestURI();

        String uuid = UUID.randomUUID().toString();

        try{
            log.info("REQUEST [{}][{}]", uuid, requestURI);
            chain.doFilter(request, response); //다음 필터 호출 꼭 넣어줘야함, chain있으면 그거 호출되고 없으면 서블렛이 호출 됨
        } catch (Exception e){
            throw e;
        } finally {
            log.info("RESPONSE [{}][{}]", uuid, requestURI);
        }


    }

    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        log.info("필터 초기화");
    }

    @Override
    public void destroy() {
       log.info("필터 파괴");
    }
}
