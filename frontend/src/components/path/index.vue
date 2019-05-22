<template>
    <div id="myPath">
        <div id="pathSelect">
            <div class="heading">Odaberi fakultet i zanimanje</div>
            <div class="pathListElement pathSpacer" v-for="(path, i) in paths" :key="i" @click="changeSelectedPath(i)">
                <div>
                    {{path.fakultet.naziv}}
                    <br>
                    {{path.zanimanje.naziv}}
                </div>
            </div>
            <div class="dummyPath"></div>
        </div>

        <stepSelector ref="stepIndicator" v-if="dataLoaded" :path="selectedPath" @stepClicked="changeSelectedStep"></stepSelector>

        <pathInfo ref="step" :data="selectedPath" v-on:stepSlidePlusEmitter="slidePlusEmitter" v-on:stepSlideMinusEmitter="slideMinusEmitter"></pathInfo>

	</div>   
</template>

<script>
import stepSelector from "@/components/path/StepSelector.vue"
import pathInfo from "@/components/path/PathInfo.vue"

import json from './data.json'

export default {
	name: 'myPath',
	components: {
        stepSelector,
        pathInfo
	},
	data() {
		return {
            dataLoaded: false,
            currentSelectedPathIndex: 0,
            selectedPath: {},
            selectedStep: {},
			paths: json
		}
    },
    mounted() {
        this.selectPathStyle(0)
        this.selectedPath = this.paths[0]
        this.dataLoaded = true
    },
	methods: {
        changeSelectedPath: function(index) {
            this.selectedPath = this.paths[index]
            this.selectPathStyle(index)
        },

        changeSelectedStep: function(s) {
            this.$refs.step.changeStep(s)
        },

        selectPathStyle(index) {
			let paths = document.getElementsByClassName("pathListElement")
			
			paths[this.currentSelectedPathIndex].classList.remove("pathSelected")
			this.currentSelectedPathIndex = index
			
			paths[index].classList.add("pathSelected")
        },
        
        slidePlusEmitter() {
            this.$refs.stepIndicator.changeStepPlus()
        },

        slideMinusEmitter() {
            this.$refs.stepIndicator.changeStepMinus()
        }
    }
}
</script>

<style scoped>

#pathSelect{
    position: fixed;
    display: inline-block;
    width: 100%;
    height: 20%;
    top: 8%;
    padding: 0.2em 0em 0.2em 0em;
    overflow-y: hidden;
    overflow-x: scroll;
    white-space: nowrap;

    background-color: #0a2155;
}

#pathSelect .heading{
    display: none;
    padding: 2em 1em 2em 1em;
    font-family: 'Ubuntu', sans-serif;
    font-size: 1em;
    font-weight: bold;
    text-transform: uppercase;
    color: #fff;
    white-space: normal;
}

/* width */
#pathSelect::-webkit-scrollbar {
  height: 0px;
}

/* Track */
#pathSelect::-webkit-scrollbar-track {
  background: #001a4d; 
}
 
/* Handle */
#pathSelect::-webkit-scrollbar-thumb {
  background: #2d3953; 
}

/* Handle on hover */
#pathSelect::-webkit-scrollbar-thumb:hover {
  background: #0a2155; 
}

.pathListElement{
    font-size: 2.5vh;
    display: inline-block;
    margin: 1em 0.5em 1em 0.5em;
    padding: 1em;
}

.pathListElement > div{
    display: inline-block;
    width: 100%;
    height: 100%;
    padding: 1.5em;

    color: #fff;
    font-family: Roboto;
    

    background-color: #0c2869;
    border-radius: 10px;

    cursor: pointer;
}

#pathSelect > .pathSpacer{
    border-radius: 15px;
    padding: 0.2em;
}

#pathSelect > .pathSelected{
    background: #f54925;
    border-radius: 12px;
    padding: 0.2em;
}

.dummyPath{
    height: 20%;
    background-color: #0a2155 !important;
}

@media only screen and (min-width: 1070px) {

    #pathSelect{
        position: fixed;
        width: 20%;
        height: 100%;
        padding: 0.5em 0em 0.5em 0em;
        overflow-y: scroll;
        overflow-x: hidden;
    }

    #pathSelect::-webkit-scrollbar {
        width: 8px;
    }

    #pathSelect .heading{
        display: block;
    }

    .pathListElement{
        display: block;
        width: 95%;
        font-size: 1em;
        white-space: normal;
    }

    .pathListElement > div {
        width: 100%;
        height: 100%;
        padding: 1.5em;

        color: #fff;
        font-family: Roboto;
        

        background-color: #0c2869;
        border-radius: 10px;

        cursor: pointer;
    }
}
</style>