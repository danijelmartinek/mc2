<template>
    <div id="start" v-touch:swipe.left="slidePlus">
        <div class="drow">
            <div class="info dcol xs-12 m-6">
                <p>
                    Pronađi svoj put!
                </p>
            </div>
            <div class="buttonContainer dcol xs-12 m-6" v-on:click="slidePlus">
                <span class="button">
                    <p>
                        Start
                    </p>
                </span>
            </div>
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
    text-align: center;
    vertical-align: center;
}

.info{
    height: 40vh;
    position: relative;
}

.info > p{
    font-family: 'PublicSansBlack';
    text-transform: uppercase;
    width: 50%;
    font-size: 2.5em;
    font-weight: 1000;
    color: #FF5E3A;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-shadow: 0px 0px 10px rgb(255, 94, 58, 0.5);
}

.buttonContainer{
    height: 40vh;
    position: relative;
}

.button{
    width: 55vw;
    height: 55vw;
    color: #F2F2F0;
    background-color: #FF5E3A;
    background-image: url("./../../assets/img/papyrus.png");
    background-blend-mode: multiply;
    border-radius: 50%;
    cursor: pointer;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    
    box-shadow: 0px 0px 30px 15px rgb(255, 94, 58, 0.3);

    -webkit-tap-highlight-color: transparent;
    webkit-touch-callout: none; /* iOS Safari */
    -webkit-user-select: none; /* Safari */
    -khtml-user-select: none; /* Konqueror HTML */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* Internet Explorer/Edge */
    user-select: none; /* Non-prefixed version, current supported by Chrome and Opera */
}

.button > p{
    font-size: 2em;
    font-weight: bold;
    text-transform: uppercase;

    margin: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.button:active{
    width: 51vw;
    height: 51vw;
    transition: 0.1s;
}

@media only screen and (min-width: 470px) {
    .info > p{
        font-size: 4em;
    }

    .button{
        width: 35vw;
        height: 35vw;
    }

    .button > p{
        font-size: 2.5em;
    }

    .button:active{
        width: 33vw;
        height: 33vw;
    }
}

@media only screen and (min-width: 710px) {
    .info{
        height: 75vh;
        text-align: left;
    }

    .info > p{
        font-size: 5em;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
        text-shadow: 0px 0px 15px rgb(255, 94, 58, 0.5);
    }

    .buttonContainer{
        height: 100vh;
    }
}

@media only screen and (min-width: 1070px) {
    .info > p{
        font-size: 6em;
        left: 62.5%;
        top: 50%;
        transform: translate(-50%, -50%);
    }

    .button{
        width: 20vw;
        height: 20vw;
        left: 37.5%;
    }

    .button > p{
        font-size: 3em;
    }

    .button:active{
        width: 19vw;
        height: 19vw;
    }
}
</style>
