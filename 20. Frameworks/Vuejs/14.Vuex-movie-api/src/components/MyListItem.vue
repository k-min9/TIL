<template>
  <table class="table table-striped">
    <tr>
      {{ todoMovie.title }}
    </tr>
  </table>
</template>

<script>
export default {
  name: 'MyListItem',
  props: {
    todoMovie: {
      type: Object,
    }
  }
}
</script>

<style>

</style>