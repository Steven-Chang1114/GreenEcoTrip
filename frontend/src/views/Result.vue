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
    <el-card class="box-card" width="100%">
      <div slot="header" class="clearfix">
        <span>Trip</span>
        <el-button style="float: right; padding: 3px 0" type="text">Book</el-button>
      </div>
      <el-steps :space="200" :active="1" v-for="trip in trips" :key="trip.id" simple>
        <el-step v-for="step in trip.steps" :key="step.id" title="Step 1" icon="el-icon-s-promotion">{{step.start}}</el-step>

      </el-steps>
    </el-card>
    
  </el-main>
  </el-container>
</el-container>
</div>
</template>

<script>
import Date from './components/Date'
import F from './components/F'

  export default {
    name: "Result",
    components: {
      Date,
      F
    },
    data() {
      return {
        trips: [
        {
          id: 0,
          steps: [
          {id: 0, start: "Barcelona", end: "London", type: "flight"},
          {id: 1, start: "London", end: "Edinburgh", type: "rail"}
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