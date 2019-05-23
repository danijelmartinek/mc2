<template>
  <div id="app">
    <div class="nav-bar"></div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
html{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;
}

.nav-bar{
  position: fixed;
  height: 8%;
  width: 100%;
  background-color: green;
}
</style>
