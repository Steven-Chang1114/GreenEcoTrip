<template>
<div >
<FTD />
<Image />
</div>
</template>

<script>
import FTD from './components/FromToDes.vue'
import Date from './components/Date.vue'
import Image from './components/Image.vue'

export default {
  name: 'HomePage',
  components: {
    FTD,
    Date,
    Image
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