<template>
    <div id="pathInfo">
		<transition-group tag="div" class="comp-slider" :name="transitionDirection">
			<div v-for="n in [currentComp]" v-bind:key="n">
				<component v-on:stepSlidePlus="slidePlus" v-on:stepSlideMinus="slideMinus" :data="data" v-bind:is="compList[n]"></component>
			</div>
		</transition-group>
	</div>   
</template>

<script>
import highSchoolStep from "@/components/path/steps/HighSchoolStep.vue"
import collegeStep from "@/components/path/steps/CollegeStep.vue"
import professionStep from "@/components/path/steps/ProfessionStep.vue"

export default {
    name: 'start',
    props: ['data'],
	components: {
		highSchoolStep,
        collegeStep,
        professionStep
	},
	data() {
		return {
			message: 'Click for slide',
			show: true,
			compList: [highSchoolStep, collegeStep, professionStep],
			currentComp: 0,
			transitionDirection: 'slide'
		}
    },
	methods: {
        changeStep(step){
            if(step >  this.currentComp){
                this.transitionDirection = 'slide'
                this.currentComp = step
            } else if(step < this.currentComp) {
                this.transitionDirection = 'slideBack'
                this.currentComp = step
            }
        },
        
		slidePlus(){
			this.transitionDirection = 'slide'
            this.currentComp++
            this.$emit('stepSlidePlusEmitter')
		},
		slideMinus(){
			this.transitionDirection = 'slideBack'
            this.currentComp--
            this.$emit('stepSlideMinusEmitter')
		}
	}
}
</script>

<style scoped>
#pathInfo {
	position: fixed;
    bottom: 0;
    right: 0;
    height: 62%;
    width: 100%;
    z-index: -100;

    background-color: #0c317a;
}

@media only screen and (min-width: 1070px) {

    #pathInfo {
        height: 72%;
        width: 80%;
    }
}

.slide-leave-active,
.slide-enter-active {
	transition: 0.4s;
}
.slide-enter {
	transform: translate(100%, 0);
}
.slide-leave-to {
	transform: translate(-100%, 0);
}

.slideBack-leave-active,
.slideBack-enter-active {
	transition: 0.4s;
}

.slideBack-enter {
	transform: translate(-100%, 0);
}
.slideBack-leave-to {
	transform: translate(100%, 0);
}
</style>