<template>
<div class="col-12 col-sm-6 d-flex justify-content-center">
  <div class = "card">
    <img :src="`https://image.tmdb.org/t/p/original/${ movieCard.poster_path }`" :alt="movieCard.title">
    <div class = "card-body">
      <p class="card-text"><strong>{{ movieCard.title }}</strong><br>{{ movieCard.overview }}</p>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object
  },
  data: function() {
    return {
      imgPath: '',
    }
  }
}
</script>

<style>

</style>