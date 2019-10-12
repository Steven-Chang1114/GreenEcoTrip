<template>
<div>
  {{this.$store.state.departureLocation}}
  {{this.$store.state.destination}}
  <Date />
</div>
</template>

<script>
import Date from './components/Date'

  export default {
    name: "Result",
    components: {
      Date
    }
  };
</script>