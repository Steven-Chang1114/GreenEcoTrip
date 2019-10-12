<template>
<div>
  <template>
  <el-carousel height="100px" direction="vertical" :autoplay="false">
    <el-carousel-item v-for="item in items" :key="item">
      <img :src="item" />
    </el-carousel-item>
  </el-carousel>
</template>
</div>
</template>

<script>
import image from '../../assets/rainforest.jpg'
import image2 from '../../assets/rainforest2.jpg'
import image3 from '../../assets/rainforest3.jpeg'

export default {
  name: 'Banner',
  data() {
    return {
      items: [image,image2,image3],
    };
  },
}
</script>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 100px;
    margin: 0;
  }
  
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>