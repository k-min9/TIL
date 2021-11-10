<template>
  <li class="todo-list-item">
    <input type="checkbox" v-model="newTodo.completed" @click="onSave(newTodo)">
    <span v-if="isEditing">
      <input type="text" v-model="newTodo.title">
      <button @click="onSave">[save]</button>
    </span>
    <span v-else>
      {{ todo.title }}
      <button @click="onClick">[edit]</button>
    </span>
  </li>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'TodoListItem',
  data() {
    return {
      // 자바스크립트 deepcopy
      newTodo: {...this.todo },
      isEditing: false
    }
  },
  props: {
    todo : Object
  },
  method: {
    ...mapActions(['updateTodo']),
    onClick() {
      this.isEditing = !this.isEditing
    },
    onSave() {
      this.updateTodo(this.newTodo)
      this.isEditing = !this.isEditing      
    }
  },
}
</script>

<style scoped>
  .todo-list-item {
    border: blue solid 2px;
  }
</style>