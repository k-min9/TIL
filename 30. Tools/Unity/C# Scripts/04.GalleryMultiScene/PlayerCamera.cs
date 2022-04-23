using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCamera : MonoBehaviour
{
    private Camera mainCamera;

    private Transform target;  // 카메라가 따라갈 대상
    public Vector3 offset;  // 위치 오프 셋, 카메라 최초 position값 넣으면 됨

    // 휠로 카메라 이동
    public float rotateSpeed = 10.0f;
    public float zoomSpeed = 10.0f;

    void Start()
    {
        mainCamera = GetComponent<Camera>();
    }

    void Update()
    {
        if (target != null) {
            Zoom();
            transform.position = target.position + offset;
            
        }
    }

    void Zoom()
    {
        float distance = Input.GetAxis("Mouse ScrollWheel") * -1 * zoomSpeed;
        if(distance != 0)
        {
            // 최대 줌인, 줌아웃
            float nextDistance = mainCamera.fieldOfView + distance;
            if (nextDistance < 20.0f) nextDistance = 20.0f;
            if (nextDistance > 100.0f) nextDistance = 100.0f;
            mainCamera.fieldOfView = nextDistance;
        }
    }

    public void setPlayer(Transform player)
    {
        target = player;
        // 닉네임 카메라 세팅
        LookCamera.SetCam(mainCamera);
    }
}
