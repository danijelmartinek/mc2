<template>
    <div id="case1">
		<dropdown :options="skole" @select-item="onHighSchoolSelect" placeholder="Odaberite školu" noitems="Škola ne postoji" :v-if="dataLoaded[0] == true"></dropdown>
        <dropdown :options="fakulteti" @select-item="onCollegeSelect" placeholder="Odaberite fakultet" noitems="Fakultet ne postoji" :v-if="dataLoaded[1] == true">
			<!-- <template slot="item" slot-scope="option">
				<span>
					<img :src="option.thumbnail">
				</span>
			</template> -->
		</dropdown>
		<dropdown :options="college.smjerovi" @select-item="onCollegeCourseSelect" placeholder="Odaberite smjer" noitems="Smjer ne postoji" v-if="collegeSelected"></dropdown>
		<dropdown :options="zanimanja" @select-item="onProfessionSelect" placeholder="Odaberite zanimanje" noitems="Zanimanje ne postoji" :v-if="dataLoaded[2] == true"></dropdown>
		<br>
		<router-link tag="span" to="/mypath"><button>Potvrdi</button></router-link>
	</div>
</template>

<script>
import axios from 'axios'

import dropdown from "@/components/generatePath/Dropdown.vue"

export default {
	name: 'case1',
	components: {dropdown},
	data() {
		return {
			skole: [],
			fakulteti: [],
			zanimanja: [],
			dataLoaded: [false, false, false],
			college: {},
			collegeSelected: false
		}
	},
	mounted() {
		this.$store.state.selectedOptions.slucajOdabira = 1

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

		axios.get('/api/zanimanja')
        .then(res => {
          if(res.status == 200){
			this.zanimanja = res.data
			this.dataLoaded[2] = true
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

		onProfessionSelect(option) {
			this.$store.state.selectedOptions.zanimanjeId = option._id
		}
	}
}
</script>

<style scoped>
</style>