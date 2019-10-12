<template>
<div>
    <p><b>Departure</b><i class="el-icon-date"></i><span id="arrive"><b>Arrive</b><i class="el-icon-place"></i></span></p>
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
    name: "Date",
    data() {
      return {
        pickerOptions: {
 
        },
        date: '',
      };
    }
  };
</script>

<style>
#arrive{
    margin-left: 122px;
}
</style>