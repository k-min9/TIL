// 위치 : 앱/static/accounts/js
const followBtn = document.querySelector('#followBtn')
const followersCount = document.querySelector('#followersCount')

followBtn.addEventListener('click', function (event) {
  const userId = event.target.dataset.userId
  const URI = `http://127.0.0.1:8000/accounts/${userId}/follow/`

  const reqConfig = {
    headers: {
      'X-CSRFToken': Cookies.get('csrftoken')
    }
  }

  axios.post(URI, {}, reqConfig)
    .then(res => {
      followersCount.innerText = res.data.followersCount
      
      if (res.data.isFollow){
        // 현재 팔로우 중이니까, 언팔 버튼으로 만들어야 함
        event.target.innerText = '언팔로우'
        event.target.classList = 'btn btn-danger'
        
      } else {
        // 현재 팔로우 중이 아니니까, 팔로우 버튼으로
        event.target.innerText = '팔로우'
        event.target.classList = 'btn btn-primary'
      }
    })
    .catch(err => console.error(err))
})