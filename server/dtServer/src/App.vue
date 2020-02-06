<template>
  <div id="app">
  <navBar></navBar>
  <router-view></router-view>
  <footerBar></footerBar>
  </div>
</template>

<script>
import navBar from '@/components/nav'
import footerBar from '@/components/footer'
export default {
  name: 'App',
  components:{navBar,footerBar},
}
</script>

<style>
*{
  margin: 0px;
  padding: 0px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  overflow: hidden;
}


</style>
