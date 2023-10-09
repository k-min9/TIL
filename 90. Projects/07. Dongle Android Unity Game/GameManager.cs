using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour
{
    public GameObject dongleFrepab;

    public Transform dongleGroup;  // 동글 오브젝트 모을 그룹

    public Dongle lastDongle;

    private void Awake() {
        Application.targetFrameRate = 60;  // FPS 60 고정
    }
    
    void Start()
    {
        NextDongle();
    }

    // 새 동글 생성
    Dongle GetDongle() {
        GameObject instant = Instantiate(dongleFrepab, dongleGroup); // dongleGroup 자식으로 프리팹 생성
        Dongle instantDongle = instant.GetComponent<Dongle>();
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
        Dongle newDongle = GetDongle();
        lastDongle = newDongle;
        lastDongle.level = Random.Range(0,4);  // 랜덤 생성
        lastDongle.gameObject.SetActive(true);  // Dongle의 OnActive함수 실행시켜버리기 

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
}
