using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public GameObject dongleFrepab;
    public Transform dongleGroup;  // 동글 오브젝트 모을 그룹
    public GameObject effectFrepabMerge;
    public Transform effectGroup;  // 효과이펙트 오브젝트 모을 그룹

    public AudioSource bgmPlayer;
    public AudioSource[] sfxPlayer;
    public AudioClip[] sfxClip;
    public enum Sfx {
        Ef_AlertSound,
        LevelUp, // Ef_blow1~4
        Ef_button1,
        Ef_button2,
        Ef_drop,
        Ef_photo,
        Ef_punch, // Ef_punch1~3
        Ef_UIChange,
        Ef_gameOver,
        Ef_Attach  // 접촉등
    };
    int sfxIdx;

    // 게임변수
    public int maxLevel;
    public int score = 0;
    public bool isGameOver;
    public Dongle lastDongle;

    private void Awake() {
        Application.targetFrameRate = 60;  // FPS 60 고정
    }
    
    void Start()
    {
        bgmPlayer.Play();
        NextDongle();
    }

    // 새 동글 생성
    Dongle GetDongle() {
        // 이펙트 생성
        GameObject effectMerge = Instantiate(effectFrepabMerge, effectGroup); // effectGroup 자식으로 프리팹 생성
        ParticleSystem instantEffectMerge = effectMerge.GetComponent<ParticleSystem>();

        // 동글생성
        GameObject instant = Instantiate(dongleFrepab, dongleGroup); // dongleGroup 자식으로 프리팹 생성
        Dongle instantDongle = instant.GetComponent<Dongle>();
        instantDongle.effectMerge = instantEffectMerge;

        return instantDongle;
    }

    // 시간 후 다음 동글 생성 Coroutine
    IEnumerator WaitNext() {
        while (lastDongle != null) {
            yield return null;
        }

        yield return new WaitForSeconds(1.5f);

        NextDongle();
    }

    // 다음 동글 가져오기
    void NextDongle() {
        if (isGameOver) return;  // 게임오버시 추가생산 없음

        Dongle newDongle = GetDongle();
        lastDongle = newDongle;
        lastDongle.gameManager = this;  // 게임매니저 초기화 (최대레벨 등의 변수 공유를 위한 초기화)
        lastDongle.level = Random.Range(0,4);  // 랜덤 생성
        lastDongle.gameObject.SetActive(true);  // Dongle의 OnActive함수 실행시켜버리기 

        SfxPlay(Sfx.Ef_UIChange);

        StartCoroutine("WaitNext"); // 다음 동글 생성 코루틴
    }

    public void TouchDown() {
        if (lastDongle == null) return;
        lastDongle.Drag();
    }

    public void TouchUp() {
        if (lastDongle == null) return;
        lastDongle.Drop();
        lastDongle = null;
    }

    public void GameOver() {
        if (isGameOver) return; // 한번만 실행
        isGameOver = true;

        StartCoroutine(GameOverRoutine());
    }

    IEnumerator GameOverRoutine() {
        // 장면 안의 모든 동글 가져오기
        Dongle[] dongles = FindObjectsOfType<Dongle>();

        SfxPlay(Sfx.Ef_gameOver);  // 게임오버사운드

        // 지우기 전 모든 동글의 물리효과 비활성화
        for (int i = 0; i < dongles.Length; i++)
        {
            dongles[i].rigid.simulated = false;
        }

        // 하나씩 접근해서 지우기
        for (int i = 0; i < dongles.Length; i++)
        {
            dongles[i].Hide(Vector3.up * 100); // 아주 큰 값으로 숨겨버리기
            yield return new WaitForSeconds(0.1f);
        }

        
        // yield return new WaitForSeconds(1f);
        
    }

    /* SFX 관련 */
    public void SfxPlay(Sfx type) {
        switch(type) {
            case Sfx.Ef_AlertSound:
                sfxPlayer[sfxIdx].clip = sfxClip[0];
                break;
            case Sfx.LevelUp:
                sfxPlayer[sfxIdx].clip = sfxClip[Random.Range(1,4)];
                break; 
            case Sfx.Ef_button1:
                sfxPlayer[sfxIdx].clip = sfxClip[5];
                break;  
            case Sfx.Ef_button2:
                sfxPlayer[sfxIdx].clip = sfxClip[6];
                break;  
            case Sfx.Ef_drop:
                sfxPlayer[sfxIdx].clip = sfxClip[7];
                break;    
            case Sfx.Ef_photo:
                sfxPlayer[sfxIdx].clip = sfxClip[8];
                break;                
            case Sfx.Ef_punch:
                sfxPlayer[sfxIdx].clip = sfxClip[Random.Range(9,11)];
                break;       
            case Sfx.Ef_UIChange:
                sfxPlayer[sfxIdx].clip = sfxClip[12];
                break;
            case Sfx.Ef_gameOver:
                sfxPlayer[sfxIdx].clip = sfxClip[13];
                break;
            case Sfx.Ef_Attach:
                sfxPlayer[sfxIdx].clip = sfxClip[14];
                break;
        }

        sfxPlayer[sfxIdx].Play();
        sfxIdx = (sfxIdx + 1) % sfxPlayer.Length;
    }


}
