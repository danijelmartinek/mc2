<template>
    <div id="profile">
        <div class="header">
            <h2>{{ $store.state.user.firstName }} {{ $store.state.user.lastName }}</h2>
            <div class="logout">
                <div class="confirm-btn" @click="logout()">Odjavi se</div>
            </div>
        </div>

        <div class="wrap">
            <h2>Putevi</h2>
            <div class="line"></div>
            <keep-alive>
                <paths></paths>
            </keep-alive>
        </div>

        <div class="wrap">
            <h2>Informacije</h2>
            <div class="line"></div>
            <userInfo></userInfo>
        </div>
	</div>   
</template>

<script>
import userInfo from "@/components/profile/settings/userInfo.vue"
import paths from "@/components/profile/settings/paths.vue"

export default {
    name: 'profile',
    components:{
        userInfo,
        paths
    },
	data() {
		return {

		}
    },
    mounted(){

    },
    methods: {
        logout(){
            this.$store.commit('logoutUser')
            this.$router.push({name: 'Start'})
        }
    }
}
</script>

<style scoped>
#profile{
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

.header > h2{
    float: left;
    width: 60%;
    font-size: 1.2em;
    padding: 1em;
    color: #F2F2F0;
}

.header > .logout{
    float: right;
    width: 40%;
    padding: 2em 1em 0em 0em;
    font-size: 0.7em;
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

@media only screen and (min-width: 470px) {
	.header > .logout{
        width: auto;
    }
}

@media only screen and (min-width: 1070px) {
	.header > h2{
        float: left;
        width: 50%;
        font-size: 2.5em;
        padding: 0.3em 0em 0em 1em;
        color: #F2F2F0;
    }

    .header > .logout{
        width: auto;
        padding: 2em;
        font-size: 1em;
    }
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
</style>