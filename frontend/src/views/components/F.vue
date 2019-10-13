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

  <el-divider></el-divider>
  <p style = "margin-left: 15px;">Carbon Emission</p>
  <el-progress style = "margin-left:30px; margin-right: 20px" type="dashboard" :percentage="percentage" :color="colors"></el-progress>
<div>
  <el-button-group style = "margin-left:40px; margin-right: 20px">
    <el-button icon="el-icon-minus" @click="decrease"></el-button>
    <el-button icon="el-icon-plus" @click="increase"></el-button>
  </el-button-group>
  <el-divider></el-divider><br>
</div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        percentage: 10,
        colors: [
          {color: '#f56c6c', percentage: 20},
          {color: '#e6a23c', percentage: 40},
          {color: '#5cb87a', percentage: 60},
          {color: '#1989fa', percentage: 80},
          {color: '#6f7ad3', percentage: 100}
        ],
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
      };
    },
    methods: {
      increase() {
        this.percentage += 10;
        if (this.percentage > 100) {
          this.percentage = 100;
        }
      },
      decrease() {
        this.percentage -= 10;
        if (this.percentage < 0) {
          this.percentage = 0;
        }
      }
    }
  }
</script>

<style scoped>

</style>