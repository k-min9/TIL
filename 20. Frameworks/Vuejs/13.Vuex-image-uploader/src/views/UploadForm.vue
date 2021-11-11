<template>
  <div class="dropper">
    <input type="file" @change="uploadImages" multiple accept="image/*">
    <span>Drag images here.</span>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'UploadForm',
  data() {
    return{
    }
  },
  // methods: {
  //   onChange(event) {
  //     console.log(event.target.files)
  //   }
  // }
  methods: mapActions(['uploadImages'])
}
</script>

<style scoped>
  .dropper {
    height: 30vh;
    border: 2px dashed black;
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
  }
  .dropper:hover {
    background: #eee;
  }
  input {
    width: 100%;
    height: 30vh;
    /* 부모 위치 기준으로 잡는 그거 해서 다른 글씨 올라가게 */
    position: absolute; 
    opacity: 0;
    cursor: pointer;
  }
</style>