<template>
  <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="navbar-brand nav-link mx-2 text-end">
          <router-link :to="{ name: 'Home'}">Home</router-link>
        </li>
        <li class="navbar-brand ms-md-auto nav-link mx-2 text-end">
          <router-link :to="{ name: 'Random'}">Random</router-link>
        </li>
        <li class="navbar-brand ms-md-auto nav-link mx-2 text-end">
          <router-link :to="{ name: 'MyMovieList'}">MyMovieList</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',

}
</script>

<style>

</style>