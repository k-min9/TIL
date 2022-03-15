using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class LookCamera : MonoBehaviour
{
    public GameObject Cam;

    void Update()
    {
        transform.rotation = Cam.transform.rotation;
    }
}