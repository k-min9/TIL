using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerCameraArm : MonoBehaviour
{
    // UI 완성시 이동 예정
    [SerializeField]
    private Transform cameraArm;  // 카메라 중심 회전 각도

    // bool isCameraMove = false;

    void Update()
    {
        // 3 버튼으로 카메라 제어 결정
        // if (Input.GetKeyDown(KeyCode.Alpha3)) {
        //     isCameraMove = !isCameraMove;
        // }
        LookAround();
    }

    // 마우스 움직임 감지하여 각도 조정
    private void LookAround() {
        if (GameManager.isCameraMove)
        {
            Vector2 mouseDelta = new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y"));
            Vector3 camAngle = cameraArm.rotation.eulerAngles;  // 현재 카메라의 오일러 각도

            // 회전각 제한을 위해 내용물 저장
            float x = camAngle.x - 2 * mouseDelta.y;  // 뺄 경우 마우스 아래로 보낼때 시야도 아래로 감, 반대로 하고 싶으면 더하면 됨
            if (x < 180f)  // 180도보다 작음 => 위쪽으로 회전하는 경우 : -1 ~ 70도로 제한
            {
                x = Mathf.Clamp(x, -1f, 70f);
            }
            else  // 180도보다 큼 => 아래쪽으로 회전하는 경우 335도(-25)~361도로 제한
            {
                x = Mathf.Clamp(x, 335f, 361f);
            }

            cameraArm.rotation = Quaternion.Euler(x, camAngle.y + 2* mouseDelta.x , camAngle.z);
        }
    }

}
