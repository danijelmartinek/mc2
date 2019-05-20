<template>
    <div id="myPath">
        
        <div id="pathSelectContainer">
            <div class="heading">Odaberi fakultet i zanimanje</div>
            <div id="pathSelect">
                <div class="pathListElement pathSpacer" v-for="(path, i) in paths" :key="i" @click="changeSelectedPath(i)">
                    <div>
                        {{path.college}}
                        <br>
                        {{path.profession}}
                    </div>
                </div>
                <div class="dummyPath"></div>
            </div>
        </div>

        <pathSelector :path="selectedPath" @stepClicked="changeSelectedStep"></pathSelector>

	</div>   
</template>

<script>
import pathSelector from "@/components/path/PathSelector.vue"

export default {
	name: 'myPath',
	components: {
		pathSelector
	},
	data() {
		return {
            currentSelectedPathIndex: 1,
            selectedPath: {
                highSchool: "Gimnazija",
                college: "TVZ",
                profession: "Programmer"
            },
            selectedStep: {},
            selectedStepNumber: 1,
			paths: [
                {
                    highSchool: "Gimnazija IZD",
                    college: "TVZ",
                    profession: "Programmer"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "Filozofski fakultet",
                    profession: "povjesničar"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "FSB",
                    profession: "Inžinjer aeronautike"
                },
                {
                    highSchool: " IZD",
                    college: "TVZ",
                    profession: "Programmer"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "Filozofski fakultet",
                    profession: "povjesničar"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "FSB",
                    profession: "Inžinjer aeronautike"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "TVZ",
                    profession: "Programmer"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "Filozofski fakultet",
                    profession: "povjesničar"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "FSB",
                    profession: "Inžinjer aeronautike"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "TVZ",
                    profession: "Programmer"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "Filozofski fakultet",
                    profession: "povjesničar"
                },
                {
                    highSchool: "Gimnazija IZD",
                    college: "FSB",
                    profession: "Inžinjer aeronautike"
                }
            ]
		}
    },
    mounted() {
        this.selectPathStyle(0)
    },
	methods: {
        changeSelectedPath: function(index) {
            this.selectedPath = this.paths[index]

            if(this.selectedStepNumber == 1){
                this.selectedStep = this.selectedPath.highSchool
            } else if(this.selectedStepNumber == 2) {
                this.selectedStep = this.selectedPath.college
            } else if(this.selectedStepNumber == 3) {
                this.selectedStep = this.selectedPath.profession
            }

            this.selectPathStyle(index)
        },
        changeSelectedStep: function(s) {
            this.selectedStepNumber = s
            if(s == 1){
                this.selectedStep = this.selectedPath.highSchool
            } else if(s == 2) {
                this.selectedStep = this.selectedPath.college
            } else if(s == 3) {
                this.selectedStep = this.selectedPath.profession
            }

            console.log(this.selectedStep)
        },

        selectPathStyle(index){
			let paths = document.getElementsByClassName("pathListElement")
			
			paths[this.currentSelectedPathIndex].classList.remove("pathSelected")
			this.currentSelectedPathIndex = index
			
			paths[index].classList.add("pathSelected")
		}
    }
}
</script>

<style scoped>
#pathSelectContainer{
    width: 100%;
    padding: 0.2em 0em 0.2em 0em;

    background-color: #0a2155;
}

#pathSelectContainer .heading{
    padding: 1em;
    font-family: 'Ubuntu', sans-serif;
    font-size: 1em;
    font-weight: bold;
    text-transform: uppercase;
    color: #fff;
}

#pathSelect{
    display: inline-block;
    width: 100%;
    height: 20vh;
    padding: 0.2em 0em 0.2em 0em;
    overflow-y: hidden;
    overflow-x: scroll;
    white-space: nowrap;

    background-color: #0a2155;
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
    border-radius: 15px;
    padding: 0.2em;
}

.dummyPath{
    height: 20%;
    background-color: #0a2155 !important;
}

@media only screen and (min-width: 1070px) {

    #pathSelectContainer{
        position: fixed;
        width: 20%;
        padding: 1em 0em 1em 0em;
    }

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

    .pathListElement{
        display: block;
        width: 95%;
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