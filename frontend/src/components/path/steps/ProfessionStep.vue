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
    width: 100%;
    height: 62vh;
    background-color: blue;
    overflow-y: scroll;
}

@media only screen and (min-width: 1070px) {

    #professionStep{
        height: 82vh;
    }
}
</style>
