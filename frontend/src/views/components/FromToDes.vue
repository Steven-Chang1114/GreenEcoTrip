<template>
<div style="padding-left: 100px; padding-right: 100px">
  <div id="base">
  <el-row class="demo-autocomplete" :gutter="40">
    <el-col :span="9">
      <p style = "font-size: 1.5em; margin-bottom: 5px; margin-top:5px;"><b> From</b><i class="el-icon-map-location"></i></p>
      <el-autocomplete
        size="large"
        class="inline-input"
        v-model="departLoc"
        :fetch-suggestions="querySearch"
        placeholder="City"
      ></el-autocomplete>
    </el-col>

    <el-col :span="9" >
      <p style = "font-size: 1.5em; margin-bottom: 5px; margin-top:5px;"><b>To</b><i class="el-icon-place"></i></p>
      <el-autocomplete
        size="large"
        class="inline-input"
        v-model="destination"
        :fetch-suggestions="querySearch"
        placeholder="City"
      ></el-autocomplete>
    </el-col>
    <el-col :span="4">
      <Date id = "date" showTop />
    </el-col>
  </el-row>
  <center >
  <el-button v-on:click="travelSearch" type="success" id = "submit" plain><h3>Let's start the trip!<i class="el-icon-magic-stick"></i></h3></el-button>
  </center>
  </div>
</div>
</template>

<script>
import Date from './Date.vue'

const lookup = {
  Shanghai: "",
  Beijing: "",
  Hongkong: "",
  London: "",
  Edinburgh: "EDI-sky",
  Manchester: "MAN-sky",
  Barcelona: "BCN-sky",
  Valencia: "",
  Paris: "CDG-sky",
  Glascow: "",
  Madrid: "MAD-sky",
}

export default {
  components:{
    Date
  },
  name: "FTD",
  data() {
    return {
      links: [
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
      ],
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
    travelSearch() {
      let date = this.$store.state.tripInterval
      let dstr = date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate()
      fetch('http://localhost:8000/home/results/', {method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          country: 'UK',
          currency: 'GBP',
          locale: 'en-UK',
          originPlace: lookup[this.departLoc],
          destinationPlace: lookup[this.destination],
          outboundDate: dstr,
          adults: 1
        })
      })
      .then(res => res.json())
      .then(data => this.$store.commit('updateTrips', data))
      this.$store.commit('updateTrips', {flights: [], trains: []})

      this.$router.push({path: '/result'})
    }
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
}

.inline-input {
  display: inline;
}

#base{
  background-color: rgba(0,0,0,0.4);
  border-radius: 10px;
  padding: 2rem;
}
#submit{
  margin-top: 2rem;
}

</style>