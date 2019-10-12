<template>
<div>
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
    },
    data() {
      return {
        pickerOptions: {
 
        },
        date: Date.date,
      };
    }
  };
</script>