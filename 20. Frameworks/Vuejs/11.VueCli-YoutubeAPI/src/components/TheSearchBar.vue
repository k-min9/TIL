<template>
  <div class = "search-bar" :style="{ margin: videoLength ? '0' : '40vh 0'}"> <!--vh : vector height 중앙 상대값 잡아라-->
    <input @keyup.enter="onEnter" type="text"> <!--@keyup.enter= : 눌렸다가 떼이면-->
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  // 트랜잭션 연습
  props: {
    videoLength: Number,
  },
  methods: {
    onEnter(event){
      // 이런식으로 원하는 결과물을 찾기
      // console.log(event)
      // console.log(event.target.value)

      // event emit : 위로 발신 -> <the-search-value>가 들어줄테니 거기로 이동
      this.$emit('keyword-input', event.target.value) // 커스텀 이벤트 keyword-input을 만들었고 보내는 인자는 event.target.value라고 생각하면 된다.
      //this.$emit('keyword-input', {} ) // 텍스트 덩어리가 아니라 오브젝트를 넘기기
    }
  }

}
</script>

<style>
.search-bar > input {
  width: 100%;
  padding: 0.5rem;
  font-size: 2rem;
}

.search-bar {
  /* 반응형 간격 */
  transition-duration: 0.5s;
}

</style>