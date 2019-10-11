<template>
  <div id="app">
    <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
  <el-menu-item index="1"><router-link to="/">HOME</router-link></el-menu-item>
  <el-menu-item index="2"><router-link to="/about">About</router-link></el-menu-item>
  <el-submenu index="2">
    <template slot="title">EN</template>
    <el-menu-item index="2-1">简体中文</el-menu-item>
    <el-menu-item index="2-2">Français</el-menu-item>
    <el-menu-item index="2-3">Español</el-menu-item>
    <el-menu-item index="2-4">日本語</el-menu-item>
    <el-menu-item index="2-5">한국어</el-menu-item>
  </el-submenu>
   <el-submenu index="3">
    <template slot="title">EUR</template>
    <el-menu-item index="3-1">CNY</el-menu-item>
    <el-menu-item index="3-2">USD</el-menu-item>
    <el-menu-item index="3-3">CAD</el-menu-item>
    <el-menu-item index="3-4">GBP</el-menu-item>
    <el-menu-item index="3-5">HKD</el-menu-item>
  </el-submenu>
</el-menu>
<div class="line"></div>
    </el-header>
    <router-view/>
  </div>
</template>

<script>
import HomePage from './views/HomePage.vue'

export default {
  name: 'app',
  components: {
    HomePage
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
