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

        <stepSelector ref="stepIndicator" v-if="dataLoaded" :path="data.selectedPath" @stepClicked="changeSelectedStep"></stepSelector>

        <pathInfo ref="step" :data="data" v-on:stepSlidePlusEmitter="slidePlusEmitter" v-on:stepSlideMinusEmitter="slideMinusEmitter"></pathInfo>

	</div>   
</template>

<script>
import axios from 'axios'

import stepSelector from "@/components/path/StepSelector.vue"
import pathInfo from "@/components/path/PathInfo.vue"

export default {
	name: 'myPath',
	components: {
        stepSelector,
        pathInfo
	},
	data() {
		return {
            data: {
                selectedPath: {},
                selectedHighSchool: {},
                selectedCollege: {},
                selectedProfession: {}
            },
            stepDataArray: [],
            dataLoaded: false,
            currentSelectedPathIndex: 0,
			paths: []
		}
    },
    mounted() {

        let pathData = {
            "skolaId": "5cdebf15f88a0c5529953b7d",
            "fakultetId": "5cdec1dde96cf8578794928c",
            "zanimanjeId": "bf63bdd35bfea107408f28e1",
            "interesi": []
        }

        let headers = {
            'Content-Type': 'application/json'
        }

        axios.post('/api/gencasetwo', pathData, {headers: headers})
        .then(res => {
            if(res.status == 200){
                console.log(res.data)
                this.paths = res.data
                // this.paths.push(res.data)
                this.getStepData()
            }
        })
    },
	methods: {
        changeSelectedPath: function(index) {
            this.data.selectedPath = this.paths[index]
            this.data.selectedHighSchool = this.stepDataArray[index].highSchool
            this.data.selectedCollege = this.stepDataArray[index].college
            this.data.selectedProfession = this.stepDataArray[index].profession
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
        },

        getStepData() { //return object with highSchool, college and profession for each path
            this.paths.forEach((path, i) => {
                let reqData = {
                    highSchool: path.skola.skolaId,
                    college: path.fakultet.fakultetId,
                    profession: path.zanimanje.zanimanjeId
                }

                let headers = {
                    'Content-Type': 'application/json'
                }

                axios.post('/api/getstepdata', reqData, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        this.stepDataArray.push(res.data)

                        if(i == 0){
                            this.selectPathStyle(0)
                            this.changeSelectedPath(0)
                            this.dataLoaded = true
                        }
                    }
                })
            })
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