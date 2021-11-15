<template>
  <div class = "d-flex justify-content-center align-items-center flex-column">
    <div><button @click="onClick" class="btn btn-success">Pick</button></div>
    <hr>
    <img :src="`https://image.tmdb.org/t/p/w300/${ randomMovie.poster_path }`" :alt="randomMovie.title">
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'Random',
  methods: {
    ...mapActions(['pickRandomMovie']),
    onClick() {
      this.pickRandomMovie(this.$store.state)
    },
  },
  computed: mapGetters(['randomMovie']),
  created() {
    this.pickRandomMovie(this.$store.state)
  }
}
</script>

<style>

</style>