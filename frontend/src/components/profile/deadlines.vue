<template>
    <div id="deadlines">
        <timeline class="section1"></timeline>
        <repository class="section2"></repository>
	</div>   
</template>

<script>
import timeline from "@/components/profile/timeline.vue"
import repository from "@/components/profile/repository.vue"

export default {
    name: 'deadlines',
	components: {
        timeline,
        repository
    },
    props: ['items'],
	data() {
		return {

		}
    },
    mounted(){

    }
}
</script>

<style scoped>
#deadlines{
    height: 100vh;
    overflow-x: hidden; 
    overflow-x: auto;
}
.section1{
    float: left;
    width: 100%;
}
.section2{
    float: left;
    width: 100%;
}

@media only screen and (min-width: 1070px) {
    .section1{
        width: 50%;
    }
    .section2{
        width: 50%;
    }
}

</style>