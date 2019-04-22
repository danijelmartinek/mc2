<template>
    <div id="sliderOne" v-touch:swipe.left="slidePlus">
            <div v-on:click="slidePlus">
                <p>
                    Start
                </p>
            </div>    
    </div>
</template>

<script>
export default {
  name: 'step1',
  methods: {
      slidePlus() {
          this.$emit('stepSlidePlus')
      }
  }
}
</script>

<style scoped>
#sliderOne {
    height: 100%;
    position: relative;
    text-align: center;
    vertical-align: center;
    line-height: 20vw;
}

#sliderOne > div{
    width: 55vw;
    height: 55vw;
    color: white;
    background-color: orange;
    border-radius: 50%;
    cursor: pointer;
    
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    -webkit-tap-highlight-color: transparent;
    webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
    -khtml-user-select: none; /* Konqueror HTML */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* Internet Explorer/Edge */
    user-select: none; /* Non-prefixed version, current supported by Chrome and Opera */
}

#sliderOne > div > p{
    font-family: 'Ubuntu', sans-serif;
    font-size: 2em;
    font-weight: bold;
    text-transform: uppercase;

    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

#sliderOne > div:active{
    width: 51vw;
    height: 51vw;
    transition: 0.1s;
}

@media only screen and (min-width: 470px) {
    #sliderOne > div{
        width: 35vw;
        height: 35vw;
    }

    #sliderOne > div > p{
        font-size: 2.5em;
    }

    #sliderOne > div:active{
        width: 33vw;
        height: 33vw;
    }
}

@media only screen and (min-width: 1070px) {
    #sliderOne > div{
        width: 20vw;
        height: 20vw;
    }

    #sliderOne > div > p{
        font-size: 3em;
    }

    #sliderOne > div:active{
        width: 19vw;
        height: 19vw;
    }
}
</style>
