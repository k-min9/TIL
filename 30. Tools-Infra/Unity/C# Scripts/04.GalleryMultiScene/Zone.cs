using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class Zone : MonoBehaviour
{
    // public RectTransform uiGroup;
    public GameObject uiGroup;

    public TMP_Text title;
    public TMP_Text description;

    public TextMesh ticketTitle;
    public TextMesh ticketDescription;

    public void Enter()
    {
        uiGroup.SetActive(true);
        // uiGroup.anchoredPosition = Vector3.down * 180;
        // title.text = "기본 text";
        title.text = ticketTitle.text;
        // description.text = "추가 설명";
        description.text = ticketDescription.text;
    }

    public void Exit()
    {
        uiGroup.SetActive(false);
        // uiGroup.anchoredPosition = Vector3.down * 1000;
    }

    // 외부(react)에 의해 실행될 것이기 때문에 public 필수
    public void SetTitle(string title)
    {
        ticketTitle.text = title;
    }

    public void SetDesc(string desc)
    {
        ticketDescription.text = desc;
    }

}
