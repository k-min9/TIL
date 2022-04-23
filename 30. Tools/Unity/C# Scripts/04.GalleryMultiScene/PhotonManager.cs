using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;  // 포톤 기능 사용
using UnityEngine.UI;  // UI에 접속 시도 사항 등 표시
using Photon.Realtime;
using TMPro;
using UnityEngine.SceneManagement;
using System.Runtime.InteropServices;

public class PhotonManager : MonoBehaviourPunCallbacks
{
    // 버전
    private string version = "1";
    public Text connectionInfoText;  // 네트워크 정보 표시용 텍스트
    public PhotonView PV;
    public GameObject playerPrefab;

    [Header("GamePanel")]
    public GameObject GamePanel;
    public GameObject HowtoPanel;

    // 채팅 패널 통일 가능?
    [Header("ChattingPanel")]
    public GameObject ChattingPanel;
    public Text[] ChatText;
    public TMP_InputField ChatInput;
    public Scrollbar bar;

    // 내보낼 변수
    public string roomName;

    // 함수 내보내기
    [DllImport("__Internal")]
    private static extern void GetRoomName(string roomName);

    void Start()
    {
        connectionInfoText.text = "상태 : " + PhotonNetwork.CurrentRoom.Name;
        SpawnPlayer();

    // 방 생성 완료를 react 쪽에 보고
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        roomName = "입장완료";
        GetRoomName(roomName);
    #endif
    }

    void Update()
    {
        // ESC 버튼으로 설명 화면
        if (Input.GetKeyDown(KeyCode.Escape)) {
            if (HowtoPanel.activeSelf == true) {
                HowtoPanel.SetActive(false);
            } else {
                HowtoPanel.SetActive(true);
            }
        }

        // // 4 버튼으로 로비 판넬 보이기
        // if (Input.GetKeyDown(KeyCode.Alpha4)) {
        //     ShowPanelStart();
        // }
        // // 5 버튼으로 게임 판넬 보이기
        // if (Input.GetKeyDown(KeyCode.Alpha5)) {
        //     ShowPanelGame();
        // }
        // 엔터 버튼으로 채팅 판넬 보이기, 채팅 보내기
        if (Input.GetKeyDown(KeyCode.Return)) {
            // 방에 들어가 있는 상태
            if (GameManager.isPlaying) {
                if (GameManager.isChatting == true) {
                    if (ChatInput.text != "") {
                        ChatSend();
                    } else {
                        GameManager.isChatting = false;
                        ChattingPanel.SetActive(false);
                    }                
                } else {
                    ShowPanelChatting();
                }
            // 방에 들어가있지 않은 상태. 일단은 닉네임 설정용으로 둘까?
            } 
            // else {
            //     SetNickName();
            // }
        }        
    }

    public void ShowPanelChatting() {
        GameManager.isChatting = true;
        ChattingPanel.SetActive(true);
        // 판넬 활성화 후 포커스
        ChatInput.Select();
        ChatInput.ActivateInputField();
    }

    // 다른 플레이어가 들어가면 실행됨
    public override void OnPlayerEnteredRoom(Player newPlayer)
    {
        ChatRPC("<color=yellow>" + newPlayer.NickName + "님이 참가하셨습니다</color>");
    }

    // 다른 플레이어가 나가면 실행됨
    public override void OnPlayerLeftRoom(Player otherPlayer)
    {
        ChatRPC("<color=yellow>" + otherPlayer.NickName + "님이 퇴장하셨습니다</color>");
    }

    // 방에서 나오기
    public void LeaveRoom() {
        PhotonNetwork.LeaveRoom();
        // ShowPanelStart();
    }

    // 방을 나오면 자동으로 실행
    public override void OnLeftRoom() {
        // 룸을 나가면 시작 씬으로 돌아감
        SceneManager.LoadScene("Start");
    }

    // 플레이어 생성
    private void SpawnPlayer() {
        // 생성 랜덤 위치
        Vector3 randomSpawnPos = Random.insideUnitSphere * 3f;
        randomSpawnPos.y = 0f;
        // 생성
        PhotonNetwork.Instantiate(playerPrefab.name, randomSpawnPos, Quaternion.identity);
        // 카메라 세팅
        // Camera.main.GetComponent<PlayerCamera>().setPlayer(gameObject.transform);
    }


    // 채팅
    public void ChatSend()
    {
        if (ChatInput.text != "") {
            PV.RPC("ChatRPC", RpcTarget.All, PhotonNetwork.NickName + " : " + ChatInput.text);
            ChatInput.text = "";
            // 보내고도 포커스 활성화
            ChatInput.Select();
            ChatInput.ActivateInputField();
        }
    }

    [PunRPC] // RPC는 플레이어가 속해있는 방 모든 인원에게 전달한다
    void ChatRPC(string msg)
    {
        bool isInput = false;
        for (int i = 0; i < ChatText.Length; i++)
            if (ChatText[i].text == "")
            {
                isInput = true;
                ChatText[i].text = msg;
                break;
            }
        if (!isInput) // 꽉차면 한칸씩 위로 올림
        {
            for (int i = 1; i < ChatText.Length; i++) ChatText[i - 1].text = ChatText[i].text;
            ChatText[ChatText.Length - 1].text = msg;
            // 스크롤 제어 어색하지만 없는거보다 나은 것 같음
            StartCoroutine(SetValueScrollBarTop());
        } else {
            StartCoroutine(SetValueScrollBarBottom());
        }
    }
    
    // 스크롤 제어 로직 코루틴으로 구성
    IEnumerator SetValueScrollBarTop()
    {
        yield return null;
        bar.value = 0f;
    }

    IEnumerator SetValueScrollBarBottom()
    {
        yield return null;
        bar.value = 1f;
    }
}