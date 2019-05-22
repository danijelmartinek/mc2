<template>
    <div id="collegeStep" v-touch:swipe.left="slidePlus" v-touch:swipe.right="slideMinus">
         <div class="viewContainer">
            <h1>{{ data.selectedCollege.naziv }}</h1>
            <h2>{{ data.selectedCollege.vrstaVisokogUcilista }}</h2>
        </div>
	</div>   
</template>

<script>
export default {
    name: 'collegeStep',
    props:['data'],
	data() {
		return {
        
        }
    },
    methods: {
        slidePlus() {
            this.$emit('stepSlidePlus')
        },

        slideMinus() {
            this.$emit('stepSlideMinus')
        }
    }
}
</script>

<style scoped>
#collegeStep{
    width: 100%;
    height: 62vh;
    background-color: blue;
    overflow-y: scroll;
}

.viewContainer{
    width: 90%;
    margin: 0 auto;
}

@media only screen and (min-width: 1070px) {

    #collegeStep{
        height: 82vh;
    }
}
</style>
