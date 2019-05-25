<template>
    <div id="pathInfo">
		<transition-group tag="div" class="comp-slider container" :name="transitionDirection">
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
    height: 57%;
    width: 100%;
    z-index: -100;
	overflow: auto;
}

.container{
	width: 100%;
	float: right;
	background-color: #F2F2F0;
}

@media only screen and (min-width: 1070px) {

    #pathInfo {
        height: 72%;
        width: 75%;
    }

	.container{
		width: 90%;
		height: 95.8%;
		border-top-left-radius: 50px;
        border-bottom-left-radius: 50px;
		background-color: #F2F2F0;
		box-shadow: 0px 0px 50px 5px rgba(0, 0, 0, 0.1);
		overflow: auto;
	}
}

.slide-leave-active,
.slide-enter-active {
	transition: 0s;
}
.slide-enter {
	transform: translate(100%, 0);
}
.slide-leave-to {
	transform: translate(-100%, 0);
}

.slideBack-leave-active,
.slideBack-enter-active {
	transition: 0s;
}

.slideBack-enter {
	transform: translate(-100%, 0);
}
.slideBack-leave-to {
	transform: translate(100%, 0);
}
</style>