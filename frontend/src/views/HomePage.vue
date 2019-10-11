<template>
<div >
<FTD />
</div>
</template>

<script>
import FTD from './components/FromToDes.vue'

export default {
  name: 'HomePage',
  components: {
    FTD
  },
  props: {
    msg: String
  }
}
</script>


<style scoped>

#search {

  margin-top: 60px;
}
.from {
  padding-left: 100em;
}
</style>