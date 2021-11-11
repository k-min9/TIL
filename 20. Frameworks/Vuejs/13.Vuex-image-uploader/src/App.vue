<template>
  <div>
    <nav-bar></nav-bar>
    App!
    <router-view></router-view>
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