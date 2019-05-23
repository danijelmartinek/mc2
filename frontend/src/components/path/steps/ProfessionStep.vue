<template>
    <div id="professionStep" v-touch:swipe.right="slideMinus">
        <div class="viewContainer">
            <h1>{{ data.selectedProfession.naziv }}</h1>
            <h2>{{ data.selectedProfession.kategorija }}</h2>
        </div>
	</div>   
</template>

<script>
export default {
    name: 'professionStep',
    props:['data'],
	data() {
		return {
        
        }
    },
    methods: {
        slideMinus() {
            this.$emit('stepSlideMinus')
        }
    }
}
</script>

<style scoped>
#professionStep{
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

    #professionStep{
        height: 82vh;
    }
}
</style>
