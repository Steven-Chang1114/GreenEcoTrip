<template>
 <el-row class="demo-autocomplete">
  <el-col :span="4" class = "auto" >
    <p><b>From</b><i class="el-icon-map-location"></i></p>
    <el-autocomplete
      class="inline-input"
      v-model="state1"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>

  <el-col :span="4" class = "aut">
    <p><b>To</b><i class="el-icon-place"></i></p>
    <el-autocomplete
      id = "a"
      class="inline-input"
      v-model="state2"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>
  <el-col :span="600" class = "aut">
    <Date id = "date"/>
  </el-col>
</el-row>
</template>
<script>
import Date from './Date.vue'

export default {
    components:{
      Date
    },
    name: "FTD",
    data() {
      return {
        links: [],
        state1: '',
        state2: ''
      };
    },
    methods: {
      querySearch(queryString, cb) {
        var links = this.links;
        var results = queryString ? links.filter(this.createFilter(queryString)) : links;
        // call callback function to return suggestions
        cb(results);
      },
      createFilter(queryString) {
        return (link) => {
          return (link.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0);
        };
      },
      loadAll() {
        return [
          { "value": "Shanghai"},
          { "value": "Beijing"},
          { "value": "Hongkong"},
          { "value": "London"},
          { "value": "Edinburgh"},
          { "value": "Manchester"},
          { "value": "Barcelona"},
          { "value": "Valencia"},
          { "value": "Paris"},
          { "value": "Glascow"},
          { "value": "Madrid"}
         ];
      },
      handleSelect(item) {
        console.log(item);
      }
    },
    mounted() {
      this.links = this.loadAll();
    }
  }
</script>

<style>
.demo-autocomplete{
  margin-top: 50px;
  margin-left: 300px;
}
#date{
  margin-top: 15px;
}


</style>