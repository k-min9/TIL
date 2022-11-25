using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Photon.Pun;  // 포톤 기능 사용
using UnityEngine.UI;  // UI에 접속 시도 사항 등 표시
using Photon.Realtime;
using TMPro;
using UnityEngine.SceneManagement;
using Hashtable = ExitGames.Client.Photon.Hashtable;
using System.Runtime.InteropServices;

public class PhotonCommuLobby : MonoBehaviourPunCallbacks
{
    // 버전
    private string version = "1";
    public Text connectionInfoText;  // 네트워크 정보 표시용 텍스트
    public PhotonView PV;
    public GameObject playerPrefab;

    // 로비
    [Header("LobbyPanel")]
    public GameObject LobbyPanel;
    public TMP_InputField NickNameInput;
    public Button[] EnterBtn;
    public Text TextAlert;
    public Text TextAlertNickname;

    // 채팅 패널 통일 가능?
    [Header("ChattingPanel")]
    public GameObject ChattingPanel;
    public Text[] ChatText;
    public TMP_InputField ChatInput;
    public Scrollbar bar;

    // 방 정보
    List<string> commuList = new List<string>();
    int currentPage = 1, maxPage, multiple;

    // 내보낼 변수
    public string roomName;

    // 함수 내보내기
    [DllImport("__Internal")]
    private static extern void GetRoomName(string roomName);
    [DllImport("__Internal")]
    private static extern void GetNickName(string nickName);

    void Start()
    {
        connectionInfoText.text = "상태 : 로비";
        NickNameInput.text = PhotonNetwork.LocalPlayer.NickName;
        // 초기 포커스
        // NickNameInput.Select();
        // NickNameInput.ActivateInputField();

        // 초기 방정보 세팅
        commuList.Add("SSAFY 커뮤니티");
        if (GameManager.roomCount != 0) EnterBtn[0].transform.GetChild(1).GetComponent<Text>().text = GameManager.roomCount + "/" +GameManager.roomMax;

        // Input Field 엔터 입력시 Submit 작동
        // RoomNameInput.onSubmit.AddListener(delegate{RoomNameSubmit(RoomNameInput);});

        // Debug.Log("마스터 서버 연결중...");
        // connectionInfoText.text = "상태 : 마스터 서버에 접속 중...";
        // 설정 정보(버전 빼고 기본 옵션)로 마스터 서버 접속 시도
        // PhotonNetwork.GameVersion = version;
        // PhotonNetwork.ConnectUsingSettings();  
        // 버튼, 입력창 기본 비활성화
        // NickNameInput.interactable = false;
        // for (int i = 0; i < StartPanelButton.Length; i++) StartPanelButton[i].interactable = false;
    }

    void commuListRenewal() 
    {
        // Debug.Log(commuList.Count);
        // 로비 인원수 갱신
        currentPage = 1;
        multiple = (currentPage - 1) * EnterBtn.Length;
        for (int i = 0; i < EnterBtn.Length; i++)
        {        
            EnterBtn[i].interactable = (multiple + i < commuList.Count) ? true : false;
            EnterBtn[i].transform.GetChild(0).GetComponent<Text>().text = (multiple + i < commuList.Count) ? commuList[multiple + i] : "";
            // 커뮤니티 이미 생성 되어 있음
            // EnterBtn[i].transform.GetChild(1).GetComponent<Text>().text = (multiple + i < commuList.Count) ? commuList[multiple + i].PlayerCount + "/" + commuList[multiple + i].MaxPlayers : "";
        }
    }

    public override void OnRoomListUpdate(List<RoomInfo> roomList)
    {
        int roomCount = roomList.Count;
        for (int i = 0; i < roomCount; i++)
        {
            if (roomList[i].Name == "SSAFY 커뮤니티")
            {
                EnterBtn[0].transform.GetChild(1).GetComponent<Text>().text = (roomList[i].PlayerCount != 0) ? roomList[i].PlayerCount + "/" + roomList[i].MaxPlayers : "0/18";
                GameManager.roomCount = roomList[i].PlayerCount;
                GameManager.roomMax = roomList[i].MaxPlayers;
            }
            // if (!roomList[i].RemovedFromList)
            // {
            //     if (!myList.Contains(roomList[i])) myList.Add(roomList[i]);
            //     else myList[myList.IndexOf(roomList[i])] = roomList[i];
            // }
            // else if (myList.IndexOf(roomList[i]) != -1) myList.RemoveAt(myList.IndexOf(roomList[i]));
        }
    }


    void Update()
    {

        // 로비 인원수 갱신
        commuListRenewal();

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
            } else {
                SetNickName();
            }
        }        
    }

    // // 마스터 서버 접속 성공시 자동 실행
    // public override void OnConnectedToMaster()
    // {
    //     // Debug.Log("마스터 서버 연결 성공!");
    //     connectionInfoText.text = "상태 : 온라인 - 마스터 서버";
    //     // 마스터 서버 연결시 로비로 연결
    //     PhotonNetwork.JoinLobby();
    // }

    // 마스터 서버 접속 실패시 자동 실행
    public override void OnDisconnected(DisconnectCause cause)
    {
        base.OnDisconnected(cause);
    }

    // 로비에 연결시 자동으로 실행
    public override void OnJoinedLobby()
    {
        // 방에 들어가있지 않은 상태
        GameManager.isPlaying = false;
        connectionInfoText.text = "상태 : 로비";
        SetNickNameInit();
        // 버튼 기본 활성화
        // NickNameInput.interactable = true;
        // for (int i = 0; i < StartPanelButton.Length; i++) StartPanelButton[i].interactable = true;
        // 채팅 판넬 및 기록 초기화
        GameManager.isChatting = false;
        ChattingPanel.SetActive(false);
        for (int i = 0; i < ChatText.Length; i++) ChatText[i].text = "";

    }

    // 닉네임 초기 설정
    public void SetNickNameInit() {
        // 기본 닉네임 설정
        if (NickNameInput.text == "") NickNameInput.text = "Noname";
        PhotonNetwork.LocalPlayer.NickName = NickNameInput.text;
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetNickName(NickNameInput.text);
        return;
    #endif
    }

    // 닉네임 설정
    public void SetNickName() {
        // 기본 닉네임 설정
        if (NickNameInput.text == "") NickNameInput.text = "Noname";
        PhotonNetwork.LocalPlayer.NickName = NickNameInput.text;
        TextAlertNickname.text = "닉네임이 변경되었습니다.";
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        GetNickName(NickNameInput.text);
        return;
    #endif
    }

    // 엔터로 방 이름 입력 받기
    // void RoomNameSubmit(TMP_InputField input) {
    //     if (input.text.Length > 0) CreateRoomRequest();
    // }

    // 판넬 제어
    public void ShowPanelChatting() {
        GameManager.isChatting = true;
        ChattingPanel.SetActive(true);
        // 판넬 활성화 후 포커스
        ChatInput.Select();
        ChatInput.ActivateInputField();
    }

    // 방 만들기 통합 관리
    public void CreateRoomRequest() {
        // if (RoomNameInput.text == "") return;
        // *** react <-> unity 환경
    #if UNITY_WEBGL == true && UNITY_EDITOR == false
        roomName = "commuSSAFY";
        // roomName = roomName.Substring(0, roomName.LastIndexOf('의'));
        GetRoomName(roomName);
        return;
    #endif
        // *** 개발환경
        CreateCommu();
    }  
    
    // 방 정보 들어오면 그대로 세팅
    public void CreateRoomWebGL(string roomType) {
        RoomOptions ro = new RoomOptions();
        ro.MaxPlayers = 18;
        // ro.IsVisible = false;
        ro.CustomRoomProperties = new Hashtable() {{"roomType", roomType}};

        PhotonNetwork.JoinOrCreateRoom("SSAFY 커뮤니티", ro, null);
        connectionInfoText.text = "상태 : " + "SSAFY 커뮤니티";
        // GameManager.roomType = "GalleryS";
        // 방 입장시 react 쪽에 기본적인 정보를 보내보자
    // #if UNITY_WEBGL == true && UNITY_EDITOR == false
    //     roomName = PhotonNetwork.NickName;
    //     // roomName = roomName.Substring(0, roomName.LastIndexOf('의'));
    //     GetRoomName(roomName);
    // #endif
    }

    // 커뮤니티 만들기
    public void CreateCommu() {

        RoomOptions ro = new RoomOptions();
        ro.MaxPlayers = 18;
        // ro.IsVisible = false;
        ro.CustomRoomProperties = new Hashtable() {{"roomType", "CommuSSAFY"}};

        // PhotonNetwork.JoinOrCreateRoom(PhotonNetwork.NickName + "의 방", ro, null);
        // connectionInfoText.text = "상태 : " + PhotonNetwork.NickName + "의 방";
        PhotonNetwork.JoinOrCreateRoom("SSAFY 커뮤니티", ro, null);
        connectionInfoText.text = "상태 : " + "SSAFY 커뮤니티";

        // GameManager.roomType = "GalleryM";
        // 방 입장시 react 쪽에 기본적인 정보를 보내보자
    // #if UNITY_WEBGL == true && UNITY_EDITOR == false
    //     roomName = PhotonNetwork.NickName;
    //     // roomName = roomName.Substring(0, roomName.LastIndexOf('의'));
    //     GetRoomName(roomName);
    // #endif
    }

    // react에서 방 들어갈때 경고문 설정
    public void SetErrorMessage(string message)
    {
        TextAlert.text = message;
    }


    // 아무 방이나 들어가기
    public void JoinRandomRoom() {
        PhotonNetwork.JoinRandomRoom();
    }

    // 내가 방에 들어가면 실행됨
    public override void OnJoinedRoom()
    {
        Hashtable CP = PhotonNetwork.CurrentRoom.CustomProperties;
        GameManager.roomType = CP["roomType"].ToString();
        GameManager.isPlaying = true;
        // connectionInfoText.text = "상태 : " + PhotonNetwork.CurrentRoom.Name;
        // PhotonNetwork.LoadLevel("GalleryM");
        PhotonNetwork.LoadLevel(GameManager.roomType);
        // SpawnPlayer();
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
    }

    // 홈으로 이동 (버튼)
    public void MoveSceneToStart() {
        SceneManager.LoadScene("Start");
    }

    // 플레이어 생성
    // private void SpawnPlayer() {
    //     // 생성 랜덤 위치
    //     Vector3 randomSpawnPos = Random.insideUnitSphere * 3f;
    //     randomSpawnPos.y = 0f;
    //     // 생성
    //     PhotonNetwork.Instantiate(playerPrefab.name, randomSpawnPos, Quaternion.identity);
    //     // 카메라 세팅
    //     // Camera.main.GetComponent<PlayerCamera>().setPlayer(gameObject.transform);
    // }


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
