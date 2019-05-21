<template>
    <div id="professionStep" v-touch:swipe.right="slideMinus">
        <p>{{ data.zanimanje }}</p>
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

<style>
#professionStep{
    position: fixed;
    width: 100%;
    background-color: blue;
}
</style>
