<template>
  <div>
    <my-list-item
      v-for="todoMovie in todoMovies"
      :key="todoMovie.id"
      :todoMovie="todoMovie"
    ></my-list-item>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import MyListItem from '@/components/MyListItem'

export default {
  name: 'MyList',
  components: {
    MyListItem,
  },
  computed: {
    ...mapState([
      'todoMovies',
    ])
  }
}
</script>

<style>

</style>