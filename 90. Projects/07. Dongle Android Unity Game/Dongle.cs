using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dongle : MonoBehaviour
{
    public GameManager gameManager;
    public ParticleSystem effectMerge;

    public int level;   
    public bool isDrag;
    public bool isMerge;  // 타 동글의 개입으로 인한 오류 방지용
    SpriteRenderer spriteRenderer;

    int[] scores = new int[]{1,3,6,10,15,21,28,36,45,55};

    public Rigidbody2D rigid;
    CircleCollider2D circle;
    Animator anim;

    float deadTime;

    void Awake() {
        rigid = GetComponent<Rigidbody2D>();
        circle = GetComponent<CircleCollider2D>();
        anim = GetComponent<Animator>();
        spriteRenderer = GetComponent<SpriteRenderer>();
    }

    void OnEnable() {
        anim.SetInteger("Level", level);
    }

    void Update()
    {
        if (isDrag) {
            Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);  // 스크린좌표를 월드로 변환
            float leftBorder = -4.7f + (0.6f + transform.localScale.x / 2f);  // 경계에 기본경계+반지름 만큼 감소
            float rightBorder = 4.7f - (0.6f + transform.localScale.x / 2f);

            if (mousePos.x < leftBorder) {
                mousePos.x = leftBorder;
            } else if (mousePos.x > rightBorder) {
                mousePos.x = rightBorder;
            }

            mousePos.y = 8;  // 상단에 위치 고정
            mousePos.z = 0;  // z축은 0으로 고정
            transform.position = Vector3.Lerp(transform.position, mousePos, 0.2f);  // 천천히 따라오게 하는 함수
        }
    }

    public void Drag() {
        isDrag = true;
    }

    public void Drop() {
        isDrag = false;
        rigid.simulated = true;  // 자연낙하 활성화
    }

    // 충돌중 계속 실행하는 함수
    void OnCollisionStay2D(Collision2D collision) {
        if (collision.gameObject.tag == "Dongle") {
            Dongle other = collision.gameObject.GetComponent<Dongle>();

            // 합치기 로직
            if (level == other.level && !isMerge && !other.isMerge && level < 7) {  // 레벨 동일 & 합치는 중 아님 & 최고레벨 이하
                // 나와 상대편 위치 가져오기
                float meX = transform.position.x;
                float meY = transform.position.y;
                float otherX = other.transform.position.x;
                float otherY = other.transform.position.y;

                // 내가 아래에 있을때 또는 동일한 높이일 때, 내가 오른쪽에 있을때
                if (meY < otherY || (meY == otherY && meX > otherX)) {
                    // 상대를 숨기고
                    other.Hide(transform.position);
                    // 레벨업
                    LevelUp();
                }
            }
        }

    }

    // 동글 합칠때 숨기기
    public void Hide(Vector3 targetPos) {
        isMerge = true;

        rigid.simulated = false;
        circle.enabled = false;

        // 게임오버시 이펙트 실행
        if(targetPos == Vector3.up * 100) {
            EffectPlay();
        }

        StartCoroutine(HideRoutine(targetPos));
    }

    // 내 위치로 이동하면서 숨기게 Coroutine 사용
    IEnumerator HideRoutine(Vector3 targetPos) {
        
        int frameCount = 0;

        while (frameCount < 20) {
            frameCount++;
            if (targetPos != Vector3.up * 100) {  // 일반 숨김
                transform.position = Vector3.Lerp(transform.position, targetPos, 0.5f);
            } else { // 게임오버 숨김
                transform.localScale = Vector3.Lerp(transform.localScale, Vector3.zero, 0.2f);  // 작아지며 사라지게
            }
            
            yield return null;
        }

        isMerge = false;
        gameObject.SetActive(false);
        
    }

    void LevelUp(){
        isMerge = true;

        // 레벨업 중 방해되는 물리속도 제거
        rigid.velocity = Vector2.zero;
        rigid.angularVelocity = 0;  // 회전속도

        gameManager.score += scores[level];

        StartCoroutine(LevelUpRoutine());
    }

    IEnumerator LevelUpRoutine() {
        yield return new WaitForSeconds(0.2f);

        anim.SetInteger("Level", level + 1);  // 애니메이션 재생
        EffectPlay();

        yield return new WaitForSeconds(0.3f);  // 애니메이션시간 0.2초 고려 (폭업방지용)
        level++;

        isMerge = false;
    }

    // 게임오버체크용
    void OnTriggerStay2D(Collider2D collision) {
        if(collision.tag == "Line") {

            deadTime += Time.deltaTime;

            if (deadTime > 5) {
                gameManager.GameOver();
            } else if (deadTime > 2) {
                spriteRenderer.color = new Color(0.9f, 0.2f, 0.2f);
            }
        }
    }

    // 게임오버 관련 변수 초기화
    void OnTriggerExit2D(Collider2D collision) {
        if(collision.tag == "Line") {
            deadTime = 0;
            spriteRenderer.color = Color.white;
        }
    }

    // 레벨업 이펙트 관리
    void EffectPlay() {
        effectMerge.transform.position = transform.position;
        effectMerge.transform.localScale = transform.localScale;
        effectMerge.Play();
    }
}
