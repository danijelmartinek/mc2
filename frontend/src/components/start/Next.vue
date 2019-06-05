<template>
  <div id="sliderTwo" class="gridSelectContainer" v-touch:swipe.right="slideMinus">
    <div class="drow">
      <!-- <div class="dcol s-12 m-6 gridSelect">
        <router-link tag="div" to="/case/4">
          <fit-text>Ne znam koji fakultet upisati niti kojim zanimanjem se želim baviti</fit-text>
        </router-link>
      </div> -->
      <div class="dcol s-12 m-6 gridSelect">
        <router-link tag="div" to="/case/3">
          <fit-text>Znam koji fakultet upisati ali ne i kojim zanimanjem se želim baviti</fit-text>
        </router-link>
      </div>
      <div class="dcol s-12 m-6 gridSelect">
        <router-link tag="div" to="/case/2">
          <fit-text>Ne znam koji fakultet upisati ali znam kojim zanimanjem se želim baviti</fit-text>
        </router-link>
      </div>
      <div class="dcol s-12 offset-m-3 m-6 gridSelect">
        <router-link tag="div" to="/case/1">
          <fit-text>Znam koji fakultet upisati i kojim zanimanjem se želim baviti</fit-text>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import fitText from './../../assets/scripts/fitText/fitText.vue';

export default {
  name: 'next',
  components: {
      fitText,
  },
  methods: {
      slideMinus() {
          this.$emit('stepSlideMinus')
      }
  }
}
</script>

<style scoped>
#sliderTwo > div{
  position: relative;
  top: 40%;
  left: 50%;
  
  -ms-transform: translate(-50%, -50%);
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -o-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
}

.gridSelectContainer{
  width: 95%;
  margin: 0 auto;
}

.gridSelect{
	padding: 0.2em 2em 0.2em 2em;
	text-align: center;
	font-weight: bold;
	text-transform: uppercase;
  font-size: 1em;
}

.gridSelect > div{
  background-color: #2C365D;
  background-image: url("./../../assets/img/papyrus.png");
  background-blend-mode: multiply;
  color: #F2F2F0;
  padding: 1em;
  border-radius: 1em;
  cursor: pointer;
  box-shadow: 0px 0px 20px 10px rgba(0, 0, 0, 0.2);

  -webkit-tap-highlight-color: transparent;
  webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, current supported by Chrome and Opera */
}

.gridSelect > div:active{
  background-color: rgb(63, 77, 135);
}

@media only screen and (min-width: 340px) {
  .gridSelectContainer{
    width: 90%;
  }

  .gridSelect{
    padding: 0.3em 1em 0.3em 1em;
    font-size: 1.5em;
  }
  
}

@media only screen and (min-width: 710px) {
  .gridSelectContainer{
    width: 80%;
  }

  .gridSelect{
    padding: 0.5em 0.5em 0.5em 0.5em;
    font-size: 1.7em;
  }

  .gridSelect > div{
    min-height: 150px;
  }
}

@media only screen and (min-width: 1070px) {
  .gridSelectContainer{
    width: 65%;
  }

  .gridSelect{
    padding: 0.5em 0.5em 0.5em 0.5em;
    font-size: 2em;
  }

  .gridSelect > div{
    min-height: 150px;
  }
}

@media only screen and (min-width: 1610px) {
  .gridSelectContainer{
    width: 50%;
  }

  .gridSelect{
    padding: 0.5em 0.5em 0.5em 0.5em;
    font-size: 2.1em;
  }

  .gridSelect > div{
    min-height: 160px;
  }
}
</style>
