<template>
  <div>
    <nav-bar></nav-bar>
    <div class="ui container">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {NavBar,}
}
</script>

<style>

</style>