<template>
<div>
  <p v-if="showTop">
    <b>Departure</b><i class="el-icon-date"></i>
    <span id="return"><b>Return</b><i class="el-icon-place"></i></span>
  </p>
  <div class="block">
    <el-date-picker
      v-model="date"
      type="daterange"
      range-separator="To"
      start-placeholder="Start date"
      end-placeholder="End date">
    </el-date-picker>
  </div>
  
  </div>
</template>

<script>
  export default {
    name: "Date",
<<<<<<< Updated upstream
    props: {
      showTop: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      date: {
        get () {
          return this.$store.state.tripInterval
        },
        set (val) {
          this.$store.commit('updateTripInterval', val)
        }
      }
    },
=======
    computed: {
    date: {
      get () {
        return this.$store.state.tripInterval
      },
      set (val) {
        this.$store.commit('updateTripInterval', val)
      }
    }
    }
>>>>>>> Stashed changes
  };
</script>

<style>
#return{
    margin-left: 122px;
}
</style>