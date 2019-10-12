<template>
  <div id="app">
    <el-menu
    class="el-menu-demo"
    mode="horizontal"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
      <el-menu-item index="1" ><router-link to="/"><i class="el-icon-s-promotion"></i></router-link></el-menu-item>
      <el-menu-item index="2" disabled><i class="el-icon-info"></i></el-menu-item>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-s-comment"></i>
        </template>
        <el-menu-item index="2-1">简体中文</el-menu-item>
        <el-menu-item index="2-2">Français</el-menu-item>
        <el-menu-item index="2-3">Español</el-menu-item>
        <el-menu-item index="2-4">日本語</el-menu-item>
        <el-menu-item index="2-5">한국어</el-menu-item>
        <el-menu-item index="2-5">English</el-menu-item>
      </el-submenu>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-coin"></i></template>
        <el-menu-item index="3-1">CNY</el-menu-item>
        <el-menu-item index="3-2">USD</el-menu-item>
        <el-menu-item index="3-3">CAD</el-menu-item>
        <el-menu-item index="3-4">GBP</el-menu-item>
        <el-menu-item index="3-5">HKD</el-menu-item>
        <el-menu-item index="3-6">EUR</el-menu-item>
      </el-submenu>
      <el-menu-item style="position: absolute; right: 40vw">
        <span style="font-size: 2em;"><font-awesome-icon icon="leaf" slot="icon"/> Travel4Future</span>
      </el-menu-item>
    </el-menu>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  }
}
</script>

<style scope>
body {
  margin: 0px;
  height: 100vh;
}
#app {
  height: 100%;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
