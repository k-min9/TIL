using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LookCamera : MonoBehaviour
{
    public static Camera Cam;

    void Update()
    {  
        if(Cam != null) transform.rotation = Cam.transform.rotation;
    }

    public static void SetCam(Camera camera) {
        Cam = camera;
    }
}