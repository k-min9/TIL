<template>
  <nav class="ui secondary pointing menu">
    <router-link to="/" class="active item">
      Image Storage
    </router-link>
    <ul class="right menu">
      <div v-if="isLoggedIn" class="horizontal">  <!-- getters에 있는 isLoggedIn 필요, horizontal은 simentic ui 문법 -->
        <router-link :to="{ name: 'Home' }" class="item">Gallery</router-link>
        <router-link :to="{ name: 'Upload' }" class="item">Upload</router-link>
        <a @click="logout" class="item">Logout</a>
      </div>
      <div v-else>
        <a @click="login" class="ui item">Login</a>
      </div>
    </ul>
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