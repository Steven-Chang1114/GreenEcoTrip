<template>
<div>
    <p><b>Departure</b><i class="el-icon-date"></i><span id="arrive"><b>Arrive</b><i class="el-icon-place"></i></span></p>
  <div class="block">  
    <el-date-picker  
      v-model="value1"
      type="daterange"
      range-separator="To"
      start-placeholder="Start date"
      end-placeholder="End date">
    </el-date-picker>
    <h1>
        {{value1}}
    </h1>
  </div>
  </div>
</template>

<script>
  export default {
    name: "date",
    data() {
      return {
        pickerOptions: {
 
        },
        value1: '',
      };
    }
  };
</script>

<style>
#arrive{
    margin-left: 122px;
}
</style>