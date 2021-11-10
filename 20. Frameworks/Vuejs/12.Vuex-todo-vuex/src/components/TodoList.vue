<template>
  <div class="todo-list">
    TodoList
    <todo-list-item></todo-list-item>
    <todo-list-item></todo-list-item>
    <todo-list-item></todo-list-item>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'

export default {
  components: { TodoListItem },
  name: 'TodoList'

}
</script>

<style scoped>
  .todo-list {
    border: red solid 2px;
  }
</style>