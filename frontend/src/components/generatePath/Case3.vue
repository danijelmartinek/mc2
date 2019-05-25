<template>
    <div id="case3">
		<dropdown :options="skole" @select-item="onHighSchoolSelect" placeholder="Odaberite školu" noitems="Škola ne postoji" :v-if="dataLoaded[0] == true"></dropdown>
        <dropdown :options="fakulteti" @select-item="onCollegeSelect" placeholder="Odaberite fakultet" noitems="Fakultet ne postoji" :v-if="dataLoaded[1] == true"></dropdown>
		<dropdown :options="college.smjerovi" @select-item="onCollegeCourseSelect" placeholder="Odaberite smjer" noitems="Smjer ne postoji" v-if="collegeSelected"></dropdown>
		<br>
		<router-link tag="span" to="/mypath"><button>Potvrdi</button></router-link>
	</div>
</template>

<script>
import axios from 'axios'

import dropdown from "@/components/generatePath/Dropdown.vue"

export default {
	name: 'case3',
	components: {dropdown},
	data() {
		return {
			skole: [],
			fakulteti: [],
			dataLoaded: [false, false],
			college: {},
			collegeSelected: false
		}
	},
	mounted() {
		this.$store.state.selectedOptions.slucajOdabira = 3

		axios.get('/api/skole')
        .then(res => {
          if(res.status == 200){
			this.skole = res.data
			this.dataLoaded[0] = true
          }
		})

		axios.get('/api/fakulteti')
        .then(res => {
          if(res.status == 200){
			this.fakulteti = res.data
			this.dataLoaded[1] = true
          }
		})

	},
	methods: {
		onHighSchoolSelect(option) {
			this.$store.state.selectedOptions.skolaId = option._id
		},

		onCollegeSelect(option) {
			this.$store.state.selectedOptions.fakultetId = option._id
			this.collegeSelected = false

			let t = this
			setTimeout(function(){
				t.college = option
				t.collegeSelected = true
			}, 100);
		},

		onCollegeCourseSelect(option) {
			this.$store.state.selectedOptions.smjerId = option._id
		},

	}
}
</script>

<style scoped>
</style>