<template>
  <div class="d-flex justify-content-center align-items-center flex-column bg-info p-3 rounded-3">
    <h2>My Movie List</h2>
    <input 
      type="text"
      v-model.trim="movieTitle"
      @keyup.enter="createMovie"
    >
    <button @click="createMovie">Add</button>
  </div>
</template>

<script>
export default {
  name: 'MyListForm',
  data: function(){
    return {
      movieTitle: null,
    }
  },
  methods: {
    createMovie: function(){
      const todoMovie = {
        title: this.movieTitle
      }
      if (todoMovie.title) {
        this.$store.dispatch('createMovie', todoMovie)
      }
      this.movieTitle = null
    },
  },
}
</script>

<style>

</style>