using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Runtime.InteropServices;

public class PlayerController : MonoBehaviour
{
    private Rigidbody playerRigidBody;  // 이동에 사용할 리지드바디 컴포넌트
    private Animator playerAnimator;  // 애니메이션 할당용 변수


    // 이동
    public float speed = 10f;  // 속력
    public float jumpPower = 13.5f;  // 점프력
    Vector3 newVelocity;  // 이동 벡터
    float xInput;  // 입력
    float zInput;  // 입력
    bool isWalkDown; // 입력
    bool isJumpDown; // 입력
    bool isJump;  // 점프 상태인지 확인
    bool isBorder;  // 경계선에 닿았나 체크

    // 함수 내보내기
    [DllImport("__Internal")]
    private static extern void GetSpeed(float speed);


    void Awake()
    {
        // 게임 오브젝트에서 Rigidbody 컴포넌트를 찾아 playerRigidBody에 할당
        playerRigidBody = GetComponent<Rigidbody>();
        // playerAnimator = GetComponent<Animator>();
        playerAnimator = GetComponentInChildren<Animator>();  // 컴포넌트 하위 자식에 부여했음
        // 시작할때 react 쪽에 기본적인 정보를 보내보자
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetSpeed(speed);
    #endif
    }

    void Update()
    {
        GetInput();
        Move();
        Turn();   
        Jump();
    }

    void FixedUpdate() {
        FreezeRotation();
        StopToWall();
    }

    void GetInput()
    {
        // 수평축과 수직축의 입력값을 감지하여 저장
        // GetAxis : 어떤 축에 대한 입력값을 숫자(-1 ~ 1)로 반환
        // 방향키 외에도 AWSD에도 대응
        xInput = Input.GetAxis("Horizontal");
        zInput = Input.GetAxis("Vertical");
        isWalkDown = Input.GetButton("Walk");  // Shift 누르고 있는지 여부
        isJumpDown = Input.GetButtonDown("Jump");  // Space 한번 누르면 즉시
    }

    void Move()
    {
        // Vector3 속도를 (xSpeed, 0, zSpeed)로 생성
        newVelocity = new Vector3(xInput, 0f, zInput).normalized;

        // 리지드바디의 속도에 newVelocity 할당 (관성없이 바로 속도 부여)  >> 점프 구현시 방해 됨
        // playerRigidBody.velocity = newVelocity;
        if (!isBorder)
            transform.position += newVelocity * speed * (isWalkDown? 0.3f : 1f) * Time.deltaTime;

        // 애니메이션 설정
        playerAnimator.SetBool("isRun", newVelocity != Vector3.zero);
        playerAnimator.SetBool("isWalk", isWalkDown);
    }

    void Jump()
    {
        if (isJumpDown && !isJump) {
            playerRigidBody.AddForce(Vector3.up * jumpPower, ForceMode.Impulse);
            playerAnimator.SetBool("isJump", true);  // 착지용
            playerAnimator.SetTrigger("doJump");  // 도약 버튼 누를때 한 번
            isJump = true;
        }
    }

    void OnCollisionEnter(Collision collision) {
        // 점프 후 바닥 충돌시 점프 상태 해제
        if(collision.gameObject.tag == "Floor") {
            playerAnimator.SetBool("isJump", false);  // 착지용
            isJump = false;
        }
    }

    void Turn() 
    {
        // 방향 전환
        if (newVelocity != Vector3.zero)
        {
            Quaternion newRotation = Quaternion.LookRotation(newVelocity);
            playerRigidBody.MoveRotation(newRotation);
        }
    }

    // rigidBody velocity로 인한 자동회전 방지
    void FreezeRotation() {
        playerRigidBody.angularVelocity = Vector3.zero;
    }

    // 벽 통과 방지용 코드
    void StopToWall() {
        // 보는 방향 확인용 코드
        // Debug.DrawRay(transform.position, transform.forward*5, Color.green);
        // Raycast : Ray를 쏘아 닿는 오브젝트, 레이어를 감지, true, false 로 바뀜 -> move의 제한사용으로 활용
        isBorder = Physics.Raycast(transform.position, transform.forward, 4, LayerMask.GetMask("Wall"));
    }

    // 외부(react)에 의해 실행될 것이기 때문에 public 필수
    // react에 의해 불릴 methodName
    public void SpeedUp()
    {
        speed = speed + 0.5f;
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetSpeed(speed);
    #endif
    }

    public void SpeedDown()
    {
        speed = speed - 0.5f;
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetSpeed(speed);
    #endif
    }

}
