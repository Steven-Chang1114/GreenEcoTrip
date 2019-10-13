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

      <el-card class="box-card" width="100%" v-for="trip in trips" :key="trip.id">
        <div slot="header" class="clearfix">
          <span>Carbon emission: {{(trip.emission).toFixed(0)}} kg</span><span style = "margin-left:70px;" v-if="trip.price">Price: {{trip.price}} $</span>
          <el-button style="float: right; padding: 3px 0" type="text">Book</el-button>
        </div>

        <el-steps :space="200" :active="1" simple >
          <fragment v-for="(step, index) in trip.steps" :key="step.id">
            <el-step v-if="index==0" :title="step.origin.name">
              <font-awesome-icon :icon="getIcon(step.type)" slot="icon"/>
            </el-step>
            <el-step :title="step.destination.name || step.destination.Name" simple>
              <font-awesome-icon :icon="getIcon(step.type)" slot="icon"/>
            </el-step>
          </fragment>
        </el-steps>
        
      </el-card>

    </el-main>
    <Banner />
  </el-container>
</el-container>
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
      },
      parseFlights(flights) {
        let f = []
        for (const flightIdx in flights) {
          const flight = flights[flightIdx];
          let steps = []
          for (const stepIdx in flight.OutboundLegId.SegmentIds) {
            const segment = flight.OutboundLegId.SegmentIds[stepIdx]
            if (segment.Id === undefined) {
              continue
            }
            steps.push({
              id: segment.Id,
              origin: segment.OriginStation,
              destination: segment.DestinationStation,
              type: 'flight',
              departure: segment.Departure,
              arrival: segment.Arrival,
            })
          }
          f.push({
            steps,
            emission: flight.Emissions
          })
        }
        return f
      },
      parseTrains(trains, k) {
        let t = []
        for (const tripIdx in trains) {
          const details = trains[tripIdx].Details
          let steps = [{
            id: k + tripIdx,
            origin: details[0].transit_detail.departure_stop,
            destination: details[details.length - 1].transit_detail.arrival_stop,
            departure: details[0].transit_detail.departure_time.text,
            arrival: details[0].transit_detail.arrival_time.text,
            type: 'rail'
          }]
          t.push({
            steps,
            emission: trains[tripIdx].Emissions
          })
        }
        return t
      }
    },
    computed: {
      trips() {
        const trips = this.$store.state.trips
        const flights = this.parseFlights(trips.Planes)
        const trains = this.parseTrains(trips.Trains)
        return trains.concat(flights)
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