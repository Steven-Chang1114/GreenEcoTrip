<template>
  <div class="binding" v-title data-title="绑定账号">
    <div class="bindingbtn">
      <input type="text" v-model="city"/>
    </div>
    <div v-show="isshow">
      <p v-for="item in selectCitys" :key = "item">{{item}}</p>
    </div>
  </div>
</template>
<script>

export default {
  data () {
    return {
      isshow:true,
      city:"",
      citys:['Shanghai','London','Edinburgh','Barcelona','Beijing','Tokyo','New York','Manchester','Valencia','Madrid','Paris'],
      selectCitys:[]
    }
  },
  name: 'FTD',
  methods:{
    
  },
  watch:{
    city:function(val, oldVal){
      if(val.length==0){
         this.isshow = false
       }else{
          this.isshow = true;
          var citys = []
          this.citys.forEach((item,index) => {
              if(item.indexOf(val)>=0){
                  citys.unshift(item)
              }
          })  
          this.selectCitys = citys;
       }
    }
  }
}
</script>