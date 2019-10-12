<template>
<div>
  <el-row :gutter="3" >
    <el-col :span="1">
      <Drawer />
    </el-col>
    <el-col :span="15">
       <F />
      <h2 id="info">From: {{this.$store.state.departureLocation}} to {{this.$store.state.destination}}</h2>
    </el-col>
    <el-col :span="1" >
        <Date id = "departure"/>
    </el-col>
  </el-row>
  <Timeline id = "time"/>
 
  <SwitchPage id = "page"/>
</div>
</template>

<script>
import Date from './components/Date'
import SwitchPage from './components/SwitchPage'
import Timeline from './components/Timeline'
import F from './components/F'

  export default {
    name: "Result",
    components: {
      Date,
      SwitchPage,
      Timeline,
      F
    }
  };
</script>

<style>
#info{
  text-align: left;
  padding-left: 500px;
}
#departure{
  margin-top: 16px;
  
}
#page{
  text-align: center;
  margin-top: 500px;
}
#time{
  padding-left: 560px;
  padding-top: 10px;
}
</style>