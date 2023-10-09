using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Dongle : MonoBehaviour
{
    public int level;   
    public bool isDrag;

    Rigidbody2D rigid;
    Animator anim;

    void Awake() {
        rigid = GetComponent<Rigidbody2D>();
        anim = GetComponent<Animator>();
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
}
