<template>
    <div id="college">
        <span v-if="$store.state.user.savedPaths[0]">
            <div class="header">
                <h3>{{ college.naziv }}</h3>
            </div>

            <div class="offset-xs-1 xs-10 offset-m-2 m-8 offset-l-4 l-4 dropdown">
                <v-select 
                    class="style-chooser" 
                    label="naziv" 
                    :options="college.smjerovi" 
                    v-model="study" 
                    placeholder="Smjer"
                >
                </v-select>
            </div>

            <div class="wrap" v-if="study">
                <h2>Predmeti</h2>
                <div class="line"></div>
                <br>
                <div v-for="(kolegij, index) in study.kolegiji" :key="kolegij._id">
                    <h3>{{ kolegij.naziv }}</h3>
                    <div class="tab">
                        <h4>Semestar: {{ kolegij.semestar }}</h4>
                        <h4>Dobivena znanja i komptencije:</h4>
                        <div class="tab" v-for="(znanje, ind) in kolegij.dobivenaZnanja" :key="znanje._id">
                            <span v-if="ind < listLimits[index]">{{ znanje.naziv }}</span>
                        </div>
                        <h5 v-if="listLimits[index] == defaultLimit" class="tab" style="cursor: pointer;" @click="showMore(index)">PRIKAŽI VIŠE</h5>
                        <h5 v-if="listLimits[index] > defaultLimit" class="tab" style="cursor: pointer;" @click="showLess(index)">PRIKAŽI MANJE</h5>
                    </div>
                    <div class="line-long"></div>
                </div>
            </div>

            <div class="wrap" v-if="study">
                <h2>Informacije</h2>
                <div class="line"></div>
                <br>
                <div v-if="college.lokacija">LOKACIJA FAKULTETA: <b>{{ college.lokacija.adresa }}, {{ college.lokacija.grad }}</b></div>
                <br>
                <div>RAZINA STUDIJA: <b>{{ college.razina }}</b></div>
                <br>
                <div>BROJ SEMESTARA: <b>{{ college.brojSemestara }}</b></div>
                <br>
                <div>BROJ ECTS BODOVA: <b>{{ college.brojBodova }}</b></div>
                <br>
                <div v-if="study.prehrana">- studij ima menzu</div>
                <div v-else>- studij nema menzu</div>

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
    name: 'college',

	data() {
		return {
            college: {},
            study: {},
            listLimits: [],
            defaultLimit: 4
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

                let pathCollegeId = {
                    _id: res.data[0].fakultet.fakultetId
                }

                axios.post('/api/fakultet', pathCollegeId, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        this.college = res.data
                        this.study = this.college.smjerovi[0]
                    }
                })
            }
        })
    },

    watch: {
        study(){ //na promjenu smjera, postavlja se početni limit znanja koja se prikazuju
            if(this.study){
                this.study.kolegiji.forEach(() => {
                    this.listLimits.push(this.defaultLimit)
                });
            }
        }
    },

    methods: {
        showMore(i){ //prikažu se sva znanja kolegija
            this.listLimits[i] = this.study.kolegiji[i].dobivenaZnanja.length
            this.$forceUpdate() //updatea se komponenta
        },

        showLess(i){ //mijenja se limit prikazivanja znanja kolegija na početni
            this.listLimits[i] = this.defaultLimit
            this.$forceUpdate()
        }
    }
}
</script>

<style scoped>
#college{
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

.confirm-btn {
    color: #F2F2F0;
    font-weight: bold;
    text-transform: uppercase;
    text-align: center;
    cursor: pointer;
    background-color: #FF5E3A;
    padding: 1em;
    margin: 0.6em;
    border-radius: 0.5em;
}

.confirm-btn:hover {
	background-color: #fd7d61;
}


.confirm-btn:active {
    font-size: 0.9em;
    margin: 1em 1em 0em 0em;
}


.dropdown{
    padding-top: 1em;
}

.style-chooser >>> .style-chooser .vs__search::placeholder {
	background: #2C365D;
	color: #F2F2F0;
	opacity: 0.5;
	text-transform: lowercase;
	font-variant: 'PublicSansRegular';
	border-radius: 0.5em !important;
}

.style-chooser >>> .vs__search {
	color: #F2F2F0;
}

.style-chooser >>> .vs__dropdown-toggle {
	background: #2C365D;
	height: 40px;
	border: none;
    color: #F2F2F0;
    padding-left: 1.8em;
	text-transform: lowercase;
	font-variant: small-caps;
	border-radius: 0.5em !important;
	box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.2);
}

.style-chooser >>> .vs__selected{
	color: #F2F2F0;
}

.style-chooser >>> .vs__dropdown-menu {
	background: #2C365D;
	border: none;
	color: #F2F2F0;
	text-transform: lowercase;
	font-variant: small-caps;
	border-radius: 0.5em !important;
}

.style-chooser >>> .vs__dropdown-option{
	color: #F2F2F0 !important;
	height: 3em !important;
	vertical-align: middle !important;
	line-height: 2.5em !important;
	white-space: nowrap; 
	overflow: hidden;
	text-overflow: ellipsis;
}

.style-chooser >>> .vs__dropdown-option--highlight{
	background: #FF5E3A !important;
}

.style-chooser >>> .vs__clear,
.style-chooser >>> .vs__open-indicator {
	fill: #F2F2F0;
}
</style>