using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;  // UI 관련 라이브러리
using UnityEngine.SceneManagement;  // 씬 관리 관련 라이브러리

public class GameManager : MonoBehaviour
{
    public static bool isCameraMove = false;
    public static bool isChatting = false;

    void Update()
    {
        // R 버튼으로 씬의 재로딩
        if (Input.GetKeyDown(KeyCode.R)) {
            // 나중 실전 사용시 씬 이름을 빌드 목록에서 빼먹지 않고 등록하자!
            SceneManager.LoadScene("SampleScene");
        }

        // 3 버튼으로 카메라 제어 결정
        if (Input.GetKeyDown(KeyCode.Alpha3)) {
            isCameraMove = !isCameraMove;
        }
    }
}
