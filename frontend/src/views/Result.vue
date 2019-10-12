<template>
<div>
  <el-container style="height: 760px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
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
    <el-main>
    <el-card class="box-card" width="100%" v-for="trip in trips" :key="trip.id">
      <div slot="header" class="clearfix">
        <span>Carbon emission: {{trip.carbon}} kL</span><span style = "margin-left:70px;">Price: {{trip.price}} $</span>
        <el-button style="float: right; padding: 3px 0" type="text">Book</el-button>
      </div>
      <el-steps :space="200" :active="1" simple >
        <fragment v-for="(step, index) in trip.steps" :key="step.id">
          <el-step v-if="index==0" :title="step.start">
            <font-awesome-icon :icon="getIcon(step.type)" slot="icon"/>
          </el-step>
          <el-step :title="step.end" simple>
            <font-awesome-icon :icon="getIcon(step.type)" slot="icon"/>
          </el-step>
        </fragment>
      </el-steps>
    </el-card>
    
  </el-main>
  <Banner />
  </el-container>
</el-container>

</div>
</template>

<script>
import Date from './components/Date'
import F from './components/F'
import Banner from './components/Banner'

  export default {
    name: "Result",
    components: {
      Date,
      F,
      Banner
    },
    methods: {
      getIcon(type) {
        switch (type) {
          case 'flight':
            return 'plane'
          case 'bus':
            return 'bus'
          case 'rail':
            return 'subway'
          default:
            break;
        }
      }
    },
    data() {
      return {
        trips: [
        {
          id: 0,
          carbon: 69,
          price: 420,
          steps: [
          {id: 0, start: "Barcelona", end: "London", type: "flight"},
          {id: 1, start: "London", end: "Edinburgh", type: "rail"}
        ]},
        {
          id: 1,
          carbon: 9,
          price: 4567890,
          steps: [
          {id: 0, start: "Barcelona", end: "Valencia", type: "flight"},
          {id: 1, start: "Valencia", end: "London", type: "rail"}
        ]},
        {
          id: 1,
          carbon: 4353,
          price: 1,
          steps: [
          {id: 0, start: "Madrid", end: "Valencia", type: "bus"},
          {id: 1, start: "Valencia", end: "Barcelona", type: "flight"},
          {id: 2, start: "Barcelona", end: "London", type: "rail"},
          {id: 3, start: "London", end: "KL", type: "rail"}
        ]},
        ]
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

  #departure{
    padding-right: 500px;
  }

  #line{
    padding-right: 20px;
    padding-bottom: 20px;
  }

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .box-card{
    padding-left: 50px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    margin-left:50px;
    margin-right:50px;
    margin-top: 30px;
  }
</style>