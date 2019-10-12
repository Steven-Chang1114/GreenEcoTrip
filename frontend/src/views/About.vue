<template>
<div>
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
import Date from './components/Date.vue'

  export default {
    components: {
      date: Date.date,
    },
    name: "date",
    data() {
      return {
        pickerOptions: {
 
        },
      };
    }
  };
</script>