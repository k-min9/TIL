package hello.login.web;

import hello.login.web.argumentresolver.LoginMemberArgumentResolver;
import hello.login.web.filter.LogFilter;
import hello.login.web.filter.LoginCheckFilter;
import hello.login.web.interceptor.LogInterceptor;
import hello.login.web.interceptor.LoginCheckInterCeptor;
import lombok.extern.java.Log;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.method.support.HandlerMethodArgumentResolver;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import javax.servlet.Filter;
import java.util.List;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    //번외. 직접 만든 ArgumentResolver
    @Override
    public void addArgumentResolvers(List<HandlerMethodArgumentResolver> resolvers) {
        resolvers.add(new LoginMemberArgumentResolver());
    }

    //인터셉터 오버라이드
    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new LogInterceptor())
                .order(1)
                .addPathPatterns("/**") //하위는 전부 다 라는 뜻, 서블릿과 패턴이 다르다.
                .excludePathPatterns("/css/**", "/*.ico", "/error"); //범위 빼기, 인터셉터 생성 당시에 체크하니 화이트리스트가 필요없다.

        registry.addInterceptor(new LoginCheckInterCeptor())
                .order(2)
                .addPathPatterns("/**") //하위는 전부 다 라는 뜻, 서블릿과 패턴이 다르다.
                .excludePathPatterns("/", "/members/add", "/login", "/logout", "/css/**", "/*.ico", "/error");

    }


    //만들어 둔 필터를 등록해놔야 작동함
    @Bean
    public FilterRegistrationBean logFilter() {
        FilterRegistrationBean<Filter> filterFilterRegistrationBean = new FilterRegistrationBean<>();
        filterFilterRegistrationBean.setFilter(new LogFilter());
        filterFilterRegistrationBean.setOrder(1);
        filterFilterRegistrationBean.addUrlPatterns("/*"); // 모든 URL에서 작동

        return filterFilterRegistrationBean;
    }

    @Bean
    public FilterRegistrationBean loginCheckFilter() {
        FilterRegistrationBean<Filter> filterFilterRegistrationBean = new FilterRegistrationBean<>();
        filterFilterRegistrationBean.setFilter(new LoginCheckFilter());
        filterFilterRegistrationBean.setOrder(2); // 1번 필터 후 2번 필터 시행
        filterFilterRegistrationBean.addUrlPatterns("/*"); // 모든 URL에서 작동

        return filterFilterRegistrationBean;
    }

}
