<template>
    <div id="highSchoolStep" v-touch:swipe.left="slidePlus">
        <div class="viewContainer">
            <h1>{{ data.selectedHighSchool.naziv }}</h1>
            <h2>{{ data.selectedHighSchool.vrsta }}</h2>
        </div>
	</div>   
</template>

<script>
export default {
    name: 'highSchoolStep',
    props:['data'],
	data() {
		return {
        
        }
    },
    methods: {
        slidePlus() {
            this.$emit('stepSlidePlus')
        }
    }
}
</script>

<style scoped>
#highSchoolStep{
    width: 100%;
}

.viewContainer{
    width: 90%;
    margin: 0 auto;
}

@media only screen and (min-width: 1070px) {

}
</style>

