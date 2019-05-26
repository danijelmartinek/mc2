<template>
    <div id="start">
			<span class="bg"></span>
			<transition-group tag="div" class="comp-slider" :name="transitionDirection">
				<div v-for="n in [currentComp]" v-bind:key="n">
					<component v-on:stepSlidePlus="slidePlus" v-on:stepSlideMinus="slideMinus" v-bind:is="compList[n]"></component>
				</div>
			</transition-group>
	</div>   
</template>

<script>
import start from "@/components/start/Start.vue"
import next from "@/components/start/Next.vue"

export default {
	name: 'start',
	components: {
		start,
		next
	},
	data() {
		return {
			message: 'Click for slide',
			show: true,
			compList: [start, next],
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
#start {
	overflow: hidden;
}

.bg{
	z-index: -999;
	position: absolute;
	width: 100%;
	height: 100%;
	background-image: url("./../../assets/img/iconsPattern.svg");
	background-repeat: repeat;
	background-size: 200px 200px;
	opacity: 0.1;
	filter: alpha(opacity=10);
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