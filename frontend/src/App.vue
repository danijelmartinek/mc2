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
@font-face {
  font-family: PublicSansRegular;
  src: url(./assets/fonts/public-sans/PublicSans-Regular.woff2)
}

html{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;

  font-family: 'PublicSansRegular';
}

#navbar{
  z-index: 999;
  position: fixed;
  height: 8%;
  width: 100%;
  background-color: #F2F2F0;
  box-shadow: 0px 5px 30px 5px rgba(0, 0, 0, 0.1);
}

#contentContainer{
  position: fixed;
  top: 8%;
  height: 92%;
  width: 100%;

  background-color: #F2F2F0;
}
</style>
