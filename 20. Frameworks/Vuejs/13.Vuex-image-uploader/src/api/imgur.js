import qs from 'qs'

const CLIENT_ID = process.env.VUE_APP_IMGUR_CLIENT_ID
const ROOT_URL = 'https://api.imgur.com'

export default {
  login() {
    const queryObj = {
      client_id: CLIENT_ID,
      response_type: 'token',
    }
    // 주소 조합 (예상 완성 주소 : https://api.imgur.com/oauth2/authorize?client_id="우리APIid"&response_type=token)
    const fullUrl = `${ROOT_URL}/oauth2/authorize?${qs.stringify(queryObj)}`
    window.location.href = fullUrl
  },
  IMAGES_URL: `${ROOT_URL}/3/account/me/images`,
  UPLOAD_URL: `${ROOT_URL}/3/image`,
}