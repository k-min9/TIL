using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;  // UI 관련 라이브러리
using UnityEngine.SceneManagement;  // 씬 관리 관련 라이브러리
using Photon.Realtime;

public class GameManager : MonoBehaviour
{
    // 게임 상태 제어
    public static bool isPlaying = false;  // 현재 방 안에 들어가 있는지
    public static bool isCameraMove = false;  // 현재 카메라 제어 중인지
    public static bool isChatting = false;  // 현재 채팅중인지
    public static string NickName = "Noname";
    public static string roomType = "GalleryS";  // 기본 로딩 씬 타입

    // 로비 정보 모음 (커뮤니티 하나)
    public static int roomCount = 0;
    public static int roomMax = 18;

    void Update()
    {
        // 특정 상황에서는 진행 안함
        if (isChatting) return;

        // R 버튼으로 씬의 재로딩
        // if (Input.GetKeyDown(KeyCode.R)) {
        //     // 나중 실전 사용시 씬 이름을 빌드 목록에서 빼먹지 않고 등록하자!
        //     SceneManager.LoadScene("Start");
        // }

        // C 버튼으로 카메라 제어 결정
        if (Input.GetKeyDown(KeyCode.C)) {
            isCameraMove = !isCameraMove;
        }
    }

    // 외부(react)에 의해 실행될 것이기 때문에 public 필수
    // public void SetNickname(string name) {
    //     NickName = name;
    // }
}
