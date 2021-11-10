<template>
  <div>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  }
}
</script>

<style lang="scss">
/* static 하게 로드해보기 */
/* @import '~bootstrap/dist/css/bootstrap.css'; */ /* scss 없으면 */
@import 'bootstrap/scss/bootstrap' // scss 있으면


</style>