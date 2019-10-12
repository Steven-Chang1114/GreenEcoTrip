<template>
<div>
  <p v-if="showTop" style = "margin-bottom: 2px; margin-top:4px;">
    <b>Departure</b><i class="el-icon-date"></i>
  </p>
  <el-date-picker
    :style="inline ? 'display: inherit;':''"
    v-model="tripInterval"
    type="date"
    placeholder="Departure time">
  </el-date-picker>
  </div>
</template>

<script>
  export default {
    name: "Date",
    props: {
      showTop: {
        type: Boolean,
        default: false
      },
      inline: {
        type: Boolean,
        default: false
      }
    },
    computed: {
      tripInterval: {
        get () {
          return this.$store.state.tripInterval
        },
        set (val) {
          this.$store.commit('updateTripInterval', val)
        }
      }
    },
  };
</script>

<style>
#return{
    margin-left: 122px;
}
</style>