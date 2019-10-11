<template>
 <el-row class="demo-autocomplete">
  <el-col :span="12">
    <p><b>From</b></p>
    <el-autocomplete
      class="inline-input"
      v-model="state1"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>

  <el-col :span="12">
    <p><b>To</b></p>
    <el-autocomplete
      id = "1"
      class="inline-input"
      v-model="state2"
      :fetch-suggestions="querySearch"
      placeholder="City"
      :trigger-on-focus="false"
      @select="handleSelect"
    ></el-autocomplete>
  </el-col>
</el-row>
</template>
<script>

export default {
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
  margin-top: 30px;
}
#id{
  margin-right: 60000px;
}
</style>