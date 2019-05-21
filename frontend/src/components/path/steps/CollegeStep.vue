<template>
    <div id="collegeStep" v-touch:swipe.left="slidePlus" v-touch:swipe.right="slideMinus">
        <p>{{ data.fakultet }}</p>
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

<style>
#collegeStep{
    position: fixed;
    width: 100%;
    background-color: blue;
}
</style>
