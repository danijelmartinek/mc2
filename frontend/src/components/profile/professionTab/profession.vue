<template>
    <div id="profession">
        <span v-if="$store.state.user.savedPaths[0]">
            <div class="header">
                <h3>{{ profession.naziv }}</h3>
            </div>

            <div class="wrap">
                <h2>OPIS ZANIMANJA EUROPSKE KOMISIJE</h2>
                <div class="line"></div>
                <div>{{ profession.opis }}</div>
            </div>

            <div class="wrap">
                <h2>POTREBNA ZNANJA I VJEŠTINE</h2>
                <div class="line"></div>
                <span v-for="(znanje, index) in profession.potrebnaZnanja" :key="index">
                    <span v-if="index == 0" class="firstInArray">{{ znanje.naziv }}, </span>
                    <span v-if="index == (profession.potrebnaZnanja.length - 1)">{{ znanje.naziv }}.</span>
                    <span v-else>{{ znanje.naziv }}, </span>
                </span>
            </div>

            <div class="wrap">
                <h2>OPCIONALNA ZNANJA I VJEŠTINE</h2>
                <div class="line"></div>
                <span v-for="(znanje, index) in profession.opcionalnaZnanja" :key="index">
                    <span v-if="index == 0" class="firstInArray">{{ znanje.naziv }}, </span>
                    <span v-if="index == (profession.potrebnaZnanja.length - 1)">{{ znanje.naziv }}.</span>
                    <span v-else>{{ znanje.naziv }}, </span>
                </span>
            </div>

            <div class="wrap">
                <h2>TVRTKE KOJE SE BAVE OVIM ZANIMANJEM</h2>
                <div class="line"></div>
                <div class="company" v-for="company in companies" :key="company._id">
                    <h3><b>{{ company.nazivTvrtke }}</b></h3>
                    <br>
                    <div>OPIS TVRTKE:</div>
                    <div class="tab">{{ company.opis }}</div>
                    <br>
                    <span v-for="activity in company.djelatnosti" :key="activity._id">
                        <span v-if="activity._id == profession._id">
                            <div>OPIS DJELATNOSTI:</div>
                            <div class="description">{{ activity.opis }}</div>
                            <br>
                            <div>POVEZNICA: <a :href="activity.link">{{ activity.link }}</a></div>
                        </span>
                    </span>
                    <div class="line-long"></div>
                </div>
            </div>
        </span>
        <span v-else>
             <div class="header">
                <h3><i>Nemaš spremljenih puteva.</i></h3>
            </div>
        </span>
	</div>   
</template>

<script>
import axios from "axios"

export default {
    name: 'profession',

	data() {
		return {
            profession: {},
            companies: []
		}
    },

    mounted(){

        let headers = {
                'Content-Type': 'application/json'
            }
        let arr = [this.$store.state.user.selectedPath]

        axios.post('/api/getpaths', arr, {headers: headers})
        .then(res => {
            if(res.status == 200){

                let pathProfessionId = {
                    _id: res.data[0].zanimanje.zanimanjeId
                }

                axios.post('/api/zanimanje', pathProfessionId, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        this.profession = res.data
                        this.loadCompanies()
                    }
                })
            }
        })
        
    },
    methods: {
        loadCompanies(){
            const headers = {
                'Content-Type': 'application/json'
            }

            axios.post('/api/getcompanies', {zanimanjeId: this.profession._id}, {headers: headers})
            .then(res => {
                if(res.status == 200){
                    this.companies = res.data
                }
            })
        },
    }
}
</script>

<style scoped>
#profession{
    height: 92vh;
    overflow-x: hidden; 
    overflow-x: auto;
    padding-bottom: 10vh;
}

.header{
    width: 100%;
    height: 15vh;
    background-color: #2C365D;
}

.header > h3::first-letter { 
  text-transform: uppercase;
}

.header > h3{
    float: left;
    position: relative;
    top: 35%;
    transform: translateY(-50%);
    font-size: 1.2em;
    padding-left: 1em;
    color: #F2F2F0;
}

.wrap{
    padding: 2em;
    margin: 2em;
    background-color: #fff;
    color: #2C365D;
    border-radius: 2em;
    box-shadow: 0px 0px 20px 0px rgba(0, 0, 0, 0.2);
}

.wrap > h2{
    text-transform: uppercase;
}

.line{
    display: block;
    width: 20%;
    height: 5px;
    background-color: #FF5E3A;
    margin-bottom: 1em;
}

.line-long{
    display: block;
    width: 100%;
    height: 2px;
    background-color: #FF5E3A;
    margin: 1em 0em 1em 0em;
    opacity: 0.2;
}

.tab{
    margin-left: 1em;
}

.company{
    width: 100%;
    padding: 1em;
    background-color: #fff;
    border-radius: 1em;
}

.company > .icon{
    margin-top: -1em;
    font-size: 2em;
}

.company > .icon > span{
    background-color: #fff;
    padding: 0.2em;
    border-radius: 0.5em;
}

.company .description{
    padding-top: 0.5em;
    padding-left: 1em;
}
</style>