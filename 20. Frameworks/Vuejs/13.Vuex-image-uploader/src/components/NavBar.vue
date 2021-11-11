<template>
  <nav class="ui secondary pointing menu">
    <router-link to="/" class="active item">
      Image Storage
    </router-link>
    <div v-if="isLoggedIn" class="right menu">
      <router-link :to="{ name: 'Home' }" class="item">Gallery</router-link>
      <router-link :to="{ name: 'Upload' }" class="item">Upload</router-link>
      <a @click="logout" class="item">Logout</a>
    </div>
    <div v-else class="right menu">
        <a @click="login" class="ui item">Login</a>
    </div>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NavBar',
  computed: mapGetters(['isLoggedIn']),
  methods: mapActions(['login', 'logout']),
}
</script>

<style>

</style>