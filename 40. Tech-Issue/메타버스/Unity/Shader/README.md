# Shader

- 개요 : 재질(Material)이 화면에 표시되는 방식(외형)을 정의.

## UnityChanToonShader2.0

- 개요 : 유니티에서 지원해준 기본적인 Toon 느낌의 Shader을 적용해보자.
- 설치
  - PackageManager에서 Add package by name : com.unity.toonshader
- 적용
  - 기존 Material와 Texture을 복사
  - 복사한 Material의 Shader을 Toon으로 변경
  - Three Color and Control Map Settings의 BaseMap을 변경하고, 관련 색상을 적용하기(흰색 추천)
  - fbx의 Inspector>Materials에서 Shader을 변경한 Material로 변경
- 기타
  - Light를 연한 노란색에서 흰색으로 바꿔주는게 좋음
