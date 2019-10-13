<template>
<el-dialog title="Shipping address" :visible.sync="dialogTableVisible">
  <div class="gallery">
    <div class="gallery-image">
      <img src="../../assets/greenhills.jpg" width="800" height="600" />
      <div class="gallery-text">
        <h3>{{popup(emission, max)}}</h3>
      </div>
    </div>
  </div>
</el-dialog>
</template>

<script>
export default {
  name: "GreenTips",
  props: ['emission', 'max'],
  methods: {
    popup(emission, max) {
      co2Data = {
          'lamb': 39.2,
          'beef': 27.0,
          'cheese': 13.5,
          'mile': 2.25,
          'new clothes': 25,
      }
      
      var keys = Object.keys(co2Data);
      var key = keys[Math.floor(keys.length * Math.random())];
      var value = Math.round(emission / co2Data[key]);
        if (emission < 0.2*max) return "We're glad we could help you find the best and greenest way to get to your destination!" +
                                  " We hope you'll visit Trave4Future soon."
      switch (key) {
          case 'lamb':
            return 'Were thinking of having lamb curry tonight? This trip will produce as much CO2 as eating ' + value +' kg of lamb,' +
                        ' so how about switching to lentils for a while?';
              break;
          case 'beef':
              return "This trip will produce as much CO2 as " + value +" kg of beef. That's so many McRibs... maybe next time, or a quinoa burger instead!.";
              break;
          case 'cheese':
              return "This trip will produce as much CO2 as " + value +" kg of cheese. That's enough to make Stuart Little lactose intolerant."
              + ' Try some vegain dairy products!';
              break;
          case 'mile':
              return "This trip produces the equivalent amount of CO2 as driving for " + value + " miles. Maybe commute to work next week!";
              break;
          case 'new clothes':
              return "I know going shopping can be tempting, but by choosing this trip you'd actually produce the " +
                  "same amount of CO2 as buying " + value + " kg of new clothes";
              break;

      }
    }
  }
};
</script>

<style>
</style>