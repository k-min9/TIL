import { useEffect, useState } from "react";
import axios from 'axios';
import "./res/index.css";

const USER_NO = 'ME0001'

function App() {
  const [userName, SetUserName] = useState('')

  const getUserName = () => {
    axios.get(`http://localhost:8080/api/v1/user/${USER_NO}/`)
    .then(response => {
      SetUserName(response.data?.name)
    })
  }

  useEffect(() => {
    // getUserName()
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
          <button className="tablinks on">1주일</button>
          <button className="tablinks">1개월</button>
          <button className="tablinks">3개월</button>
        </div>
        <div className="spacer-20"></div>
        <div className="service-summary-detail-container">
          <div className="color-gray">이용건수</div>
          <div>0건</div>
          <div className="color-gray">이용시간</div>
          <div>100분</div>
          <div className="color-gray">이동거리</div>
          <div>69.9km</div>
          <div className="color-gray">탄소절감효과</div>
          <div>8.7kg</div>
        </div>

        <hr />

        <div class="service-list-container">
          <div class="service-list-content">
            <div>
              <span>30km</span>
              <span class="color-gray ml-10">60분</span>
            </div>
            <div class="service-list-body">
              <div class="color-gray">이용시간</div>
              <div>22.01.01 08:00 ~ 22.01.31 09:00</div>
              <div class="color-gray">결제일시</div>
              <div>22.01.01</div>
              <div class="color-gray">결제수단</div>
              <div>카드 1000원</div>
            </div>
          </div>
          <hr />
        </div>

        <div className="service-empty">
          <div className="service-empty-container">
            <div>
              조회된 정보가 없습니다.
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App;
