<template>
    <div>
       <div id="toggleCategoryContainer">
          <div id="toggleCategory">
              <label class="select">
                  <input type="radio" checked="checked" @click="changeStepTo(0)" name="radio">
                  <span class="checkmark"></span>
                  <div class="text">{{ path.skola.naziv }}</div>
              </label>
              <div class="line"></div>
              <label class="select">
                  <input type="radio" @click="changeStepTo(1)" name="radio">
                  <span class="checkmark"></span>
                  <div class="text">{{ path.fakultet.naziv }}</div>
              </label>
              <div class="line"></div>
              <label class="select">
                  <input type="radio" @click="changeStepTo(2)" name="radio">
                  <span class="checkmark"></span>
                  <div class="text">{{ path.zanimanje.naziv }}</div>
              </label>
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'toggleStep',
  props: ['path'],
	data() {
		return {
			step: 0
		}
  },
  mounted(){
    this.$emit('stepClicked', 0)
  },
	methods: {
		changeStepTo: function(s) {
      if(this.step != s){
        this.step = s
        this.$emit('stepClicked', s)
      }
    }
	}
}
</script>

<style>
#selectedPath{
    width: 100%;
    height: 100%;
}

@media only screen and (min-width: 1070px) {

    #selectedPath{
        position: fixed;
        width: 80%;
        margin-left: 20%;
    }
}


#toggleCategoryContainer{
  position: fixed;
  height: 20%;
  width: 80%;
  right: 0;
  padding-top: 2em;
  
  background-color: #0a2763;
}

#toggleCategory{
  width: 80%;
  position: relative;
  left: 0;
  right: 0;
  margin: 0 auto;
  padding: 1em;
}

#toggleCategory:checked{
  right: 0%;
}


.select {
  width: 16%;
  float: left;
  position: relative;
  margin: 0.5em 0.15em 1.5em 0.15em;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.text {
  position: static;
  padding-top: 1em;
  font-size: 1em;
  font-weight: bold;
  font-family: Roboto;
  color: white;
  text-transform: uppercase;
  text-align: center;
}

/* Hide the browser's default radio button */
.select input {
  position: absolute;
  opacity: 0;
  cursor: pointer;
}

/* Create a custom radio button */
.checkmark {
  position: static;
  display: block;
  margin: 0 auto;
  height: 20px;
  width: 20px;
  background-color: #fff;
  border-radius: 50%;
}

/* On mouse-over, add a grey background color */
.select:hover input ~ .checkmark {
  background-color: #ffc9c2;
}

/* When the radio button is checked, add a blue background */
.select input:checked ~ .checkmark {
  background-color: #f53b24;
  box-shadow: 1px 1px 7px #f53b24;
}

.line{
  width: 24%;
  height: 5px;
  float: left;
  margin: 1em 0em 0em 0em;
  background-color: #fff;
  border-radius: 25px;
}
</style>
