using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;  // 포톤 기능 사용
using UnityEngine.UI;  // UI에 접속 시도 사항 등 표시
using Photon.Realtime;

// Canvas에 적용
public class PhotonLauncher : MonoBehaviourPunCallbacks  //  MonoBehaviour 기능 + 포톤 서비스에 의해 발생하는 콜백(이벤트, 메시지) 감지
{
    // 버전
    private string version = "1";
    public Text connectionInfoText;  // 네트워크 정보 표시용 텍스트
    public PhotonView PV;

    // 로비
    [Header("StartPanel")]
    public GameObject StartPanel;
    public InputField NickNameInput;
    public TextMesh NickName;

    [Header("GamePanel")]
    public GameObject GamePanel;

    [Header("ChattingPanel")]
    public GameObject ChattingPanel;
    public Text[] ChatText;
    public InputField ChatInput;

    void Start()
    {
        // Debug.Log("마스터 서버 연결중...");
        connectionInfoText.text = "상태 : 마스터 서버에 접속 중...";
        // 설정 정보(버전 빼고 기본 옵션)로 마스터 서버 접속 시도
        PhotonNetwork.GameVersion = version;
        PhotonNetwork.ConnectUsingSettings();  
    }

    void Update()
    {
        // 4 버튼으로 로비 판넬 보이기
        if (Input.GetKeyDown(KeyCode.Alpha4)) {
            ShowPanelStart();
        }
        // 5 버튼으로 게임 판넬 보이기
        if (Input.GetKeyDown(KeyCode.Alpha5)) {
            ShowPanelGame();
        }
        // 엔터 버튼으로 채팅 판넬 보이기, 채팅 보내기
        if (Input.GetKeyDown(KeyCode.Return)) {
            // 다른 곳에 focus 되어있는지라던가 인터넷 연결되었는지라던가 조건 더 필요함
            // if (ChattingPanel.activeSelf && ChatInput.isFocused) { 
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
        }        
    }

    // 마스터 서버 접속 성공시 자동 실행
    public override void OnConnectedToMaster()
    {
        // Debug.Log("마스터 서버 연결 성공!");
        connectionInfoText.text = "상태 : 온라인 - 마스터 서버";
        // 마스터 서버 연결시 로비로 연결
        PhotonNetwork.JoinLobby();
    }

    // 마스터 서버 접속 실패시 자동 실행
    public override void OnDisconnected(DisconnectCause cause)
    {
        base.OnDisconnected(cause);
    }

    // 로비에 연결시 자동으로 실행
    public override void OnJoinedLobby()
    {
        // Debug.Log("로비 연결 설공!");
        connectionInfoText.text = "상태 : 로비";
        SetNickName();

    }

    // 닉네임 설정
    public void SetNickName() {
        // 기본 닉네임 설정
        if (NickNameInput.text == "") NickNameInput.text = "Noname";
        PhotonNetwork.LocalPlayer.NickName = NickNameInput.text;
        NickName.text = NickNameInput.text;
    }

    // 판넬 제어
    public void ShowPanelStart() {
        StartPanel.SetActive(true);
        GamePanel.SetActive(false);
    }
    public void ShowPanelGame() {
        StartPanel.SetActive(false);
        GamePanel.SetActive(true);
    }
    public void ShowPanelChatting() {
        // ChattingPanel.SetActive(!ChattingPanel.activeSelf);
        GameManager.isChatting = true;
        ChattingPanel.SetActive(true);
        // 판넬 활성화 후 포커스
        ChatInput.Select();
        ChatInput.ActivateInputField();
    }

    // 방 만들기
    public void CreateRoom() {
        PhotonNetwork.CreateRoom(NickName.text + "의 방", new RoomOptions { MaxPlayers = 6 });
        connectionInfoText.text = "상태 : " + NickName.text + "의 방";
        ShowPanelGame();
    }

    // 아무 방이나 들어가기
    public void JoinRandomRoom() {
        PhotonNetwork.JoinRandomRoom();
        ShowPanelGame();
    }

    // 내가 방에 들어가면 실행됨
    public override void OnJoinedRoom()
    {
        connectionInfoText.text = "상태 : " + PhotonNetwork.CurrentRoom.Name;
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
        ShowPanelStart();
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
        }
    }

}
