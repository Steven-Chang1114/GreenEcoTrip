<template>
<div id = "background">
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


<style>
#background{
  background-image: url("../assets/vacation.jpg");
  padding-bottom: 800px;
  max-width: 200%;
  object-fit: cover;
  height: 3px;
}
</style>