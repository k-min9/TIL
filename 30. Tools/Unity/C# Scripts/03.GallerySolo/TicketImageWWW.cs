// using System.Collections;
// using System.Collections.Generic;
// using UnityEngine;

// public class TicketImage : MonoBehaviour
// {
//     public string url = "https://docs.unity3d.com/uploads/Main/ShadowIntro.png";

//     IEnumerator Start()
//     {
//         Texture2D tex;
//         tex = new Texture2D(4, 4, TextureFormat.DXT5Crunched, false);
//         using (WWW www = new WWW(url))
//         {
//             yield return www;
//             www.LoadImageIntoTexture(tex);
//             GetComponent<Renderer>().material.mainTexture = tex;
//         }
//     }

//     // 외부(react)에 의해 실행될 것이기 때문에 public 필수
//     public IEnumerator SetUrl(string ticketUrl)
//     {
//         url = ticketUrl;
//         Texture2D tex;
//         tex = new Texture2D(4, 4, TextureFormat.DXT5Crunched, false);
//         using (WWW www = new WWW(url))
//         {
//             yield return www;
//             www.LoadImageIntoTexture(tex);
//             GetComponent<Renderer>().material.mainTexture = tex;
//         }
//     }
    
// }
