<template>
    <div id="professionStep" v-touch:swipe.right="slideMinus">
         <div class="viewContainer">
            <h1 class="collegeTitle">
                <span class="titleIcon-container"><svg class="titleIcon" data-name="profession" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 335.41 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M304.86,101.1A41.28,41.28,0,0,1,334,151.57L328,174a39.9,39.9,0,0,1-48.83,28.18l-83.38-22.34,4.32-16.14-57.23-15.34-4.32,16.15L55.17,142.18A39.91,39.91,0,0,1,27,93.35l6-22.43A41.24,41.24,0,0,1,83.46,41.79Z"/><path class="cls-1" d="M319.72,204.91l-17.3,64.54a41.26,41.26,0,0,1-50.48,29.14L30.55,239.27A41.27,41.27,0,0,1,1.41,188.79L18.7,124.25a51.07,51.07,0,0,0,33.55,28.82l83.39,22.35-3,11.08a26.14,26.14,0,0,0,18.46,32l6.78,1.82a26.14,26.14,0,0,0,32-18.47l3-11.09,83.39,22.34A51.08,51.08,0,0,0,319.72,204.91Z"/><path class="cls-1" d="M212.7,2.25a66.07,66.07,0,0,1,47.87,75.31l-11.14-3a54.48,54.48,0,0,0-104.69-28l-11.15-3A66.07,66.07,0,0,1,212.7,2.25Z"/><path class="cls-1" d="M186.3,171.68,179,198.92a14.85,14.85,0,0,1-18.17,10.49L154,207.6a14.87,14.87,0,0,1-10.49-18.17l7.31-27.24Z"/></svg></span>
                {{ data.selectedProfession.naziv }}
            </h1>
            <h5>Potrebna razina obrazovanja: <span style="text-transform: lowercase">{{ data.selectedProfession.minimalnaRazinaObrazovanja }}</span></h5>
            <div class="divider"></div>
            <div class="elementDistancer"></div>
            <div><b>OPIS ZANIMANJA</b></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div><b>NEDAVNI OGLASI</b></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div><b>TVRTKE KOJE SE BAVE OVIM ZANIMANJEM</b></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
        </div>
	</div>   
</template>

<script>

// import accordion from "@/assets/scripts/accordion/Accordion.vue"

export default {
    name: 'professionStep',

    components: {
        // accordion,
    },

    props:['data'],

	data() {
		return {}
    },

    watch: {
        'data.selectedProfession._id':function() {}
    },

    methods: {
        slideMinus() {
            this.$emit('stepSlideMinus') //funkcija koja prebacuje pogled na fakultet
        },

        // generateID(){
        //     let S4 = function() {
        //         return (((1+Math.random())*0x10000)|0).toString(16).substring(1)
        //     }
        //     return (S4()+S4()+"-"+S4()+"-"+S4()+S4()+S4())
        // }
    }
}
</script>

<style scoped>
#collegeStep{
    width: 100%;
}

.viewContainer{
    width: 90%;
    margin: 0 auto;
    margin-top: 1em;
    padding: 1em;
    margin-bottom: 3em;
    border-radius: 20px;
    color: #2C365D;
}

.collegeTitle{
    margin-top: 1.5em; 
    font-size: 2.5em;
}

.titleIconContainer{
    position: absolute;
}

.titleIcon{
    position: absolute;
    width: 2em;
    top: -2%;
    left: 8%;
    fill: #2C365D;
    margin: 0.5em 0.2em 0em 0em;
}

.infoElementNested{
    margin-left: 2em;
}

.divider{
    width: 100%;
    padding: 0.5em;
    border-bottom: 2px solid #2C365D;
    opacity: 0.2;
}

.float-left{
    float: left;
}


.float-right{
    display: block;
}

.elementDistancer{
    width: 100%;
    height: 1em;
}

@media only screen and (min-width: 1070px){
    .collegeTitle{
        margin-top: 0; 
        font-size: 2.5em;
    }

    .float-right{
        float: right;
    }

    .hideUp{
        display: none;
    }
}
</style>
