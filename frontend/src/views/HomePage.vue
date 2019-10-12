<template>
<div id="background">
<Welcome />
<FTD />
</div>
</template>

<script>
import FTD from './components/FromToDes.vue'
import Welcome from './components/Welcome.vue'

export default {
  name: 'HomePage',
  components: {
    FTD,
    Welcome
  },
  props: {
    msg: String
  }
}
</script>


<style scoped>
#background{
  background-image: url("../assets/vacation.jpg");
  height: 100%;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}
</style>