<template>
<div>
  {{this.$store.state.departureLocation}}
  {{this.$store.state.destination}}
<<<<<<< Updated upstream
  <Date />
</div>
=======
  {{this.$store.state.tripInterval}}
  <div class="block">
    <el-date-picker  
      v-model="date"
      type="daterange"
      range-separator="To"
      start-placeholder="Start date"
      end-placeholder="End date">
    </el-date-picker>
  </div>
  
  </div>
>>>>>>> Stashed changes
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