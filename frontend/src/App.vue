<template>
  <div id="app">
    <navbar></navbar>
    <div id="contentContainer"><router-view/></div>
  </div>
</template>

<script>
import navbar from './components/core/Navbar.vue'

export default {
  name: 'app',
  components: { navbar }
}
</script>

<style>
@font-face {
  font-family: PublicSansRegular;
  src: url(./assets/fonts/public-sans/PublicSans-Regular.woff2)
}

@font-face {
  font-family: PublicSansBlack;
  src: url(./assets/fonts/public-sans/PublicSans-Black.woff2)
}

html{
  width: 100%;
  height: 100%;
  margin: 0;
  padding: 0;

  font-family: 'PublicSansRegular';
}

#contentContainer{
  position: fixed;
  top: 8%;
  height: 92%;
  width: 100%;

  background-color: #F2F2F0;
}
</style>
