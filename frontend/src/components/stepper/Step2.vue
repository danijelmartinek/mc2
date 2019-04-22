<template>
  <div id="sliderTwo" class="gridSelectContainer" v-touch:swipe.right="slideMinus">
    <div class="drow">
      <div class="dcol s-12 m-6 gridSelect">
        <p>
			<fit-text>Ne znam koji fakultet upisati niti kojim zanimanjem se želim baviti</fit-text>
        </p>
      </div>
      <div class="dcol s-12 m-6 gridSelect">
        <p>
			<fit-text>Znam koji fakultet upisati ali ne i kojim zanimanjem se želim baviti</fit-text>
        </p>
      </div>
      <div class="dcol s-12 m-6 gridSelect">
        <p>
			<fit-text>Ne znam koji fakultet upisati ali znam kojim zanimanjem se želim baviti</fit-text>
        </p>
      </div>
      <div class="dcol s-12 m-6 gridSelect">
        <p>
			<fit-text>Znam koji fakultet upisati i kojim zanimanjem se želim baviti</fit-text>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import fitText from './../../assets/scripts/fitText/fitText.vue';

export default {
  name: 'step2',
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
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.gridSelectContainer{
  width: 95%;
  margin: 0 auto;
  overflow: scroll;
}

.gridSelect{
	border: 2px solid blue;
	padding: 0em 1em 0em 1em;
	text-align: center;
	font-family: 'Ubuntu', sans-serif;
	font-weight: bold;
	text-transform: uppercase;
	line-height: 1em;
}

.gridSelect > p{
  border: 2px solid blue;
  padding: 1em;
  font-size: 2em;
  border-radius: 1em;
}

@media only screen and (min-width: 320px) {
  .gridSelectContainer{
    width: 90%;
  }
}

@media only screen and (min-width: 710px) {
  .gridSelectContainer{
    width: 80%;
  }
}

@media only screen and (min-width: 1070px) {
  .gridSelectContainer{
    width: 60%;
  }
}

@media only screen and (min-width: 1610px) {
  .gridSelectContainer{
    width: 40%;
  }
}
</style>
