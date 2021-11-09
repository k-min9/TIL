<template>
  <!-- <div v-if="video"> video 값이 있을 때만 표시하라고 표기, 다만 이 예제는 video가 null이 아니라 {}라서 여기서 체크 못함 -->
  <div v-if="isVideo" class="video-detail">
    <div class="video-container">
      <iframe :src="videoSrc" frameborder="0"></iframe>
    </div>
    <h2>{{ video.snippet.title | unescape }}</h2>
    <hr>
    <p>{{ video.snippet.description | unescape }}</p>
  </div>

</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
    video: Object,
  },
  computed: {
    videoSrc() {
      if (this.isVideo){
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      } else {
        return ''
      }
    },
    isVideo() {
      return !_.isEmpty(this.video)
    },

  },
  // 실제로 ListItem의 필터를 재사용
  filters: {
    unescape(rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>
.video-detail {
  width: 70%;
  padding-right: 1rem;
}

.video-container {
  position: relative;
  padding-top: 56.25%;
}

.video-container > iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

</style>