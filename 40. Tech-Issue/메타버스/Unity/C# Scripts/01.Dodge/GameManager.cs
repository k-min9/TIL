using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;  // UI 관련 라이브러리
using UnityEngine.SceneManagement;  // 씬 관리 관련 라이브러리

public class GameManager : MonoBehaviour
{
    // // 특정 구역 접근시 활성화 할 게임 오브젝트를 만든다고 가정
    // public GameObject routeToDetail;
    public Text timeText;  // 생존 시간 표시용 UI 컨텍스트

    private float surviveTime;  // 생존 시간
    private bool isGameover;  // 게임오버 상태

    void Start()
    {
        // 초기화
        surviveTime = 0f;
        isGameover = false;
        
    }

    void Update()
    {
        // 시간에 따라 UI가 변경 표기
        if (!isGameover)
        {
            surviveTime += Time.deltaTime;
            timeText.text = "Time : " + (int) surviveTime;
        }

        // R 버튼으로 씬의 재로딩
        if (Input.GetKeyDown(KeyCode.R)) {
            // 나중 실전 사용시 씬을 빌드 목록에서 빼먹지 않고 등록하자!
            SceneManager.LoadScene("SampleScene");
        }
    }

    // 피탄으로 인한 게임 오버. 실행자가 Player일테니 public 설정
    public void EndGame() {
        isGameover = true;
    }


}
