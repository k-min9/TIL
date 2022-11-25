using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Runtime.InteropServices;

public class PlayerController : MonoBehaviour
{
    private Rigidbody playerRigidBody;  // 이동에 사용할 리지드바디 컴포넌트
    public float speed = 8f;  // 이동 속력

    // 함수 내보내기
    [DllImport("__Internal")]
    private static extern void GetSpeed(float speed);

    void Start()
    {
        // 게임 오브젝트에서 Rigidbody 컴포넌트를 찾아 playerRigidBody에 할당
        playerRigidBody = GetComponent<Rigidbody>();
        // 시작할때 react 쪽에 기본적인 정보를 보내보자
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetSpeed(speed);
    #endif
    }

    void Update()
    {
        // GetKey : 누르는 동안 true를 반환
        // 비교 - GetKeyUp, GetKeyDown : 해당 키를 떼는, 누르는 순간 반환
        // if (Input.GetKey(KeyCode.UpArrow) == true)
        // {
        //     playerRigidBody.AddForce(0f, 0f, speed);
        // }
        // if (Input.GetKey(KeyCode.DownArrow) == true)
        // {
        //     playerRigidBody.AddForce(0f, 0f, -speed);
        // }
        // if (Input.GetKey(KeyCode.RightArrow) == true)
        // {
        //     playerRigidBody.AddForce(speed, 0f, 0f);
        // }
        // if (Input.GetKey(KeyCode.LeftArrow) == true)
        // {
        //     playerRigidBody.AddForce(-speed, 0f, 0f);
        // }
        // 기존 코드의 문제점 : 조작이 즉시 반영되지 않고, if문을 많이 써서 코드가 더러움

        // 수평축과 수직축의 입력값을 감지하여 저장
        // GetAxis : 어떤 축에 대한 입력값을 숫자(-1,0,1)로 반환
        // 방향키 외에도 AWSD에도 대응
        float xInput = Input.GetAxis("Horizontal");
        float zInput = Input.GetAxis("Vertical");
        
        // 실제 이동속도 = 입려값 * 이동 속력
        float xSpeed = xInput * speed;
        float zSpeed = zInput * speed;

        // Vector3 속도를 (xSpeed, 0, zSpeed)로 생성
        Vector3 newVelocity = new Vector3(xSpeed, 0f, zSpeed);

        // 리지드바디의 속도에 newVelocity 할당 (관성없이 바로 속도 부여)
        playerRigidBody.velocity = newVelocity;
    }

    // 외부(Unity 내부)에 의해 실행될 것이기 때문에 public 필수
    public void Die()
    {
        // gameObject : 컴포넌트 입장에서 자신이 추가된 게임 오브젝트
        // setActive : 인스펙터 창의 오브젝트 활성화 버튼 제어, 비활성화시 동작을 안할 뿐 아니라, 씬 자체에서 안보이게 됨
        gameObject.SetActive(false);

        // 게임 매니저의 EndGame() 메서드 실행
        GameManager gameManager = FindObjectOfType<GameManager>();
        gameManager.EndGame();
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
