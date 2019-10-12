<template>
<div style="padding-left: 100px; padding-right: 100px">
  <div id="base">
  <el-row class="demo-autocomplete" :gutter="7">
    <el-col :span="9" style = "margin-left: 22px;">
      <p style = "margin-bottom: 1px; margin-top:5px;"><b> From</b><i class="el-icon-map-location"></i></p>
      <el-autocomplete
        class="inline-input"
        v-model="departLoc"
        :fetch-suggestions="querySearch"
        placeholder="City"
        :trigger-on-focus="false"
        @select="handleSelect"
      ></el-autocomplete>
    </el-col>

    <el-col :span="9" >
      <p style = "margin-bottom: 1px; margin-top:5px;"><b>To</b><i class="el-icon-place"></i></p>
      <el-autocomplete
        class="inline-input"
        v-model="destination"
        :fetch-suggestions="querySearch"
        placeholder="City"
        :trigger-on-focus="false"
        @select="handleSelect"
      ></el-autocomplete>
    </el-col>
    <el-col :span="4">
      <Date id = "date" showTop inline/>
    </el-col>
  </el-row>
  <center >
  <router-link to="/result"><el-button v-on:click="makeOrder" type="success" id = "submit" plain><h3>Let's start the trip!<i class="el-icon-magic-stick"></i></h3></el-button></router-link>
  </center>
  </div>
</div>
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
  },
  mounted() {
    this.links = this.loadAll();
  },
  computed: {
    departLoc: {
      get () {
        return this.$store.state.departureLocation
      },
      set (val) {
        this.$store.commit('updateDeparture', val)
      }
    },
    destination: {
      get () {
        return this.$store.state.destination
      },
      set (val) {
        this.$store.commit('updateDestination', val)
      }
    }
  }
}
</script>

<style>
.demo-autocomplete{
  color:aliceblue;
  padding-top: 5px;
  margin-left: 10px;
  margin-top: 50px;
}

.inline-input {
  display: inline;
}

#base{
  background-color: rgba(0,0,0,0.4);
  object-fit: cover;
  border-radius: 10px;
  height: 200px;
  width:1100px;
  margin-top: 60px;
}
#submit{
margin-top: 25px;
}


</style>