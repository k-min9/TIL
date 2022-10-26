# KakaoPay 결제 모듈 추가하기

- 범위 : 프론트(클라이언트)에서 백(서버)까지 일련의 과정 체크

## 적용

0. 준비 ; 카카오페이 사이트에서 API 등록

- 내 애플리케이션 → 애플리케이션 추가하기
- 들어갈 경우 Admin키가 있음 → 보안을 위해 yml 파일에 추가(gitgnore 했는지 확인!)
- 플랫폼 등록 ⇒ 웹 (적는것은 프론트!)

```java
// 작성 예시
http://localhost:3000
http://localhost:8080
http://localhost:8081
https://moviecurators-spring.netlify.app
등등등...
```

1. 클라이언트에서 요청 필요 → 반환값 : 결제 페이지 주소

```jsx
buyPremium: function() {
      // 실제 적용시, 이미 프리미엄 유저인지 확인하는 것 필요
      axios({
        method: 'GET',
        url: SERVER.URL + SERVER.ROUTES.accounts.kakaoPay,
        headers: this.token,
      })
      .then((res) => {
        window.location.href = res.data  // 결제 화면 전환        
      })
      .catch (() => {
        swal.fire ({
          icon: 'error',
          title: '결제 실패',
          text: '서버가 혼잡합니다. 다시 시도해 주세요.'
        })
      })
    }
```

2. 백(서버)에서 결제 페이지 주소를 반환하는 API 컨트롤러 생성 (Service 로직 생략)  

```java
@GetMapping("/kakaoPay/")
    public String kakaoPaymentReady() {
        String result = kakaoPayService.kakaoPayReady();
        return result;
    }
```

반환 주소 형식 예시 : [https://online-pay.kakao.com/mockup/v1/0c64fa4a17947ae4d2d554a3e31564fe3292cadc906ea2a3e7102e7808e8621f/info](https://online-pay.kakao.com/mockup/v1/0c64fa4a17947ae4d2d554a3e31564fe3292cadc906ea2a3e7102e7808e8621f/info)

3. 프론트가 반환된 주소를 받고 이동한다.  
(라우터 이동이 아니니까 느리다.)
4. **주의!**  
mock 결제용이기 때문에 결제를 신속하게 끝내야한다!  
안 그러면 결제 요청이 종료된 요청으로 변경되고, 답이 없어진다.  
5. 결제 화면 종료 시, 각각  
결제 실패시 : 프론트주소/kakaoPay/fail  
결제 취소시 : 프론트주소/kakaoPay/cancel  
결제 성공시 : 프론트주소/kakaoPay/success  
로 이동한다. **(주의) 이 행위의 주체는 카카오API**  
각각 핸들러에 해당 vue를 만들어 대응하고, router과 연결한다.  
6. 일단 예제에서는 실패, 취소시는 안내메시지와 함께 홈으로 보냈다.  
성공시에만, 결제 내역의 정보를 받을 수 있는 pg_token이 카카오 API로부터 발급되어 param으로 붙어 나온다.  
**이 시점에 이미 결제는 종료되었다.**  

7. 백 엔드에 pg_token을 보내면서, DB의 프리미엄 인증 여부를 Y로 바꾼다.  
해당 결제 내역 정보를 카카오 API로부터 받아올 수 있게 하고,  
차후 필요하면 결제 내용도 저장한다.  
반환 값으로 결제 내용을 보내는 예시 하나 넣었다.  
(Premium) 부분 하드코딩이 아닌 반환 부분  

## 느낀점  차후 고려사항

이중 결제, 결제 누락 등의 요소는 카카오페이 API에서 잘 처리를 해주지만,  
최종적으로 결제가 잘 되었다는 영수증으로 연결되는 pg_token은 프론트로 전달된다.  
백(서버)에서 이 정보를 누락없이 저장할 수 있게 하는 방법에 대한 고민이 필요할 것 같다.  
