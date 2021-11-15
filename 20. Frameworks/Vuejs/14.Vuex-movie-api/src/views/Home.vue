<template>
  <div>
    <h1>Home</h1>
    <article class="container">
      <div class="row mb-5 g-3">
        <movie-card
          v-for="movieCard in movieCards"
          :key="movieCard.id"
          :movieCard="movieCard"
        >
        </movie-card>
      </div>
    </article>
  </div>
</template>

<script>
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'


export default {
  name:'Home',
  components: {
    MovieCard
  },
  created: function(){
    this.$store.dispatch('LoadMovieCards')
  },
  // created: mapActions(['LoadMovieCards']),
  computed: {
    ...mapState(['movieCards'])
  }

  
}
</script>

<style>
body{
  padding-top : 140px;
}
</style>