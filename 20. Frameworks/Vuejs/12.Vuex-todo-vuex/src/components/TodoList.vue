<template>
  <div class="todo-list">
    Todo List
    <ul>
      <todo-list-item 
      v-for="todo in todos" 
      :key="todo.id"
      :todo="todo"
      ></todo-list-item>
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem.vue'
import { mapState } from 'vuex'

export default {

  name: 'TodoList',
  components: { TodoListItem },
  computed: {
    ...mapState([
      'todos',
    ])
  }

}
</script>

<style scoped>
  .todo-list {
    border: red solid 2px;
  }
</style>