# Firebase RTDB로 실시간 알림 구현하기

## 개요

Firebase realtime database 는 데이터가 변경되면 자동으로 앱에도 그 변경된 데이터를 즉시 적용시켜 준다.  
아마 방법은 API 등록 후 messaging을 통한 pub/sub. 따라서 별도의 알림 요청 승인이 필요하지 않다.  

## 서비스 제공자 쪽 세팅

1. Firebase 콘솔 프로젝트 만들기 (GCP에 프로젝트 있을 경우 그거 선택)
2. 설정 → 프로젝트 설정 → 서비스 계정 → 새 비공개 키 생성
3. realtimedatabase 생성 후 주소 확인

    ```jsx
    https://tupli-firebase-default-rtdb.firebaseio.com/
    ```

4. 설정 → 웹 앱 추가후 안내문 확인

    ```jsx
    // Import the functions you need from the SDKs you need
    import { initializeApp } from "firebase/app";
    import { getAnalytics } from "firebase/analytics";
    // TODO: Add SDKs for Firebase products that you want to use
    // https://firebase.google.com/docs/web/setup#available-libraries

    // Your web app's Firebase configuration
    // For Firebase JS SDK v7.20.0 and later, measurementId is optional
    const firebaseConfig = {
      apiKey: "API키",
      authDomain: "M9-firebase.firebaseapp.com",
      databaseURL: "https://M9-firebase-default-rtdb.firebaseio.com",
      projectId: "프로젝트ID",
      storageBucket: "M9-firebase.appspot.com",
      messagingSenderId: "385254978962",
      appId: "무언가ID",
      measurementId: "G-D577285Q8R"
    };

    // Initialize Firebase
    const app = initializeApp(firebaseConfig);
    const analytics = getAnalytics(app);
    ```

## 프론트 (클라이언트, Vue)

1. npm firebase 설치

    ```yaml
    npm install --save firebase
    ```

2. main.js에 추가

    ```jsx
    import firebase from 'firebase/compat/app';  //firebase 9 버전 이상

    // 예시 api (실제 저장소는 다른거 쓰고 있음)
    var firebaseConfig = {
      apiKey: 'AIzaSyBOwXLnkFr6vXaIMQ_1lr79ZytPF4gKnkU',
      authDomain: 'commitment-27df4.firebaseapp.com',
      databaseURL: 'https://commitment-27df4-default-rtdb.firebaseio.com',
      projectId: 'commitment-27df4',
      storageBucket: 'commitment-27df4.appspot.com',
      messagingSenderId: '998462999422',
      appId: '1:998462999422:web:c26a5bdbe4ea16530a812f',
      measurementId: 'G-GWYNQDQEEV',
    };

    firebase.initializeApp(firebaseConfig)
    ```

3. components > alarm > Alarm.vue 추가  
핵심 : store에 getters 요청, watch에 immediate와 handler를 사용한 조합

    ```jsx
    <template>
      <div>
      </div>
    </template>

    <script>
    import { mapGetters } from 'vuex';

    export default {
      name: 'Alarm',
      data() {
        return {
          newComments: [],
        }
      },
      computed: {
        ...mapGetters({
          realtime: ['getRealtimeAlarmList']
        })
      },
      watch: {
        realtime: {
          immediate: true,
          handler(val) {
            console.log(val)
            this.newAlarms = val;
          }
        }
      }

    }
    </script>

    <style scoped>

    </style>
    ```

4. store에 getters와 관련 state, mutation, action 추가

    ```jsx
    import firebase from 'firebase/compat/app';
    import 'firebase/compat/database';

    // state (알람 내용 저장)
    ...
        realtimeAlarmList: [],
    ...

    // getters
    getRealtimeAlarmList: function(state) {
          return state.realtimeAlarmList;
    }

    // mutations (가져온 알람 갱신)
    GET_REALTIME_ALARM_LIST(state, res) {
          state.realtimeAlarmList = res;
        },

    // actions (firebase db에서 알람 가져오기 - 요청없음, 자동갱신)
    // 관련 함수 : https://firebase.google.com/docs/reference/js/v8/firebase.database.Reference
    getRealtimeAlarm({commit}) {
          console.log('alarm')
          firebase
            .database()
            .ref()
            // .ref('user_list')
            // .ref('playroom_list')
            .limitToLast(5)
            .on('value', (snap) => {
              let res = snap.val();
              console.log('alarm', res)
              const tmp = [];
              for (const idx in res) {
                res[idx].id = idx;
                tmp.unshift({
                  username: res[idx].username,
                  // address: res[idx].dataId,
                  // img: res[idx].profile,
                  // email: res[idx].userEmail,
                });
              }
              commit('GET_REALTIME_ALARM_LIST', tmp);
            });
        },
    ```

5. App.vue에 action 요청 추가

    ```jsx
    import { mapActions } from 'vuex';

    methods: {
        ...mapActions(['getRealtimeAlarm']),
      },
      created() {
        this.getRealtimeAlarm();
      },
    ```

6. 알람 띄울 곳에 Alarms.vue를 컴포넌트로 가지게 설정 > 예시에서는 NavBar.vue  

    ```jsx
    <template>

        ...
        <Alarm />
        ...

    </template>

    <script>
    import Alarm from '@/components/alarm/Alarm'

    export default {
      ...
      components: {
        Alarm
      },
    ```

기타. 환경변수 설정 등 귀찮으니까 config>firebase.js파일로 빼서 분리  

  ```jsx
  // config > firebase.js
  const firebaseConfig = {
    apiKey: "AIzaSyDJEye4GVkPyt2FAsqdJNr0YIz43S-fU4I",
    authDomain: "tupli-firebase.firebaseapp.com",
    databaseURL: "https://tupli-firebase-default-rtdb.firebaseio.com",
    projectId: "tupli-firebase",
    storageBucket: "tupli-firebase.appspot.com",
    messagingSenderId: "385254978962",
    appId: "1:385254978962:web:8b6d35d9639adab9edfd4b",
    measurementId: "G-D577285Q8R"
  };

  export {firebaseConfig};

  // main.js
  import {firebaseConfig} from './config/firebase'

  // gitgnore
  #LOCAL
  /src/config/firebase.js
  ```

## 백 (서버, 스프링)

1. build_gradle 설정

    ```yaml
    // firebase 실시간 DB 연동
      implementation group: 'com.google.firebase', name: 'firebase-admin', version: '8.1.0'
    ```

2. resources에 google cloud에서 editor 수준의 권한 key 설정하여 배치하고 application.yml 설정으로 google cloud와 충돌 방지(필수!)

    ```yaml
    spring:
      cloud:
          gcp:
            firestore:
              enabled: false
    ```

3. key를 이용한 firebaseInitialize 설정 (하는 짓은 config인데 @Service붙임...)
4. 관련 service에 DB 저장 로직 작성

    ```java
    public void saveNoti() {
            // 저장할 데이터 DTO
            NotificationDto notificationDto = new NotificationDto();

            // 세부 설정
            String type = "민구Test2";
            notificationDto.setType(type);

            final FirebaseDatabase database = FirebaseDatabase.getInstance();
            DatabaseReference ref = database.getReference("noti"); // 최상위 root: noti, 없으면 만들어줌
            String toId = "메시지 갑니다!!!";

            //ref.child로 root 다음 key 선정(다훈씨 가요옷)
            DatabaseReference notiRef = ref.child(toId); // 알림 받는 사람의 닉네임
            DatabaseReference nextNotiRef = notiRef.push(); // 다음 키값으로 푸시
            String postId = nextNotiRef.getKey(); // 현재 알람의1 키값을 가져옴
            DatabaseReference saveNoti = notiRef.child(postId); // to의 아이디 값의 child node

            saveNoti.setValueAsync(notificationDto);
        }
    ```

5. 끝! 확인과 테스트!
