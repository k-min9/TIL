// using System.Collections;
// using System.Collections.Generic;
// using UnityEngine;
// using UnityEngine.Networking;

// public class TicketImage : MonoBehaviour
// {
//     public string url = "https://docs.unity3d.com/uploads/Main/ShadowIntro.png";

//     void Start()
//     {
//         StartCoroutine(GetText());
//     }

//     IEnumerator GetText()
//     {
//         using (UnityWebRequest uwr = UnityWebRequestTexture.GetTexture(url))
//         {
//             // uwr.SetRequestHeader("Access-Control-Allow-Origin", "*");
//             // uwr.SetRequestHeader("Access-Control-Allow-Headers", "*");
//             yield return uwr.SendWebRequest();
//             if (uwr.result != UnityWebRequest.Result.Success)
//             {
//                 Debug.Log(uwr.error);
//             }
//             else
//             {
//                 GetComponent<Renderer>().material.mainTexture = DownloadHandlerTexture.GetContent(uwr);
//             }
//         }
//     }

//     // 외부(react)에 의해 실행될 것이기 때문에 public 필수
//     public void SetUrl(string ticketUrl)
//     {
//         url = ticketUrl;
//         StartCoroutine(GetText());
//     }
// }