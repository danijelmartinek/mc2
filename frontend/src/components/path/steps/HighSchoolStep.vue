<template>
    <div id="highSchoolStep" v-touch:swipe.left="slidePlus">
        <p>{{ data.skola }}</p>
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

<style>
#highSchoolStep{
    position: fixed;
    width: 100%;
    background-color: blue;
}
</style>

