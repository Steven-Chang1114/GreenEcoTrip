<template>
  <div class="about">
    <h1>{{date1}}</h1>
  </div>
</template>

<script>
import Date from './components/Date.vue'

export default {
  data: function () {
   return {
    name: 'About'
   }
  },
 components: {
  date1: Date.value1
 }
}
</script>>
