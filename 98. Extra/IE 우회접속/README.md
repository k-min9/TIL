# IE 우회 접속

- 개요 : IE를 켤 경우 강제로 엣지가 켜지는 경우
- 대처
    1. CreateObject("InternetExplorer.Application").Visible=true 를 적은 .vbs 파일을 만들고 연다.
    2. Program Files > Microsoft > Edge > Application > *.*.*.* > BHO 폴더의 이름을 BHO_bak으로 바꾼다.
