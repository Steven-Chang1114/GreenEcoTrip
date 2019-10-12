<template>
<div>
<div id = "base">
 <el-row class="demo-autocomplete" :gutter="7">
  <el-col :span="7" :offset="1">
    <p><b> From</b><i class="el-icon-map-location"></i></p>
    <el-autocomplete
      class="inline-input"
      v-model="state1"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>

  <el-col :span="7" >
    <p><b>To</b><i class="el-icon-place"></i></p>
    <el-autocomplete
      class="inline-input"
      v-model="state2"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>
  <el-col :span="6">
    <Date id = "date"/>
  </el-col>
</el-row>
<el-button v-on:click="makeOrder" type="success" id = "submit" plain><router-link to="/about"><h3>Let's start the trip!<i class="el-icon-magic-stick"></i></h3></router-link></el-button>
</div>
</div>
</template>
<script>
import Date from './Date.vue'
export default {
    components:{
      Date,
    },
    name: "FTD",
    data() {
      return {
        links: [],
        state1: '',
        state2: '',
      };
    },
    methods: {
      makeOrder(){
        date1 = value1;
      },
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
  color:aliceblue;
  padding-top: 5px;
  margin-left: 100px;
}

.inline-input {
  display: inline;
}

#base{
  background-color: rgba(0,0,0,0.4);
  object-fit: cover;
  border-radius: 10px;
  height: 230px;
  width: 1200px;
  margin-left: 130px;
  margin-top: 65px;
}
#submit{
margin-left: 500px;
margin-top: 25px;

}


</style>