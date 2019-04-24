<template>
    <div id="myPath">
        
        <div id="pathSelectContainer">
            <div class="heading">Odaberi fakultet i zanimanje</div>
            <div id="pathSelect">
                <div v-for="(path, i) in paths" :key="i">
                    {{path.college}}
                    <br>
                    {{path.profession}}
                </div>
            </div>
        </div>

        <selectedPath></selectedPath>

	</div>   
</template>

<script>
import selectedPath from "@/components/path/SelectedPath.vue"

export default {
	name: 'myPath',
	components: {
		selectedPath
	},
	data() {
		return {
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
	methods: {
		
	}
}
</script>

<style scoped>
#pathSelectContainer{
    width: 100%;
    padding: 0.2em 0em 0.2em 0em;

    background-color: red;
}

#pathSelectContainer .heading{
    padding: 1em;
    font-family: 'Ubuntu', sans-serif;
    font-size: 1em;
    font-weight: bold;
    text-transform: uppercase;
    color: #ffffff;
}

#pathSelect{
    width: 100%;
    height: 20vh;
    padding: 0.2em 0em 0.2em 0em;
    overflow-y: hidden;
    overflow-x: scroll;
    white-space: nowrap;

    background-color: red;
}

/* width */
#pathSelect::-webkit-scrollbar {
  height: 0px;
}

/* Track */
#pathSelect::-webkit-scrollbar-track {
  background: gray; 
}
 
/* Handle */
#pathSelect::-webkit-scrollbar-thumb {
  background: black; 
}

/* Handle on hover */
#pathSelect::-webkit-scrollbar-thumb:hover {
  background: #555; 
}

#pathSelect > div{
    display: inline-block;
    width: 50%;
    margin: 0.5em;
    padding: 1em;

    background-color: blue;
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

    #pathSelect > div{
        display: block;
        width: 90%;
        height: 100px;
        margin: 1em;
    }
}
</style>