<template>
<div>
  {{this.$store.state.destination}}
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
</template>

<script>
  export default {
    name: "Result",
    data() {
      return {
        pickerOptions: {
 
        },
        date: Date.date,
      };
    }
  };
</script>