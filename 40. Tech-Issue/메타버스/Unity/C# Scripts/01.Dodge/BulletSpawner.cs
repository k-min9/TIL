using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BulletSpawner : MonoBehaviour
{
    // 탄알 생성에 사용할 원본 프리팹 (public 설정)
    public GameObject bulletPrefab;
    // 생성주기 (최소, 최대)
    public float spawnRateMin = 0.5f;
    public float spawnRateMax = 3f; 

    private Transform target;  // 발사할 대상
    private float spawnRate;  // 생성 주기
    private float timeAfterSpawn;  // 최근 생성 시점에서 지난 시간



    void Start()
    {
        // 초기화
        timeAfterSpawn = 0f;
        spawnRate = Random.Range(spawnRateMin, spawnRateMax);
        target = FindObjectOfType<PlayerController>().transform;  // PlayerController 컴포넌트를 가진 게임 오브젝트를 찾아 조준 대상으로 설정
    }

    void Update()
    {
        // timeAfterSpawn 갱신
        // Time.deltaTime은 컴퓨터의 성능과 상관없이 일정한 주기의 시간 간격(1/프레임역수 << 프레임 제한 해제나 다른 프레임 환경에서도 동일 동작)으로 고정시켜준다.
        timeAfterSpawn += Time.deltaTime;

        // 주기 달성시 총알 생성
        if (timeAfterSpawn >= spawnRate) {
            // 누적 시간 초기화
            timeAfterSpawn = 0f;

            // 프리팹의 복제(인스턴스화) 생성
            // transform.position : 자신의 위치
            // transform.rotation : 자신의 회전
            GameObject bullet = Instantiate(bulletPrefab, transform.position, transform.rotation);
            bullet.transform.LookAt(target);  // 타겟을 보게 설정

            // 다음 생성 간격 설정
            spawnRate = Random.Range(spawnRateMin, spawnRateMax);
        }




    }
}
