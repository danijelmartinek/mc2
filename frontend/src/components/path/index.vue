<template>
    <div id="myPath">
        <span class="bg"></span>
        <div id="pathSelect">
            <div class="heading">Odaberi fakultet i zanimanje</div>
            <div class="elem pathListElement" v-for="(path, i) in paths" :key="i" @click="changeSelectedPath(i)">
                <div>
                    <span>
                        <div>
                            {{path.fakultet.naziv}}
                            <div class="step-divider"></div>
                            {{path.zanimanje.naziv}}
                        </div>
                    </span>
                </div>
            </div>
            <div class="dummyPath"></div>
        </div>

        <stepSelector ref="stepIndicator" v-if="dataLoaded" :path="data.selectedPath" @stepClicked="changeSelectedStep"></stepSelector>

        <pathInfo ref="step" :data="data" v-on:stepSlidePlusEmitter="slidePlusEmitter" v-on:stepSlideMinusEmitter="slideMinusEmitter" v-on:togglePathSelector="togglePathSelector"></pathInfo>
        

        <div v-show="checkAuth" @click="savePath()" id="fab" class="fab" :class="{ fabselected: pathSaved }">
            <font-awesome-icon :icon="['fa', 'save']" />
        </div>
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
            dataLoaded: false,
            currentSelectedPathIndex: 0,
            paths: []
		}
    },

    beforeMount() {
        //kod navigacije pomoću 'back' i 'forward' strelica, 
        //prevencija slanja praznog objekta za generiranje puteva - validacija da prikaz puteva nije prazan objekt
        if(this.$store.state.routeHandler){
            this.$router.go(this.$router.currentRoute)
            this.$store.state.routeHandler = false
        }
    },

    mounted() {
        this.$store.state.routeHandler = true //učitana finalna ruta generiranja puteva

        const headers = {
            'Content-Type': 'application/json'
        }

        let url = ""

        //ovisno o odabranom slučaju, pokreće se određeni algoritam za generiranje puteva na serveru
        if(this.$store.state.selectedOptions.slucajOdabira == 0){
            this.$router.push('/')
        } else {
            
            if(this.$store.state.selectedOptions.slucajOdabira == 1){
                url = '/api/gencaseone'
            } else if(this.$store.state.selectedOptions.slucajOdabira == 2){
                url = '/api/gencasetwo'
            } else if(this.$store.state.selectedOptions.slucajOdabira == 3){
                url = '/api/gencasethree'
            }

            axios.post(url, this.$store.state.selectedOptions, {headers: headers})
            .then(res => {
                if(res.status == 200){
                    this.paths = res.data
                    this.getStepData()
                }
            })
        }
    },

	methods: {
        changeSelectedPath: function(index) { //na promjenu puta, mijenjaju se podaci koji se šalju na komponentu za prikaz pojedinosti puta
            this.data.selectedPath = this.paths[index]
            this.data.selectedHighSchool = this.paths[index].stepsData.highSchool
            this.data.selectedCollege = this.paths[index].stepsData.college
            this.data.selectedProfession = this.paths[index].stepsData.profession
            this.selectPathStyle(index)
        },

        changeSelectedStep: function(s) { //funkcija koja pokreće promjenu indikatora koraka puta (koraci puta = srednja škola, fakultet, zanimanje)
            this.$refs.step.changeStep(s)
        },

        selectPathStyle(index) { //funkcija koja postavlja stil odabranog puta
			let paths = document.getElementsByClassName("elem")
			
            paths[this.currentSelectedPathIndex].classList.remove("pathListElementSelected")
            paths[this.currentSelectedPathIndex].classList.add("pathListElement")
            this.currentSelectedPathIndex = index
            
            paths[index].classList.remove("pathListElement")
			paths[index].classList.add("pathListElementSelected")
        },
        
        slidePlusEmitter() {
            this.$refs.stepIndicator.changeStepPlus() //funkcija koja pokreće promjenu koraka puta u naprijed
        },

        slideMinusEmitter() {
            this.$refs.stepIndicator.changeStepMinus() //funkcija koja pokreće promjenu koraka puta u nazad
        },

        getStepData() { //vraća objekt sa školom, fakultetom i zanimanjem za svaki generirani put
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
                        path.stepsData = res.data

                        if(i == 0){
                            this.selectPathStyle(0)
                            this.changeSelectedPath(0)
                            this.dataLoaded = true
                        }
                    }
                })
            })
        },

        togglePathSelector(reveal) { //na mobilnom telefonu omogućuje sakrivanje trake za odabir puteva na scroll
            let elem = document.getElementById("pathSelect")

            if(reveal){
                elem.style.transform = "translateY(0%)"
                this.$refs.stepIndicator.moveSelector(0)
            } else {
                elem.style.transform = "translateY(-110%)"
                this.$refs.stepIndicator.moveSelector(1)
            }
        },

        savePath(){
            if(this.checkAuth){
                if(this.pathSaved){
                    let index = this.$store.state.user.savedPaths.indexOf(this.data.selectedPath._id)
                    this.$store.state.user.savedPaths.splice(index, 1);
                } else {
                    this.$store.state.user.savedPaths.push(this.data.selectedPath._id)
                }

                const headers = {
                    'Content-Type': 'application/json'
                }
                let obj = {
                    _id: this.$store.state.user._id,
                    savedPaths: this.$store.state.user.savedPaths
                }
                axios.post('/api/updatesavedpaths', obj, {headers: headers})
            }
        }
    },

    computed: {
        checkAuth() {
          return this.$store.getters.checkAuth
        },

        pathSaved() {
            if(this.checkAuth){
                if(this.$store.state.user.savedPaths.includes(this.data.selectedPath._id)){
                    return true
                } else {
                    return false
                }
            } else {
                return false
            }
        }
    }
}
</script>

<style scoped>
.bg{
    z-index: -999;
	position: absolute;
	width: 100%;
	height: 100%;
	background-image: url("./../../assets/img/iconsPattern.svg");
	background-repeat: repeat;
	background-size: 200px 200px;
	opacity: 0.1;
	filter: alpha(opacity=10);
}

#pathSelect{
    position: fixed;
    width: 100%;
    height: 20vh;
    top: 8%;
    padding: 0.2em 0em 0.2em 0em;
    overflow-y: hidden;
    overflow-x: scroll;
    white-space: nowrap;
    text-align: center;
    transition: 0.5s;

    background-color: #2C365D;
}

#pathSelect .heading{
    display: none;
    padding: 2em 1em 2em 1em;
    font-size: 1em;
    font-weight: bold;
    text-transform: uppercase;
    color: #F2F2F0;
    white-space: normal;
}

.pathListElement{
    height: 100%;
    width: 80%;
    font-size: 1em;
    display: inline-block;
    margin-left: 0.5em;
    margin-right: 0.5em;
}

.pathListElement > div{
    text-align: center;
    display: inline-block;
    width: 100%;
    height: 80%;
    padding: 0.5em;

    color: #2C365D;

    background-color: #F2F2F0;
    border-radius: 25px;

    cursor: pointer;
}

.pathListElementSelected{
    height: 100%;
    width: 80%;
    position: relative;
    display: inline-block;
    margin-left: 0.5em;
    margin-right: 0.5em;
}


.pathListElement > div > span {
    display: block;
    position: relative;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    white-space: nowrap; 
    overflow: hidden;
    text-overflow: ellipsis;
}

.pathListElement > div > span > div{
    white-space: nowrap; 
    overflow: hidden;
    text-overflow: ellipsis;
}

.pathListElementSelected > div{
    display: table;
    width: 100%;
    height: 100%;
    text-align: center;
    display: inline-block;
    padding: 1em;

    color: #2C365D;

    box-shadow: 0px 0px 50px 10px rgba(0, 0, 0, 0.5);

    background-color: #F2F2F0;
}

.pathListElementSelected > div > span {
    display: block;
    position: relative;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
}

.pathListElementSelected > div > span > div{
    white-space: nowrap; 
    overflow: hidden;
    text-overflow: ellipsis;
}

.step-divider{
    width: 60%;
    height: 0.2em;
    margin-left: 20%;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
    background-color: #FF5E3A;
}

.dummyPath{
    height: 20%;
}

@media only screen and (min-width: 1070px) {

    #pathSelect{
        position: fixed;
        top: 12%;
        width: 25%;
        height: 85%;
        padding: 0.5em 0em 0.5em 0em;
        border-top-right-radius: 50px;
        border-bottom-right-radius: 50px;
        overflow-y: scroll;
        overflow-x: hidden;
        box-shadow: 0px 0px 15px 15px rgba(0, 0, 0, 0.2);
    }

    #pathSelect::-webkit-scrollbar {
        width: 8px;
    }

    #pathSelect .heading{
        display: block;
    }

    .pathListElement{
        display: block;
        width: 90%;
        height: auto;
        margin: 0 auto;
        padding: 1em 0.5em 1em 0.5em;
        font-size: 1em;
        white-space: normal;
    }

    .pathListElement > div {
        width: 100%;
        height: auto;
        padding: 1em 0.5em 1em 0.5em;
    }

    .pathListElement > div > span {
        display: inline;
        position: static;
        white-space: nowrap; 
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .pathListElement > div > span > div{
        width: 100%;
        padding: 0em 2em 0em 2em;
        white-space: nowrap; 
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .pathListElementSelected {
        height: auto;
    }

    .pathListElementSelected > div {
        width: 140%;
        height: auto;
        margin-left: -20%;
        padding: 1.5em 0.5em 1.5em 0.5em;
        border: 0.2em solid #FF5E3A;
        box-shadow: 0px 0px 15px 30px rgba(0, 0, 0, 0.2);
    }

    .pathListElementSelected > div > span {
        display: inline;
        position: static;
    }

    .pathListElementSelected > div > span > div{
        width: 100%;
        padding: 0em 2em 0em 4em;
        white-space: nowrap; 
        overflow: hidden;
        text-overflow: ellipsis;
    }
}


.fab{
    width: 3em;
    height: 3em;
    position: fixed;
    bottom: 1.5em;
    right: 1.5em;
    box-shadow: 0px 0px 40px 2px rgb(44, 54, 93, 0.5);

    color: #F2F2F0;
    background-color: #2C365D;
    border-radius: 50%;
    z-index: 999;
    cursor: pointer;
}
.fab:hover{
    background-color: #2C365D;
    opacity: 0.8;
}


.fab > svg{
    font-size: 1.5em;
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.fabselected{
    background-color: #FF5E3A;
    box-shadow: 0px 0px 40px 2px rgb(255, 94, 58, 0.5);
}
.fabselected:hover{
    background-color: #FF5E3A;
    opacity: 0.8;
}
</style>