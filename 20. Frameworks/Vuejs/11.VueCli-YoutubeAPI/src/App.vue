<template>
<div class>
  <h1>Youtube Browser</h1>
  <!-- 2단계 등록 -->
  <!--<TheSearchBar></TheSearchBar>도 가능, 각자 팀에 맞는 규격쓰기-->
  <header>
    <the-search-bar 
      @keyword-input="onKeywordInput"
      :video-length="videos.length"
      ></the-search-bar>
  </header>
  <section>
    <video-detail :video="selectedVideo"></video-detail> <!--클릭해서 받은 정보를 detail에 내려줌-->
    <video-list :videos='videos' @select="onSelect"></video-list> <!--인자처럼 보냄-->
  </section>  

</div>
</template>

<script>
// 1단계 : import
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoList from '@/components/VideoList.vue'
import VideoDetail from '@/components/VideoDetail.vue'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY //env.local에 APIKEY 환경변수로 저장
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  // 2단계 : 등록
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail
  },
  data() {
    return {
      inputKeyword: '',
      videos: [],
      selectedVideo: {},  // 이 방식이면 null이 아니라 v-if="video에서 못 잡기는 함"
    }
  },
  methods: {
    onKeywordInput(keyword) {
      // searchbar에서 데이터가 올라옴
      console.log(keyword)
      // keyword가 저장할 가치가 있으니 data()로 저장해두었다.
      this.inputKeyword = keyword
      this.fetchVideos(this.inputKeyword)
    },

    onSelect(video) {
      this.selectedVideo = video
    },

    fetchVideos(keyword) {
      const params = {
        key: API_KEY,
        part: 'snippet',
        type: 'video',
        q:keyword
      }
      axios({method : 'get', url : API_URL, params})
      //.then(res => console.log(res.data)) , data 내용 파악.
      //.then(res => this.videos = res.data.items) // array 반환하여 data에 저장
      .then(res => {
        this.videos = res.data.items
        this.selectedVideo = this.videos[0] // 초기값 설정 버전
      })
      .catch(err => console.error(err))
    },
  }

}
</script>

<!--scss 패키지가 내장되어있으니까 써보자-->
<!--sass 개발단계(-D)에서 필요한 로더 : npm install -D sass-loader@^10 sass-->
<style lang="scss">
@import 'bootstrap/scss/bootstrap';

// 이러면 둘 다 적용
section,
header {
  width: 80%;
  margin: 0 auto;
  padding: 1rem 0;
}

section {
  display: flex,
}

</style>