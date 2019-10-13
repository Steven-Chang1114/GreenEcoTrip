<template>
<el-container>
  <el-aside width="200px" style="background-color: rgb(238, 241, 246);">
    <el-menu :default-openeds="['1', '3']">
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>Filter</template>
      </el-submenu>
      <F />
    </el-menu>
  </el-aside>
  
  <el-container>
    <el-header style="text-align: right; font-size: 12px;">
      <el-row :gutter="10">
        <el-col :span="12">
          <h2 style="float: left; margin-top:0px; color:white">
            Select departure trip to {{this.$store.state.destination}}
          </h2>
        </el-col>
        <el-col :span="12">
          <Date/>
        </el-col>
      </el-row>
    </el-header>

    <el-main style="height: 580px;" v-loading="!trips.length">
      <TravelCard :trip="trip" v-for="trip in trips" :key="trip.id"/>
    </el-main>
    <Banner />
  </el-container>
</el-container>
</template>

<script>
import Date from './components/Date'
import F from './components/F'
import Banner from './components/Banner'
import TravelCard from './components/TravelCard'

export default {
  name: "Result",
  components: {
    Date,
    F,
    Banner,
    TravelCard
  },
  computed: {
    trips() {
      const trips = this.$store.state.trips
      return trips.Trains.concat(trips.Planes)
    }
  }
};
</script>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>