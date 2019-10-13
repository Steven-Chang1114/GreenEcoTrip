<template>
  <el-card class="box-card" width="100%" @click.native="dialogVisible=true">
    <GreenTips :dialogTableVisible="dialogVisible" :emission="emission" :max="max"/>
    <el-row :gutter="50">
      <el-col :span="8">
        <h2>Depart: {{depart}}</h2>
      </el-col>
      <el-col :span="8" :offset="8" style="text-align: right">
        <h2>Arrive: {{arrive}}</h2>
      </el-col>
    </el-row>
    <div slot="header" class="clearfix">
      <span>
        <center>
          <strong><h3>Carbon emission: {{(emission).toFixed(0)}} kg</h3></strong>
          <el-progress
            :width="64"
            type="circle"
            :percentage="emissionPercentage"
            :show-text="false"
            :colors="colors"
            ></el-progress>
        </center>
      </span>
      <img :src="image" style="float: right; margin-right: 50px" v-if="image" height="100%"/>
      <span style = "margin-left:70px;" v-if="price">Price: {{price}} $</span>
    </div>
    <el-steps :space="200" :active="1" simple >
      <fragment v-for="(step, index) in steps" :key="index">
        <el-step v-if="index==0" :title="stepOrigin(step)">
          <font-awesome-icon :icon="getIcon(stepType(step))" slot="icon"/>
        </el-step>
        <el-step :title="stepArrival(step)" simple>
          <font-awesome-icon :icon="getIcon(stepType(step))" slot="icon"/>
        </el-step>
      </fragment>
    </el-steps>
  </el-card>
</template>

<script>
import GreenTips from './GreenTips'

export default {
  name: "TravelCard",
  props: ['trip'],
  components: {
    GreenTips
  },
  data() {
    return {
      dialogVisible: false,
      colors: [
        {color: '#f56c6c', percentage: 20},
        {color: '#e6a23c', percentage: 40},
        {color: '#5cb87a', percentage: 60},
        {color: '#1989fa', percentage: 80},
        {color: '#6f7ad3', percentage: 100}
      ],
    }
  },
  computed: {
    emissionPercentage() {
      return this.emission * 100 / this.$store.state.trips.max
    },
    depart() {
      if (this.type === 'Flight') {
        const t = new Date(this.trip.OutboundLegId.Departure)
        const options = {
          hour12 : true,
          hour:  "2-digit",
          minute: "2-digit",
          timeZoneName: 'short'
        }
        return t.toLocaleTimeString("en-UK", options)
      } else {
        return this.steps[0].transit_detail.departure_time.text + ' ' + this.steps[0].transit_detail.departure_time.time_zone
      }
    },
    arrive() {
      if (this.type === 'Flight') {
        const t = new Date(this.trip.OutboundLegId.Arrival)
        const options = {
          hour12 : true,
          hour:  "2-digit",
          minute: "2-digit",
          timeZoneName: 'short'
        }
        return t.toLocaleTimeString("en-UK", options)
      } else {
        return this.steps[0].transit_detail.arrival_time.text + ' ' + this.steps[0].transit_detail.departure_time.time_zone
      }
    },
    image() {
      if (this.type === 'Flight') {
        return this.trip.OutboundLegId.Carriers[0].ImageUrl
      }
      return null
    },
    type() {
      return this.trip.Type
    },
    emission() {
      return this.trip.Emissions
    },
    pricingOptions () {
      if (this.type !== 'Flight') { return null }
      return this.trip.PricingOptions
    },
    steps () {
      if (this.type === 'Flight') {
          const length = this.trip.OutboundLegId.SegmentIds.length
          if (length > 1) {
            return this.trip.OutboundLegId.SegmentIds.slice(0, length-1)
          } else {
            return this.trip.OutboundLegId.SegmentIds
          }
      } else {
        return this.trip.Details
      }
    }
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
    stepArrival(step) {
      if (this.type === 'Flight') {
        return step.DestinationStation.Name
      } else {
        return step.transit_detail.arrival_stop.name
      }
    },
    stepOrigin(step) {
      if (this.type === 'Flight') {
        return step.OriginStation.Name
      } else {
        return step.transit_detail.departure_stop.name
      }
    },
    stepType() {
      if (this.type === 'Flight') {
        return 'flight'
      } else if (this.type === 'Transit') {
        return 'rail'
      }
    }
  },
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