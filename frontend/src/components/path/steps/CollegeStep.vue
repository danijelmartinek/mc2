<template>
    <div id="collegeStep" v-touch:swipe.left="slidePlus" v-touch:swipe.right="slideMinus">
         <div class="viewContainer">
            <h1 class="collegeTitle">
                <span class="titleIcon-container"><svg class="titleIcon" data-name="college" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 316.35 300"><defs></defs><title>Ikonice</title><path class="cls-1" d="M313.24,116.71A9.19,9.19,0,0,1,309,132.59L140.06,167.16a8.37,8.37,0,0,1-2.05.18,19.27,19.27,0,0,1-4.21-1.13,9.27,9.27,0,0,1-1.69-1.17L3.11,50.64A9.2,9.2,0,0,1,7.36,34.75L176.29.18a9.26,9.26,0,0,1,4.22.14,9.1,9.1,0,0,1,3.72,2Z"/><path class="cls-1" d="M278.43,157.23a3.27,3.27,0,0,1,3.82,4.05L267,218.33a3.27,3.27,0,0,1-3.91,2.33l-3.49-.82a3.26,3.26,0,0,1-2.4-4L272,160.39a3.26,3.26,0,0,1,2.5-2.36Z"/><path class="cls-1" d="M259.32,227.29a9.34,9.34,0,0,1,6.61,11.45,9.25,9.25,0,0,1-4,5.46,8.93,8.93,0,0,1,2.59,8.47l-11.72,43.71a4.88,4.88,0,0,1-6,3.45l-12.87-3.45a4.89,4.89,0,0,1-3.46-6l11.71-43.72a8.91,8.91,0,0,1,6.47-6,9.33,9.33,0,0,1,10.69-13.36Z"/><path class="cls-1" d="M230.56,159,220,198.51a.41.41,0,0,1-.5.29l-.55-.14c-4.28-1.06-8.49-2.11-12.62-3.11-3.64-.88-6.89-1.64-9.93-2.32-19.08-4.29-34-5.17-45.63-2.68-14.38,3.09-23.53,11.33-27.2,24.53a.45.45,0,0,1-.52.36l-.36-.09a.41.41,0,0,1-.25-.28c4.07-15.37-2-29.06-18.09-40.69C92,165.49,73.65,157.6,48.18,150.29a.44.44,0,0,1-.27-.56l9.93-37,64.37,57.07a27.94,27.94,0,0,0,8.16,5,17.86,17.86,0,0,0,3.09,1.13,18.77,18.77,0,0,0,3.24.56,28.07,28.07,0,0,0,9.59-.26Z"/></svg></span>
                {{ data.selectedCollege.naziv }}
            </h1>
            <h4>{{ data.selectedCollege.visokoUciliste }}</h4>
            <div>
                <span style="text-transform: capitalize;">{{ data.selectedCollege.razina }}</span> {{ data.selectedCollege.studij }}
                <div class="elementDistancer hideUp"></div>
                <span class="float-right">{{ data.selectedCollege.brojSemestara }} semestara, {{ data.selectedCollege.brojBodova }} ECTS</span>
            </div>
            <div class="divider"></div>
            <div class="elementDistancer"></div>
            
            <accordion :accordionID="'acc-' + generateID()" label="Smjerovi" width="200px" :customStyleWrap="'border-bottom: 2px solid #2C365D;'">
                <div v-for="smjer in data.selectedCollege.smjerovi" :key="smjer._id">
                    <accordion :accordionID="'acc-' + generateID()" :label="smjer.naziv" width="220px">
                        <div><b>KOLEGIJI:</b>
                            <div class="divider"></div>
                            <div v-for="kolegij in smjer.kolegiji" :key="kolegij._id">
                                <accordion :accordionID="'acc-' + generateID()" :label="kolegij.naziv">
                                    <div class="infoElementNested">{{ kolegij.semestar }}. semestar</div>
                                </accordion>
                                <div class="elementDistancer"></div>
                            </div>
                        </div>
                        <div><b>NAPOMENE:</b></div>
                        <div v-if="smjer.prehrana == true" class="infoElementNested">- smjer ima menzu</div>
                        <div class="elementDistancer"></div>
                        <div class="infoElement">
                            <accordion :accordionID="'acc-' + generateID()" label="Upis" width="200px" :customStyleWrap="'border-bottom: 2px solid #2C365D'">
                                <div>
                                    <div v-if="smjer.upis.prijemni == true"><b>*</b>POTREBNO JE POLAGANJE PRIJEMNOG ISPITA</div>
                                    <div v-if="smjer.upis.prijemni == true"><b>*</b>POTREBAN JE PORTFOLIO RADOVA</div>
                                    <div>
                                        <accordion :accordionID="'acc-' + generateID()" label="MATURA" width="200px">
                                            <div v-for="predmetMature in smjer.upis.maturaPredmeti" :key="predmetMature._id">
                                                <div class="infoElement">{{ predmetMature.naziv }} {{ ((predmetMature.razina[0]) ? '- ' + predmetMature.razina + ' razina' : '') }}</div>
                                            </div>
                                        </accordion>
                                    </div>
                                </div>
                            </accordion>
                        </div>
                    </accordion>
                </div>
            </accordion>

            <div class="elementDistancer"></div>
            <div><b>Korisni kolegiji na ovom fakultetu za budući posao:</b></div>
            <span v-for="(predmet, i) in korisniPredmeti" :key="i">
                {{ predmet }}
                <span v-if="!(i == (korisniPredmeti.length - 1))">,</span>
            </span>
            <div class="elementDistancer"></div>
            <div><b>SAVJETI STUDENATA OVOGA FAKULTETA</b></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div class="elementDistancer"></div>
            <div><b>LOKACIJA FAKULTETA</b></div>
        </div>
	</div>   
</template>

<script>
// import axios from 'axios'

import accordion from "@/components/path/steps/Accordion.vue"

export default {
    name: 'collegeStep',
    components: {
        accordion,
    },
    props:['data'],
	data() {
		return {
            korisniPredmeti: []
            // znanja: []
        }
    },
    watch: {
        'data.selectedCollege._id':function() {
            this.getCourses()
        }
    },
    mounted() {
        this.getCourses()

        // axios.get('/api/znanja')
		// .then(res => {
		// 	if(res.status == 200){
        //         this.data.selectedPath.fakultet.korisnaDobivenaZnanja.forEach(znanjeId => {
        //             res.data.forEach(z => {
        //                 if(znanjeId == z._id){
        //                     this.znanja.push(z)
        //                 }
        //             })
        //         })
		// 	}
		// })
    },
    methods: {
        slidePlus() {
            this.$emit('stepSlidePlus')
        },

        slideMinus() {
            this.$emit('stepSlideMinus')
        },

        generateID(){
            let S4 = function() {
                return (((1+Math.random())*0x10000)|0).toString(16).substring(1)
            }

            return (S4()+S4()+"-"+S4()+"-"+S4()+S4()+S4())
        },

        getCourses(){
            this.korisniPredmeti = []

            this.data.selectedPath.fakultet.korisnaDobivenaZnanja.forEach(znanjeId => {
                this.data.selectedCollege.smjerovi.forEach(s => {
                    s.kolegiji.forEach(k => {
                        k.dobivenaZnanja.forEach(znanje => {
                            if(!(this.korisniPredmeti.includes(znanje.naziv) == true)){
                                if(znanjeId == znanje._id){
                                    this.korisniPredmeti.push(znanje.naziv)
                                }
                            }
                        })
                    })
                })
            })
        }
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
