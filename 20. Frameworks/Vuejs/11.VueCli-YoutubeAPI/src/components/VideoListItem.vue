<template>
    <li @click="onSelect" class="list-group-item">
      <!-- {{ video }} -->
      <!-- <img :src="video.snippet.thumbnails.default.url" alt=""> 너무 기니까 computed에 data로 넣어주자 -->
      <img :src="imgSrc" :alt="videoTitle">
      {{ videoTitle | unescape }}
    </li>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoListItem',
  props: {
    video: Object
  },
  methods: {
    onSelect() {
      this.$emit('select', this.video)
    }
  },
  computed: {
    imgSrc() {
      return this.video.snippet.thumbnails.default.url
    },
    videoTitle() {
      return this.video.snippet.title
    },
    // 재사용성 고려하지 않은 필터링 1번
    // goodText() {
    //   return _.unescape(this.video.snippet.title)
    // }
  },
  // 텍스트 관련 언이스케이프 이슈(문자열의 '을 보고 탈출한다던가)를 lodash가 해결해주니 {{ video.snippet.title | unescape }}로 필터링
  filters: {
    unescape(rawText) {
      return _.unescape(rawText)
    }
  }

}
</script>

<style>
.list-group .list-group-item {
  display: flex;
  margin-bottom: 1rem;
  cursor: pointer;
}

/* 마우스 올리면 위에 희미한 배경 */
.list-group .list-group-item:hover {
  background-color: #eee;
}

.list-group .list-group-item img {
  height: fit-content;
  margin-right: 0.5rem;
}

img {
  display: block;
}

</style>