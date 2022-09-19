# 새 안드로이드 스튜디오 프로젝트

## Get started

- 버전에 따른 바인딩 이슈
  1. `buildFeatures.viewBinding = true` 를 build.gradle(module)에 추가
  2. MainActivity 코드변경

```kotlin
class MainActivity : AppCompatActivity() {

    val binding by lazy { ActivityMainBinding.inflate(layoutInflater) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.btnSay

    }
}
```

- 디바이스 만들어두기
  1. 우측 상단 ADV 매니저
  2. Create Device
  3. Play Store 대응 기기 (Nexus 5) 선택하고, 
  Image는 OS를 말하는건데 API 레벨 25~31이면 아무거나!

## 구현

- 버튼 클릭시 실행되는 Listener 만들기 : `binding.btnSay.setOnClickListener() {}`
- textView 내용물 바꾸기 : .setText 쓰지 말고 `binding.btnSay.*text* = "Hello Kotlin!"` 로 쓰자
- 로그 : 자주 쓰는건 Log.d(”Tag”, “message”) > 하단 Logcat에서 확인가능, 검색에 Tag를 활용하자

## 레이아웃

- 종류
  - 컨스트레인트 레이아웃 : 기본 레이아웃, 
  위젯 사이의 제약조건(Constraint)만으로 쉽게 화면 구성
  - 리니어 레이아웃 : 가로/세로 배열에 쓰이는 경우가 있음
  스택형태로 입력되는것을 한쪽에 쌓아둠
    - 리니어 레이아웃은 넘치게 보는 효과는 없지만,
      컨테이너 - 스크롤 뷰를 써서 조절할 수 있다.
  - 프레임 레이아웃 : 레이어를 겹쳐서 쓸때 가장 빠르게 구현 가능
    - All attributes에서 layoutgravity로 위치를 조절해야 함
- Constraint 대상의 선 중앙 동그라미에서 연결할 곳으로 뻗으면 됨
우측 편집기에서 + 누르면 앵커 포인트까지 알아서 연결해 줌
- 추천 스타트 (앵커) 위치. 왼쪽 위나 아래쪽
- Constraint Chain : 여러 위젯 클릭 후 우클릭으로 Chains

## 위젯

- 많이쓰는 것은 위젯들은 팔레트 Common에 모여있음
- 텍스트
  - 텍스트 뷰 : 보여만 줌
  - Plain Text : 입력도 가능
  - textSize 조절시, dp 대신에 sp 추천(확대시 글자크기도 커짐)
  - singleLine : 여러줄을 한줄로, maxLine : 길어지면 잘라버림
- 프로그레스 바(레이아웃) : 로딩등에 사용. runOnUiThread
- Seek 바 (게이지 류)
- rating 바(별 5개)

## 리스너

1. val listener = object : view.OnClickListner{} 식으로 만들기
2. 내부 스코프에서 Ctrl+i 누르면 override 할 onClick 고를 수 있음
3. 만든 listener를 button.setOnClickListener(listener) 등으로 연결

- 그 외 강의에 소개 된 종류
  - addTextChangedListner(”tag”, “msg 입력된 값”)
  - setOnCheckedChangeListener() : 라디오버튼, 라디오그룹, 체크박스, 토글, 스위치
  - setOnSeekBarChangeListener() :터치, 트래킹(변화) 3종의 override

## Values.xml

실제 구현시에는 절대로 버튼 안에 텍스트, 사이즈 등을 넣지 않는다!
res - values - strings/dimens/colors.xml을 클릭하면
사용하고 싶은 내용을 미리 ID(name) 의 형태로 저장할 수 있다.

해당 내용은 attribute 설정 창에서 @string/Button_text 같은 느낌으로 사용할 수 있다.

- 종류
  - strings : 텍스트
  - dimens : textSize
  - colors : 색 범위

## Activity

- manifests에는 Activity 관련 시작 액티비티(엔트리 포인트), 서브 액티비티 등의 정보가 적혀있다.
- setContentView(xx)
- Intent : 안드로이드 기본 구성 요소 간의 통신을 위해 사용되는 메시지 객체(액티비티, 서비스)

- 메인액티비티

```kotlin
class MainActivity : AppCompatActivity() {

    val binding by lazy { ActivityMainBinding.inflate(layoutInflater) }

    lateinit var activityResultLauncher: ActivityResultLauncher<Intent>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        binding.btnSay.setOnClickListener() {
            binding.textSay.text = "Hello Kotlin!"
        }
        
        // Activity 반환 정보를 받을 코드 : ActivityResultLauncher
        activityResultLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult())
        { result ->
            if (result.resultCode == RESULT_OK) {
                val message = result.data?.getStringExtra("returnValue")
                binding.resultText.text = message
                Toast.makeText(this, "안녕하세요, " + message + "님", Toast.LENGTH_SHORT).show()
            }
        }

        binding.btnMove.setOnClickListener{
            val intent = Intent(this, SubActivity::class.java)
            // 정보 전달
            intent.putExtra("from1", "Hello Bundle!!!")
            intent.putExtra("from2", 2022)
            //startActivityForResult(intent, 99)  // deprecated
            activityResultLauncher.launch(intent)
        }
    }
}
```

- 서브액티비티

```kotlin
class SubActivity : AppCompatActivity() {

    val binding by lazy { ActivitySubBinding.inflate(layoutInflater) }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        // 위젯이 많을때는 with 스코프 쓰는게 편할수도 있음
        with(binding) {
            // 꺼내 쓸때는 타입지정을 해줘야함
            to1.text = intent.getStringExtra("from1")
            to2.text = "${intent.getIntExtra("from2", 0)}"  // 숫자를 꺼낸 후, 문자로 변환

            btnClose.setOnClickListener {
                val returnIntent = Intent()
                val message = editMessage.text.toString()
                returnIntent.putExtra("returnValue", message)
                setResult(Activity.RESULT_OK, returnIntent)
                finish()
            }
        }
    }
}
```

## 리사이클러뷰

뷰 객체는 사라지지 않지만 내용이 변하게 해서 무한히 쓰는 방법

## 프래그먼트

- 액티비티 화면의 일부를 나타내거나, 재사용 가능함
- 다른 액티비티나 프래그먼트에 호스팅이 필요
- 여러 프래그먼트를 쓸때는 FrameLayout을 아닐 경우는 그냥 Fragment를 사용
