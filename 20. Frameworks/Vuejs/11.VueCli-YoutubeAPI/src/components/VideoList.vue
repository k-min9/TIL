<template>
  <ul class="video-list list-group"> <!-- list-group은 실제로 부트스트랩 지원임 -->
    <video-list-item 
      v-for="video in videos"
      :key="video.id.videoId"
      :video= "video"
      @select="onSelect"
    ></video-list-item>
    <!-- 자체 타이틀 재생 -> 그러나 우리는 하위 컴포넌트로 넘길 예정이기 때문에 ListItem에서 정리할 것이다.
    <li v-for="video in videos" :key="video.id.videoId">
      {{ video.snippet.title }}
    </li> -->
  </ul>
</template>

<script>
import VideoListItem from '@/components/VideoListItem.vue'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  methods: {
    // payload는 너무 범용적인 이름이니까 명시적으로 video라고 지음
    onSelect(video) {
      this.$emit('select', video)

    }
  },
  // 받을 인자
  props: {
    videos: Array,
    // 자세하게 쓰는 법
    // videos: {
    //   type: Array,
    //   required: true
    // }
  }
}
</script>

<!--scoped : 현재 컴포넌트의 엘리먼트만 적용-->
<style scoped> 
.video-list {
  padding: 0;
  margin: 0;
  list-style-type: none;
  width: 30%;
}
</style>