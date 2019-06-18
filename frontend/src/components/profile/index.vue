<template>
    <div id="profile">
        <navi :items="navItems" v-on:changePage="changePage"></navi>
		<component class="selectedPage" v-bind:is="compList[page]"></component>
	</div>   
</template>

<script>
import navi from "@/components/profile/navigation.vue"
import deadlines from "@/components/profile/deadlinesTab/deadlines.vue"
import college from "@/components/profile/collegeTab/college.vue"
import profession from "@/components/profile/professionTab/profession.vue"
import profile from "@/components/profile/profileTab/profile.vue"

export default {
	name: 'profile',

	components: {
		navi,
		deadlines,
		college,
		profession,
		profile
	},

	data() {
		return {
			navItems: [
				{
					text: "Matura",
					icon: ['fa', 'book']
				},
				{
					text: "Fakultet",
					icon: ['fa', 'graduation-cap']
				},
				{
					text: "Zanimanje",
					icon: ['fa', 'briefcase']
				},
				{
					text: "Profil",
					icon: ['fa', 'id-badge']
				}
			],
			page: 0,
			compList: [deadlines, college, profession, profile]
		}
	},
	
	methods:{
		changePage(i){
			this.page = i
		}
	}
}
</script>

<style>
.selectedPage{
	margin-left: 7em;
	width: calc(100% - 7em);
}
@media only screen and (max-width: 1070px) {
    .selectedPage{
		margin-left: 0em;
		width: 100%;
	}
}
</style>