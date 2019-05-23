<template>
    <div id="start" v-touch:swipe.left="slidePlus">
            <div v-on:click="slidePlus">
                <p>
                    Start
                </p>
            </div>    
    </div>
</template>

<script>
export default {
  name: 'start',
  methods: {
      slidePlus() {
          this.$emit('stepSlidePlus')
      }
  }
}
</script>

<style scoped>
#start {
    height: 100%;
    position: relative;
    text-align: center;
    vertical-align: center;
    line-height: 20vw;
}

#start > div{
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

#start > div > p{
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

#start > div:active{
    width: 51vw;
    height: 51vw;
    transition: 0.1s;
}

@media only screen and (min-width: 470px) {
    #start > div{
        width: 35vw;
        height: 35vw;
    }

    #start > div > p{
        font-size: 2.5em;
    }

    #start > div:active{
        width: 33vw;
        height: 33vw;
    }
}

@media only screen and (min-width: 1070px) {
    #start > div{
        width: 20vw;
        height: 20vw;
    }

    #start > div > p{
        font-size: 3em;
    }

    #start > div:active{
        width: 19vw;
        height: 19vw;
    }
}
</style>
