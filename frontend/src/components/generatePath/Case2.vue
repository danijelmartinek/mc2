<template>
    <div id="case2">
		<dropdown :options="skole" @select-item="onHighSchoolSelect" placeholder="Odaberite školu" noitems="Škola ne postoji" :v-if="dataLoaded[0] == true"></dropdown>
		<dropdown :options="zanimanja" @select-item="onProfessionSelect" placeholder="Odaberite zanimanje" noitems="Zanimanje ne postoji" :v-if="dataLoaded[1] == true"></dropdown>
		<br>
		<router-link tag="span" to="/mypath"><button>Potvrdi</button></router-link>
	</div>
</template>

<script>
import axios from 'axios'

import dropdown from "@/components/generatePath/Dropdown.vue"

export default {
	name: 'case2',
	components: {dropdown},
	data() {
		return {
			skole: [],
			zanimanja: [],
			dataLoaded: [false, false],
		}
	},
	mounted() {
		this.$store.state.selectedOptions.slucajOdabira = 2

		axios.get('/api/skole')
        .then(res => {
          if(res.status == 200){
			this.skole = res.data
			this.dataLoaded[0] = true
          }
		})

		axios.get('/api/zanimanja')
        .then(res => {
          if(res.status == 200){
			this.zanimanja = res.data
			this.dataLoaded[1] = true
          }
        })
	},
	methods: {
		onHighSchoolSelect(option) {
			this.$store.state.selectedOptions.skolaId = option._id
		},

		onProfessionSelect(option) {
			this.$store.state.selectedOptions.zanimanjeId = option._id
		}
	}
}
</script>

<style scoped>
</style>