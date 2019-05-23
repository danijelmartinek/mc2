<template>
  <div id="app">
    <div id="navbar"></div>
    <div id="contentContainer"><router-view/></div>
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

#navbar{
  position: fixed;
  height: 8%;
  width: 100%;
  background-color: green;
}

#contentContainer{
  position: fixed;
  top: 8%;
  height: 92%;
  width: 100%;
}
</style>
