<template>
  <div v-if="isLoggedIn" class = "image-container">
    <img v-for="image in allImages"
      :key="image.id" 
      :src="image.link" 
      :alt="image.name"
    >
  </div>
  <div v-else class="welcome-page">
    <span>로그인 해주세요</span>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ImageList',
  methods: mapActions(['fetchImages', ]),
  computed: mapGetters(['allImages', 'isLoggedIn']),
  created() {
    this.fetchImages()
  }
}
</script>

<style>
.welcome-page {
    font-size: 3rem;
    height: 40vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
.image-container {
  column-count: 3;
  column-gap: 0;
}

img {
  max-width: 100%;
  padding: 5px
}

</style>