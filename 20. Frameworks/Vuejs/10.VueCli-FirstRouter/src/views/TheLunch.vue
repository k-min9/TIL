<template>
  <div>
    <h1>Lunch</h1>
    <button @click="pickMenu">Change</button>
    <p>{{ menu }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  // 함수로 감싸지 않으면, 인스턴스가 같은 객체를 공유하기 때문에 data 내부는 무조건 함수로 해야한다.
  data() {
    return {
      menu: null,
      menus: ['빅맥', '와퍼', '징거', '싸이'],
    }
  },
  methods: {
    pickMenu() {
      this.menu = _.sample(this.menus)
    }
  },
  created() {
    this.pickMenu()
  }

}
</script>

<style>

</style>