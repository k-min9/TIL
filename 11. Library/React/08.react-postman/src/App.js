import React from "react";
import axios from 'axios';

// CORS 등 체크용 postman 리액트 버전
function App() {
  const sendAPI = () => {
    // const token = localStorage.getItem('jwt');
    axios({
      method: 'POST',
      url: 'http://localhost:8080/login_jwt/1',
      // headers : {
      //   // credentials: 'include',
      //   // 'Access-Control-Allow-Credentials': true
      // },
      withCredentials: true
      // headers: { Authorization: token },
    })
      .then(res => {
        console.log(res)
      })
      .catch(err=> {
        console.log(err)
      });
  };

  return (
    <div>
      <h1>API 발사!</h1>
      <button
        variant="dark"
        sx={{
          width: '352px',
          height: '57px',
          textAlign: 'center',
          display: 'block',
          mt: '1rem',
          mb: '1rem',
          bgcolor: '#008ED0',
          ':hover': {
            color: '#006D9F',
            bgcolor: '#D5F2FC',
          },

          fontSize: '16px',
          fontWeight: 'bold',
          color: '#fff',
        }}
        onClick={sendAPI}
      >
        버튼
      </button>
    </div>
  );
}

export default App;
