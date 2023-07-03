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
  ])

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
    axios.get(`http://localhost:8080/api/v1/user/${USER_NO}/usage/?ptype=${ptype}`)
    .then(response => {
      setUseList(response.data)
      console.log(response.data)
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
  }, [])

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
          <div>{useSummary.usage_meter}km</div>
          <div>{(useSummary.use_distance / 1000).toFixed(2)}km</div> {/* 세번째 자리에서 둘째자리까지 반올림 */}
          <div className="color-gray">탄소절감효과</div>
          <div>{useSummary.carbon_reduction}kg</div>
        </div>

        <hr />
        {useList !== null ?
        (
        <div class="service-list-container">
          {useList.list.map(
            (useDatail,idx) => (
              <div>
                  <div class="service-list-content">
                  <div>
                    <span>{(useDatail.use_distance)/1000}km</span>
                    <span class="color-gray ml-10">{useDatail.use_time}분</span>
                  </div>
                  <div class="service-list-body">
                    <div class="color-gray">이용시간</div>
                    <div>{stringToDate(useDatail.use_start_dt)}~ {useDatail.use_end_dt}</div>
                    <div class="color-gray">결제일시</div>
                    <div>22.01.01</div>
                    <div class="color-gray">결제수단</div>
                    <div>
                      {
                          useDatail.card_pay !==0 && useDatail.point_pay !== 0 ? <div>카드 : {useDatail.card_pay}원 + 포인트 : {useDatail.point_pay}P</div> :
                          useDatail.card_pay !==0 ? <div>카드 : {useDatail.card_pay}원 </div>: <div>포인트 : {useDatail.point_pay}P </div>
                      }
                    </div>
                  </div>
                </div>
                <hr />
              </div>
            )
          )}
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
