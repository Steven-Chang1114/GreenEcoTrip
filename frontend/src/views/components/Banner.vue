<template>
<div>
  <template>
  <el-carousel height="120px" direction="vertical" :autoplay="false" >
    <el-carousel-item v-for="item in items" :key="item">
      <div class="container" >
        <img :src="item.img" />
        <div class="text-block">
        <p><b>{{item.txt}}</b></p>
        </div>
      </div>
    </el-carousel-item>
  </el-carousel>
</template>
</div>
</template>

<script>
import image from '../../assets/rainforest.jpg'
import image2 from '../../assets/rainforest2.jpg'
import image3 from '../../assets/rainforest3.jpg'
import image4 from '../../assets/rainforest4.jpg'
import image5 from '../../assets/rainforest5.jpeg'
import image6 from '../../assets/rainforest6.jpg'

export default {
  name: 'Banner',
  data() {
    return {
      items: [{
          img: image,
          txt: "It’s time to get your car checked up! If your engine is working efficiently and your tires are well inflated, your car will consume the least fuel, and you won’t crash on a traffic light!"
      },{
        img: image2,
        txt: "Ever feel like you should nurture your green thumb? Now it’s the time to do it! Growing a few plants in your garden will suck up the pollution in the air making your neighbourhood a much nicer place to live in!"
      },{
        img: image3,
        txt: "Everybody forgets something at home once in a while, but by planning ahead you’ll save time and the planet! Literally! The least times you hop on your vehicle the better!"
      },{
        img: image4,
        txt: "How annoying is that pile of junk mail on your drawer right? Try telling it to the millions of trees that have been cut down to make them. Get informed on how you can get rid of companies sending you spam!"
      },{
        img: image5,
        txt: "It’s one of those beautiful days outside but you have work today? Don’t be lazy and move your desk next to a big window, the planet will thank you for not turning on the lights. It’s good exercise too!"
      },{
        img: image6,
        txt: "Vintage is stylish again! Take advantage of this opportunity,  it’s cheap, trendy and sustainable! Go down the road to your local charity store and do some shopping!"
      }
      ],
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

  .container {
  position: relative;
}

/* Bottom right text */
.text-block {
  position: absolute;
  bottom:45em;
  text-align: center;
  color: white;
  font-size: 20px;
  padding-left: .5em;
  text-shadow: 1px 1px #000000;
}
</style>