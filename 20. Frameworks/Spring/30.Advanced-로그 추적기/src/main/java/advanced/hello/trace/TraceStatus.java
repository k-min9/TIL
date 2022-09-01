package advanced.hello.trace;

/**
 * 로그의 상태 정보
 */
public class TraceStatus {

    private TraceId traceId;  // 트랜잭션 ID와 level 보유
    private Long startTimeMs;  // 로그 시작시간 (전체 수행시간 연산용)
    private String message;  // 로그 시작시 메시지 (종료시에도 수행)

    public TraceStatus(TraceId traceId, Long startTimeMs, String message) {
        this.traceId = traceId;
        this.startTimeMs = startTimeMs;
        this.message = message;
    }

    public TraceId getTraceId() {
        return traceId;
    }

    public Long getStartTimeMs() {
        return startTimeMs;
    }

    public String getMessage() {
        return message;
    }
}
