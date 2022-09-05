package advanced.hello.trace.template;

import advanced.hello.trace.TraceStatus;
import advanced.hello.trace.logtrace.LogTrace;

/**
 * 템플릿 메서드 패턴에서 부모 클래스
 * 변하지 않는 코드를 담고, 변하는 코드는 자식 클래스를 만들어 분리
 * V3은 핵심 기능과 부가 기능을 섞었고,
 * V4는 핵심 기능과 템플릿을 호출하는 코드를 섞음
 */
public abstract class AbstractTemplate<T> {

    private final LogTrace trace;

    public AbstractTemplate(LogTrace trace) {
        this.trace = trace;
    }

    public T execute(String message) {

        TraceStatus status = null;
        try {
            status = trace.begin(message);
            //로직 호출
            T result = call();

            trace.end(status);
            return result;
        } catch (Exception e) {
            trace.exception(status, e);
            throw e;
        }
    }

    protected abstract T call();
}
