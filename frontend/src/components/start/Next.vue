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
          <span><svg class="selectIcon" data-name="college" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 316.35 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M313.24,116.71A9.19,9.19,0,0,1,309,132.59L140.06,167.16a8.37,8.37,0,0,1-2.05.18,19.27,19.27,0,0,1-4.21-1.13,9.27,9.27,0,0,1-1.69-1.17L3.11,50.64A9.2,9.2,0,0,1,7.36,34.75L176.29.18a9.26,9.26,0,0,1,4.22.14,9.1,9.1,0,0,1,3.72,2Z"/><path class="cls-1" d="M278.43,157.23a3.27,3.27,0,0,1,3.82,4.05L267,218.33a3.27,3.27,0,0,1-3.91,2.33l-3.49-.82a3.26,3.26,0,0,1-2.4-4L272,160.39a3.26,3.26,0,0,1,2.5-2.36Z"/><path class="cls-1" d="M259.32,227.29a9.34,9.34,0,0,1,6.61,11.45,9.25,9.25,0,0,1-4,5.46,8.93,8.93,0,0,1,2.59,8.47l-11.72,43.71a4.88,4.88,0,0,1-6,3.45l-12.87-3.45a4.89,4.89,0,0,1-3.46-6l11.71-43.72a8.91,8.91,0,0,1,6.47-6,9.33,9.33,0,0,1,10.69-13.36Z"/><path class="cls-1" d="M230.56,159,220,198.51a.41.41,0,0,1-.5.29l-.55-.14c-4.28-1.06-8.49-2.11-12.62-3.11-3.64-.88-6.89-1.64-9.93-2.32-19.08-4.29-34-5.17-45.63-2.68-14.38,3.09-23.53,11.33-27.2,24.53a.45.45,0,0,1-.52.36l-.36-.09a.41.41,0,0,1-.25-.28c4.07-15.37-2-29.06-18.09-40.69C92,165.49,73.65,157.6,48.18,150.29a.44.44,0,0,1-.27-.56l9.93-37,64.37,57.07a27.94,27.94,0,0,0,8.16,5,17.86,17.86,0,0,0,3.09,1.13,18.77,18.77,0,0,0,3.24.56,28.07,28.07,0,0,0,9.59-.26Z"/></svg></span>
          <span>
            <svg class="selectIcon" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
              viewBox="0 0 307.84 299.63" style="enable-background:new 0 0 307.84 299.63;" xml:space="preserve">
            <g id="XMLID_2_">
              <path class="st0" d="M190.95,9.72c29.9,8.02,48.33,37.67,42.97,67.61l-10-2.68c3.92-24.42-11.24-48.41-35.64-54.95
                c-24.4-6.53-49.52,6.66-58.34,29.77l-10-2.68C130.26,18.17,161.05,1.71,190.95,9.72z"/>
            </g>
            <g>
              <polygon class="st1" points="159.2,149.18 176.48,166.46 179.64,154.66 	"/>
              <path class="st0" d="M29.61,71.36l-5.4,20.14c-5.1,19.07,6.25,38.73,25.31,43.83l74.85,20.06l3.88-14.5l4.92,1.32L42.69,51.72
                C36.51,56.49,31.79,63.25,29.61,71.36z"/>
              <path class="st0" d="M305.87,288.14l-35.4-35.4c0.38-1.03,0.73-2.08,1.02-3.16l15.53-57.94c-10.84,7.94-25.06,11.09-39.02,7.34
                l-42.73-11.45l-14.32-14.32l59.67,15.99c19.06,5.11,38.72-6.24,43.83-25.3l5.4-20.14c5.28-19.7-6.46-40.02-26.16-45.31L74.92,45.2
                c-4.39-1.18-8.8-1.49-13.07-1.08L19.7,1.97c-2.63-2.63-6.89-2.63-9.52,0c-2.63,2.63-2.63,6.89,0,9.52l286.17,286.17
                c1.32,1.31,3.04,1.97,4.76,1.97s3.45-0.66,4.76-1.97C308.5,295.03,308.5,290.77,305.87,288.14z"/>
              <path class="st0" d="M170.46,188.89c-3.34,12.48-16.22,19.93-28.7,16.57l-6.09-1.63c-12.48-3.34-19.93-16.22-16.57-28.71l2.66-9.95
                l-74.85-20.06c-13.96-3.75-24.7-13.58-30.12-25.88L1.26,177.17c-5.28,19.7,6.46,40.02,26.16,45.31l198.75,53.26
                c12.04,3.22,24.3,0.09,33.23-7.32l-86.95-86.95L170.46,188.89z"/>
              <path class="st0" d="M135.43,153.29l-6.56,24.45c-1.89,7.1,2.33,14.41,9.42,16.31l6.1,1.63c7.09,1.9,14.41-2.32,16.31-9.42
                l3.5-13.05l-16.69-16.69L135.43,153.29z"/>
              <polygon class="st0" points="175.76,169.15 180.41,170.39 176.48,166.46 	"/>
            </g>
            </svg>
          </span>
        </router-link>
      </div>
      <div class="dcol s-12 m-6 gridSelect">
        <router-link tag="div" to="/case/2">
          <span>
            <svg class="selectIcon" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
              viewBox="0 0 310.9 299.8" style="enable-background:new 0 0 310.9 299.8;" xml:space="preserve">
            <g id="XMLID_2_">
              <path class="st0" d="M273.64,157.01c2.35-0.48,4.36,1.67,3.75,3.98l-15.03,56.06c-0.45,1.68-2.16,2.69-3.85,2.29
                c-1.15-0.27-2.29-0.54-3.42-0.81c-1.76-0.41-2.83-2.2-2.36-3.96l14.59-54.47c0.32-1.18,1.27-2.07,2.46-2.32L273.64,157.01z"/>
            </g>
            <g>
              <path class="st0" d="M7.24,36.64c-3.42,0.7-6.01,3.13-6.91,6.51c-0.91,3.38,0.12,6.78,2.73,9.11l126.79,112.42
                c0.51,0.45,1.07,0.83,1.65,1.15c1.34,0.52,2.73,0.9,4.14,1.12c0.67,0.02,1.35-0.04,2.02-0.18l13.81-2.83L21.28,33.76L7.24,36.64z"
                />
              <path class="st0" d="M226.49,287.88c-0.68,2.56,0.83,5.19,3.4,5.88l12.65,3.4c2.57,0.68,5.19-0.83,5.88-3.4l6.94-25.91
                l-18.54-18.54L226.49,287.88z"/>
              <path class="st0" d="M307.85,117.18L181.06,4.75c-1.06-0.94-2.32-1.6-3.65-1.96c-1.35-0.36-2.77-0.42-4.15-0.13L44.9,28.93
                L18.13,2.16c-2.88-2.88-7.55-2.88-10.42,0c-2.88,2.88-2.88,7.55,0,10.42l285.06,285.06c1.44,1.44,3.33,2.16,5.21,2.16
                c1.89,0,3.77-0.72,5.21-2.16c2.88-2.88,2.88-7.55,0-10.42l-45.17-45.17c1.57-1.19,2.78-2.88,3.33-4.93
                c1.32-4.9-1.59-9.94-6.5-11.25c-3.71-1-7.5,0.44-9.69,3.32l-31.94-31.94c0.64,0.16,1.27,0.31,1.92,0.47l0.55,0.14
                c0.21,0.05,0.43-0.08,0.49-0.29l10.42-38.88l-43.1,8.82l-8.41-8.41l128.58-26.31c3.42-0.7,6.01-3.13,6.92-6.51
                C311.49,122.9,310.46,119.5,307.85,117.18z"/>
              <path class="st0" d="M143.77,175.65c-3.08,0.63-6.28,0.71-9.42,0.26c-1.07-0.09-2.14-0.27-3.18-0.56
                c-1.04-0.27-2.06-0.65-3.04-1.11c-2.95-1.18-5.68-2.85-8.03-4.94l-63.26-56.09l-9.76,36.42c-0.07,0.27,0.05,0.49,0.27,0.55
                c25.03,7.19,43.07,14.94,55.16,23.68c15.8,11.42,21.78,24.88,17.78,39.98c0,0.05,0.11,0.24,0.25,0.27l0.35,0.1
                c0.21,0.05,0.44-0.11,0.51-0.36c3.6-12.96,12.6-21.07,26.73-24.11c7.95-1.7,17.47-1.8,28.85-0.28l-17.12-17.12L143.77,175.65z"/>
            </g>
            </svg>
          </span>
          <span><svg class="selectIcon" data-name="profession" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 335.41 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M304.86,101.1A41.28,41.28,0,0,1,334,151.57L328,174a39.9,39.9,0,0,1-48.83,28.18l-83.38-22.34,4.32-16.14-57.23-15.34-4.32,16.15L55.17,142.18A39.91,39.91,0,0,1,27,93.35l6-22.43A41.24,41.24,0,0,1,83.46,41.79Z"/><path class="cls-1" d="M319.72,204.91l-17.3,64.54a41.26,41.26,0,0,1-50.48,29.14L30.55,239.27A41.27,41.27,0,0,1,1.41,188.79L18.7,124.25a51.07,51.07,0,0,0,33.55,28.82l83.39,22.35-3,11.08a26.14,26.14,0,0,0,18.46,32l6.78,1.82a26.14,26.14,0,0,0,32-18.47l3-11.09,83.39,22.34A51.08,51.08,0,0,0,319.72,204.91Z"/><path class="cls-1" d="M212.7,2.25a66.07,66.07,0,0,1,47.87,75.31l-11.14-3a54.48,54.48,0,0,0-104.69-28l-11.15-3A66.07,66.07,0,0,1,212.7,2.25Z"/><path class="cls-1" d="M186.3,171.68,179,198.92a14.85,14.85,0,0,1-18.17,10.49L154,207.6a14.87,14.87,0,0,1-10.49-18.17l7.31-27.24Z"/></svg></span>
        </router-link>
      </div>
      <div class="dcol s-12 offset-m-3 m-6 gridSelect">
        <router-link tag="div" to="/case/1">
          <span><svg class="selectIcon" data-name="college" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 316.35 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M313.24,116.71A9.19,9.19,0,0,1,309,132.59L140.06,167.16a8.37,8.37,0,0,1-2.05.18,19.27,19.27,0,0,1-4.21-1.13,9.27,9.27,0,0,1-1.69-1.17L3.11,50.64A9.2,9.2,0,0,1,7.36,34.75L176.29.18a9.26,9.26,0,0,1,4.22.14,9.1,9.1,0,0,1,3.72,2Z"/><path class="cls-1" d="M278.43,157.23a3.27,3.27,0,0,1,3.82,4.05L267,218.33a3.27,3.27,0,0,1-3.91,2.33l-3.49-.82a3.26,3.26,0,0,1-2.4-4L272,160.39a3.26,3.26,0,0,1,2.5-2.36Z"/><path class="cls-1" d="M259.32,227.29a9.34,9.34,0,0,1,6.61,11.45,9.25,9.25,0,0,1-4,5.46,8.93,8.93,0,0,1,2.59,8.47l-11.72,43.71a4.88,4.88,0,0,1-6,3.45l-12.87-3.45a4.89,4.89,0,0,1-3.46-6l11.71-43.72a8.91,8.91,0,0,1,6.47-6,9.33,9.33,0,0,1,10.69-13.36Z"/><path class="cls-1" d="M230.56,159,220,198.51a.41.41,0,0,1-.5.29l-.55-.14c-4.28-1.06-8.49-2.11-12.62-3.11-3.64-.88-6.89-1.64-9.93-2.32-19.08-4.29-34-5.17-45.63-2.68-14.38,3.09-23.53,11.33-27.2,24.53a.45.45,0,0,1-.52.36l-.36-.09a.41.41,0,0,1-.25-.28c4.07-15.37-2-29.06-18.09-40.69C92,165.49,73.65,157.6,48.18,150.29a.44.44,0,0,1-.27-.56l9.93-37,64.37,57.07a27.94,27.94,0,0,0,8.16,5,17.86,17.86,0,0,0,3.09,1.13,18.77,18.77,0,0,0,3.24.56,28.07,28.07,0,0,0,9.59-.26Z"/></svg></span>
          <span><svg class="selectIcon" data-name="profession" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 335.41 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M304.86,101.1A41.28,41.28,0,0,1,334,151.57L328,174a39.9,39.9,0,0,1-48.83,28.18l-83.38-22.34,4.32-16.14-57.23-15.34-4.32,16.15L55.17,142.18A39.91,39.91,0,0,1,27,93.35l6-22.43A41.24,41.24,0,0,1,83.46,41.79Z"/><path class="cls-1" d="M319.72,204.91l-17.3,64.54a41.26,41.26,0,0,1-50.48,29.14L30.55,239.27A41.27,41.27,0,0,1,1.41,188.79L18.7,124.25a51.07,51.07,0,0,0,33.55,28.82l83.39,22.35-3,11.08a26.14,26.14,0,0,0,18.46,32l6.78,1.82a26.14,26.14,0,0,0,32-18.47l3-11.09,83.39,22.34A51.08,51.08,0,0,0,319.72,204.91Z"/><path class="cls-1" d="M212.7,2.25a66.07,66.07,0,0,1,47.87,75.31l-11.14-3a54.48,54.48,0,0,0-104.69-28l-11.15-3A66.07,66.07,0,0,1,212.7,2.25Z"/><path class="cls-1" d="M186.3,171.68,179,198.92a14.85,14.85,0,0,1-18.17,10.49L154,207.6a14.87,14.87,0,0,1-10.49-18.17l7.31-27.24Z"/></svg></span>
        </router-link>
      </div>
      <div class="dcol xs-12 offset-m-1 m-10">
        <legenda id="legenda"></legenda>
      </div>
    </div>
  </div>
</template>

<script>
import legenda from "@/components/start/legend.vue"

export default {
  name: 'next',
  components: {
    legenda
  },
  mounted(){
    let elem = document.getElementById("legenda")
    elem.addEventListener('mousewheel', function(e) {
      this.scrollLeft -= (e.wheelDelta);
      e.preventDefault();
    }, false);
     
    function preventSwipe(e) {
      e.stopPropagation()
    }
    elem.addEventListener("touchstart", preventSwipe)
  },
  methods: {
      slideMinus() {
          this.$emit('stepSlideMinus')
      }
  }
}
</script>

<style scoped>

.gridSelectContainer{
  width: 95%;
  position: absolute;
  margin: 0 auto;
}

.gridSelectContainer > div{
  position: relative;
  top: 50%;
  transform: translateY(-50%);
}

.gridSelect{
	padding: 1em 2em 1em 2em;
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
    font-size: 1em;
  }
  
}

@media only screen and (min-width: 710px) {
  .gridSelectContainer{
    width: 80%;
  }

  .gridSelect{
    padding: 0.5em 0.5em 0.5em 0.5em;
    font-size: 1.5em;
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



.selectIcon{
  width: 3em;
  padding: 0.5em;
  margin: 0em 1em 0em 1em;
  fill: #F2F2F0;
}
</style>
