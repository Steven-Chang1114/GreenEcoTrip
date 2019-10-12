<template>
<div>
  <div>
    <p style = "margin-left: 15px;">Sorted by</p>
    <el-select id = "sort" size = small v-model="value" placeholder="Select" style = "margin-left:15px; margin-right:20px;">
    <el-option
      v-for="item in options"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
  </div>
  <el-divider></el-divider>
  <div class="block">
    <p style = "margin-left: 15px;">The departure time</p>
     <el-slider
      v-model="time"
      range
      :marks="marks"
      :max = 24
      style = "margin-left:20px; margin-right: 20px"
      >
    </el-slider><br>
  </div>

    <el-divider></el-divider>

    <div class="block">
    <p style = "margin-left: 15px;">The price</p>
     <el-slider
      v-model="price"
      range
      :marks="mark"
      :max = 2000
      style = "margin-left:20px; margin-right: 20px"
      >
    </el-slider><br>
  </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        price: [400, 1000],
        mark: {
          0:'0$',
          1000: {
            style: {
              color: '#1989FA'
            },
            label: this.$createElement('strong', '1000$')
          },
          2000:'2000$'
        },
        time: [6, 18],
        marks: {
          0: '0am',
          6: '6am',
          12: {
            style: {
              color: '#1989FA'
            },
            label: this.$createElement('strong', 'noon')
          },
          18: '18pm',
          24:'24pm'
        },
        options: [{
          value: 'Greenest',
          label: 'Greenest'
        }, {
          value: 'Fastest',
          label: 'Fastest'
        }, {
          value: 'Cheapest',
          label: 'Cheapest'
        }],
        value: ''
      }
    }
  }
</script>

<style scoped>

</style>