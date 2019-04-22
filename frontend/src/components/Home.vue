<template>
    <div id="slider">
		<transition-group tag="div" class="comp-slider" :name="transitionDirection">
			<div v-for="n in [currentComp]" v-bind:key="n">
				<component v-on:stepSlidePlus="slidePlus" v-on:stepSlideMinus="slideMinus" v-bind:is="compList[n]"></component>
			</div>
		</transition-group>
	</div>   
</template>

<script>
import step1 from "@/components/stepper/Step1.vue"
import step2 from "@/components/stepper/Step2.vue"

export default {
	name: 'home',
	components: {
		step1,
		step2
	},
	data() {
		return {
			message: 'Click for slide',
			show: true,
			compList: [step1, step2],
			currentComp: 0,
			transitionDirection: 'slide'
		}
	},
	methods: {
		slidePlus(){
			this.transitionDirection = 'slide'
			this.currentComp++
		},
		slideMinus(){
			this.transitionDirection = 'slideBack'
			this.currentComp--
		}	
	}
}
</script>

<style scoped>
#slider {
	overflow: hidden;
}

.slide-leave-active,
.slide-enter-active {
	transition: 0.5s;
}
.slide-enter {
	transform: translate(100%, 0);
}
.slide-leave-to {
	transform: translate(-100%, 0);
}

.slideBack-leave-active,
.slideBack-enter-active {
	transition: 0.5s;
}

.slideBack-enter {
	transform: translate(-100%, 0);
}
.slideBack-leave-to {
	transform: translate(100%, 0);
}

.comp-slider{
	overflow: hidden;
	position: relative;
	width: 100vw;
	height: 100vh;
}

.comp-slider div {
	position: absolute;
	top: 0;
	left: 0;
	bottom: 0;
	right:0;
}
</style>