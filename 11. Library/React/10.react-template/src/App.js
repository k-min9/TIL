import { useEffect, useState } from "react";
import axios from 'axios';
import "./res/index.css";

const USER_NO = 'ME00001'

// 버튼 클래스
class Button {
  constructor(id) {
    this.id = id;
    this.isSelected = false;
  }
}


function App() {
  const [userName, setUserName] = useState('')
  const [tabNo, setTabNo] = useState(1)
  const [useSummary, setUseSummary] = useState({usage_count:0, usage_minute:0, usage_meter:0, carbon_reduction:0})
  const [useList, setUseList] = useState(null)
  const [buttons, setButtons] = useState([
    new Button('카드'), 
    new Button('포인트')
  ])  // 버튼 리스트 직접 입력
  const [apiButtons, setApiButtons] = useState([]);  // api로 버튼 리스트 받기
  const [selectedButtons, setSelectedButtons] = useState([]); // 선택 버튼 필터링

  const getUserName = () => {
    axios.get(`http://localhost:8080/api/v1/user/${USER_NO}/`)
    .then(response => {
      setUserName(response.data?.name)
    })
    .catch((err)=>console.log(err))
  }

  const getUseSummary = (ptype) => {
    axios.get(`http://localhost:8080/api/v1/user/${USER_NO}/usage/summary?ptype=${ptype}`)
    .then(response => {
      setUseSummary(response.data)
    })
    .catch((err)=>console.log(err)) 
  }

  const getUseList = (ptype) => {
    axios.get(`http://localhost:8080/api/v1/user/${USER_NO}/usage2/?ptype=${ptype}`)
    .then(response => {
      const list = response.data.list2
      const sortedList = list.slice().sort((a, b) => a.use_time - b.use_time);  // 시간별로 Sorted
      // const sortedList = list.slice().sort((a, b) => b.use_time - a.use_time);  // 시간별로 Sorted (역순, 내림차순)
      // const sortedList = list.slice().sort((a, b) => a.use_no.localeCompare(b.use_no));  // 문자별로 sorted
      // const sortedList = list.slice().sort((a, b) => b.use_no.localeCompare(a.use_no));  // 문자별로 sorted (역순, 내림차순)

      console.log(sortedList)
      setUseList(sortedList)
      // setUseList(response.data.list2)
    })
    .catch((err)=>console.log(err))
  }

  // 결제방식 받아와서 버튼만들기
  const getApiButtons = () => {
    axios.get(`http://localhost:8080/api/v1/pay_methods`)
    .then(response => {
      const apiData = response.data;
      // 방법1. 반복문
      var tmpButtons = []
            // 반복문을 사용하여 버튼 매핑
            for (let i = 0; i < apiData.length; i++) {
              const item = apiData[i];
              const button = new Button(item.id);
              tmpButtons.push(button);
            }

      // 방법2. map
      // const tmpButtons = apiData.map((item) => new Button(item.id));

      setApiButtons(tmpButtons)
    })
    .catch((err)=>console.log(err))
  }

  const onTabClick = (no) => {
    setTabNo(no)
    getUseSummary(no)
    getUseList(no)
  }

  const onTabButton = (id) => {
    const updatedButtons = buttons.map(btn => {
      if (btn.id === id) {
        btn.isSelected = !btn.isSelected;
      }
      return btn;
    });
    setButtons(updatedButtons);
  }

  const onTabButton2 = (id) => {
    const updatedButtons = apiButtons.map(btn => {
      if (btn.id === id) {
        btn.isSelected = !btn.isSelected;
      }
      return btn;
    });
    setApiButtons(updatedButtons);
  }

  // 선택된 버튼 update
  const updateSelectedButtons = () => {
    const selectedIds = buttons
      .filter((btn) => btn.isSelected)
      .map((btn) => btn.id);
    setSelectedButtons(selectedIds);
  };

  // 리스트 파싱
  const parsePayMethod = (payMethod) => {
    if (payMethod && Array.isArray(payMethod) && payMethod.length > 0) {
      const sortedMethods = payMethod.sort((a, b) => a.localeCompare(b));  // sort도 가능 (id일 경우 a.id.localeCompare(b.id))
      const tags = sortedMethods.map((method, idx) => (
        <span key={idx}>
          {`#${method}`}
          {idx !== sortedMethods.length - 1 && <span className="comma">, </span>}
        </span>
      ));
      return <div className="pay-method-tags">{tags}</div>;
    }
    return null;
  };

  // 금액 표시 : num번째마다 , 넣기
  // toLocaleString 써도 됨. 아래 예시 있음
  function numberWithCommas(x, num) {
    let str = x.toString();
    let result = '';
    let count = 0;
  
    for (let i = str.length - 1; i >= 0; i--) {
      result = str[i] + result;
      count++;
  
      if (count % num === 0 && i !== 0) {
        result = ',' + result;
      }
    }
  
    return result;
  }


  // 날짜 자르기
  function stringToDate(d) {
    const yy = d.substring(2, 4)
    const mm = d.substring(5, 7)
    const dd = d.substring(8, 10)
    const h = d.substring(11, 13)
    const m = d.substring(14, 16)
    return yy+'.'+mm+'.'+dd+' '+h+':'+m
  }

  useEffect(() => {
    getUserName()
    getUseSummary(1)
    getUseList(1)
    getApiButtons()
  }, [])

  // apiButton은 연습용이었으니 우선 제외
  useEffect(() => {
    updateSelectedButtons();
  }, [buttons]); 

  return (
    <div>
      <div className="main-title">
        <h1>서비스 이용내역</h1>
        <div>{userName}</div>
      </div>
      <hr />

      <div className="service-summary">
        <div className="service-summary-tab">
        {buttons.map((button) => (
            <button
              key={button.id}
              className={`tablinks${button.isSelected ? " on" : ""}`}
              onClick={() => onTabButton(button.id)}
            >{button.id}</button>))}
        </div>
        <div className="service-summary-tab">
        {apiButtons.map((button) => (
            <button
              key={button.id}
              className={`tablinks${button.isSelected ? " on" : ""}`}
              onClick={() => onTabButton2(button.id)}
            >{button.id}</button>))}
        </div>
        <div className="service-summary-tab">
          <button className={"tablinks"+ (tabNo === 1 ? " on" : "")} onClick={()=>{onTabClick(1)}}>1주일</button>
          <button className={"tablinks"+ (tabNo === 2 ? " on" : "")} onClick={()=>{onTabClick(2)}}>1개월</button>
          <button className={"tablinks"+ (tabNo === 3 ? " on" : "")} onClick={()=>{onTabClick(3)}}>3개월</button>
        </div>
        <div className="spacer-20"></div>
        <div className="service-summary-detail-container">
          <div className="color-gray">이용건수</div>
          <div>{useSummary.usage_count}건</div>
          <div className="color-gray">이용시간</div>
          <div>{useSummary.usage_minute}분</div>
          <div className="color-gray">이동거리</div>
          <div>{useSummary.usage_meter}m / {(useSummary.usage_meter / 1000).toFixed(2)}km</div>
          <div className="color-gray">탄소절감효과</div>
          <div>{useSummary.carbon_reduction}kg</div>
        </div>

        <hr />
        {useList !== null && useList.length > 0 ?
        (
        // 필터링 포함 map 하기
        <div class="service-list-container">
          {useList
            .filter((useDetail) => {
              const filteredPayMethod = useDetail.pay_method.filter((method) =>
                selectedButtons.includes(method)
              );
              return filteredPayMethod.length > 0 || selectedButtons.length === 0;
            })
            .map((useDetail, idx) => (
              <div key={idx}>
                <div class="service-list-content">
                  <div>
                    <span>{(useDetail.use_distance)/1000}km</span>
                    <span class="color-gray ml-10">{useDetail.use_time}분</span>
                  </div>
                  <div class="service-list-body">
                    <div class="color-gray">이용시간</div>
                    <div>{stringToDate(useDetail.use_start_dt)}~ {useDetail.use_end_dt}</div>
                    <div class="color-gray">결제일시</div>
                    <div>{useDetail.pay_datetime.substring(0,10)}</div>
                    <div class="color-gray">결제금액</div>
                    <div>
                      {
                          useDetail.card_pay !==0 && useDetail.point_pay !== 0 ? <div>카드 : {useDetail.card_pay}원 + 포인트 : {useDetail.point_pay}P</div> :
                          useDetail.card_pay !==0 ? <div>카드 : {useDetail.card_pay}원 </div>: <div>포인트 : {useDetail.point_pay}P </div>
                      }
                    </div>
                    <div class="color-gray">결제수단</div>
                    <div>
                      {parsePayMethod(useDetail.pay_method)}
                    </div>
                    <div class="color-gray">할인율</div>
                    <div class="color-gray">
                      {
                        useDetail.pay_discount !== null ? <div>{(useDetail.pay_discount*100).toFixed(0)}%</div>: <div>0%</div>
                      }
                    </div>
                    <div class="color-gray">최종금액</div>
                    {/* <div>{(useDetail.card_pay + useDetail.point_pay).toLocaleString('ko-KR')}원</div> */}
                    <div class>
                      {
                        useDetail.pay_discount !== null
                        ?
                        <div>
                          <span style={{ textDecoration: 'line-through', marginRight: '5px', color: 'red'}}>
                            {numberWithCommas(useDetail.card_pay + useDetail.point_pay, 3)}원
                          </span>
                          <span>
                            {numberWithCommas(((useDetail.card_pay + useDetail.point_pay) * (1 - useDetail.pay_discount)).toFixed(0), 3)}원
                          </span>
                        </div>
                        : 
                        <div>{numberWithCommas(useDetail.card_pay + useDetail.point_pay, 3)}원</div>
                      }
                    </div>
                  </div>
                </div>
                <hr />
              </div>
            ))}
        </div>
        )
        :
        (
        <div className="service-empty">
          <div className="service-empty-container">
            <div>
              조회된 정보가 없습니다.
            </div>
          </div>
        </div>
        )
      }
      </div>
    </div>
  )
}

export default App;
