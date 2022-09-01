package advanced.hello.trace;

import java.util.UUID;

/**
 * 로그 추적기의 트랜잭션 ID와 깊이
 */
public class TraceId {

    private String id;  // 트랜잭션 ID
    private int level;  // 로그 깊이

    public TraceId() {
        this.id = createId();
        this.level = 0;
    }

    private TraceId(String id, int level) {
        this.id = id;
        this.level = level;
    }

    // UUID 중복 좀 있어도 되니까 거의 안겹치게 8글자만
    private String createId() {
        return UUID.randomUUID().toString().substring(0, 8);
    }

    // 로그 깊이 조절
    public TraceId createNextId() {
        return new TraceId(id, level + 1);
    }

    public TraceId createPreviousId() {
        return new TraceId(id, level - 1);
    }

    public boolean isFirstLevel() {
        return level == 0;
    }

    public String getId() {
        return id;
    }

    public int getLevel() {
        return level;
    }
}
