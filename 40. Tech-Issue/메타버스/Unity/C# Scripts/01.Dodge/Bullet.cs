using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet : MonoBehaviour
{
    public float speed = 8f;
    private Rigidbody bulletRigidbody;

    void Start()
    {
        // 게임 오브젝트에서 Rigidbody 컴포넌트를 찾아 bulletRigidbody에 할당
        bulletRigidbody = GetComponent<Rigidbody>();
        // 리지드바디의 속도 = 앞 쪽 방향(Vector3 타입) * 이동 속력
        // transform 사용시, 자신의 게임 오브젝트의 트랜스폼 컴포넌트로 바로 접근
        bulletRigidbody.velocity = transform.forward * speed;        

        // 생성 후, 3초뒤에 자신의 오브젝트 파괴
        Destroy(gameObject, 3f);
    }

    // isTrigger 활성화로, 트리거 충돌시 자동으로 실행하게 만듬
    void OnTriggerEnter(Collider other) {
        // 충돌한 상대방 게임 오브젝트가 Player 태그 보유
        if (other.tag == "Player")
        {
            // 상대방 게임 오브젝트에서 PlayerController 컴포넌트 가져오기
            PlayerController playerController = other.GetComponent<PlayerController>();

            // 상대방으로부터 PlayerController 컴포넌트를 가져오는데 성공했다면
            if (playerController != null)
            {
                // 상대방 PlayerController 컴포넌트의 Die() 메서드 실행
                playerController.Die();
            }
        }
    }



}
