<template>
  <div>
    <my-list-form></my-list-form>
    <div>
      <my-list></my-list>
      <my-list-item></my-list-item>
    </div>
  </div>
</template>

<script>
import MyListForm from '@/components/MyListForm.vue'
import MyList from '@/components/MyList.vue'
import MyListItem from '@/components/MyListItem.vue'

export default {
  name:'MyMovieList',
  components: {
    MyListForm, MyListItem, MyList
  },
}
</script>

<style>

</style>