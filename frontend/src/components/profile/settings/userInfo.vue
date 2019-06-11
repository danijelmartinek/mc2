<template>
    <div id="userInfo">
        <div class="userInfoContainer">
            <span class="dataErrors">
                <h4 v-for="(err, i) in data.errors" :key="i">
                    {{ err }}
                </h4>
                <h4>{{data.status}}</h4>
            </span>
            <br>
            <h3>Osnovni podaci</h3>
            <div>
                <input
                    v-model="data.firstName"
                    class="dform"
                    placeholder="Ime"
                >
            </div>
            <div>
                <input
                    v-model="data.lastName"
                    class="dform"
                    placeholder="Prezime"
                >
            </div>
            <div>
                <input
                    v-model="data.email"
                    class="dform"
                    placeholder="E-mail"
                    required
                >
            </div>

            <br>
            <h3>Ostali podaci</h3>
            <div class="dropdown">
                <v-select 
                    class="style-chooser" 
                    label="naziv" 
                    :options="skole" 
                    :reduce="skola => skola._id" 
                    v-model="data.highSchool" 
                    :placeholder="selectedHS"
                >
                </v-select>
            </div>
            <br>
            <div>
                <input
                    v-model="data.address"
                    class="dform"
                    placeholder="Adresa"
                >
            </div>
            <div>
                <input
                    v-model="data.city"
                    class="dform"
                    placeholder="Grad"
                >
            </div>

            <br>
            <h3>Promijeni lozinku</h3>
            <div>
                <input
                    v-model="data.password"
                    class="dform"
                    placeholder="Lozinka"
                    type="password"
                    required
                >
            </div>
            <div>
                <input
                    v-model="data.confirmPassword"
                    class="dform"
                    placeholder="Potvrdi lozinku"
                    type="password"
                    required
                >
            </div>
            <div class="confirm-btn xs-12 m-4 l-2" v-if="validator" @click="save()">Spremi</div>
        </div>
	</div>   
</template>

<script>
import axios from "axios"

export default {
    name: 'userInfo',
	data() {
		return {
            skole: [],
            selectedHS: "",
            data: {
                email: this.$store.state.user.email,
                password: "",
                confirmPassword: "",
                firstName: this.$store.state.user.firstName,
                lastName: this.$store.state.user.lastName,
                highSchool: "",
                address: this.$store.state.user.address,
                city: this.$store.state.user.city,
                errors: [],
                status: null
            }
		}
    },
    mounted(){
        axios.get('/api/skole')
        .then(res => {
            if(res.status == 200){
                this.skole = res.data
                this.data.highSchool = this.$store.state.user.highSchool
                
                this.skole.forEach(hs => {
                    if(hs._id == this.$store.state.user.highSchool){
                        this.selectedHS = hs.naziv
                    }
                })
            }
        })
    },
    methods: {
        validateEmail(email) {
            return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
        },

        dataValidate() {
        
            this.data.errors = []

            if(!this.data.email) {
                this.data.errors.push("Email required.")
            } else if(!this.validateEmail(this.data.email)) {
                this.data.errors.push("Email must be in format example@domain.com")
            }

            if(this.data.password != "" || this.data.confirmPassword != ""){
                if(!this.data.password) this.data.errors.push("Password required.")
                if(!this.data.confirmPassword) {
                    this.data.errors.push("Confirm Password required.")
                } else if(this.data.password != this.data.confirmPassword) {
                    this.data.errors.push("Passwords must match")
                }
            }
            
            if(!this.data.firstName) this.data.errors.push("First name required.")
            if(!this.data.lastName) this.data.errors.push("Last name required.")
            if(!this.data.highSchool) this.data.errors.push("High school required.")

            if(!(this.data.errors && this.data.errors.length)){
                return true
            } else{
                return false
            }
        
        },

        save() {

            let valid = this.dataValidate();

            const userData = {
                _id: this.$store.state.user._id,
                email: this.data.email,
                password: this.data.password,
                firstName: this.data.firstName,
                lastName: this.data.lastName,
                highSchool: this.data.highSchool,
                address: this.data.address,
                city: this.data.city,
                selectedPath: this.$store.state.user.selectedPath,
                savedPaths: this.$store.state.user.savedPaths,
                role: this.$store.state.user.role,
                profilePic: this.$store.state.user.profilePic,
                createdAt: this.$store.state.user.createdAt,
                updatedAt: new Date()
            }

            if(valid){

                let headers = {
                    'Content-Type': 'application/json'
                }

                axios.post('/api/changeuserdata', userData, {headers: headers})
                .then(res => {
                    if(res.status == 200){
                        delete userData.password
                        this.data.password = ""
                        this.data.confirmPassword = ""

                        this.$store.state.user = userData
                    }
                })
            }
        }
    },
    computed:{
        validator() {
			let user = this.$store.state.user
			if(user.firstName == this.data.firstName && user.lastName == this.data.lastName && user.email == this.data.email && this.data.password == "" && user.highSchool == this.data.highSchool){
				return false
			} else {
				return true
			}
        }
    }
}
</script>

<style scoped>
@import './resetInputsStyle.css';

.userInfoContainer{
    position: relative;
    width: 100%;
}

@media only screen and (min-width: 1070px) {
	.userInfoContainer{
        width: 50%;
    }
    .dform{
        width: 100%;
    }
}

.dform {
  width: calc(100% - 1em);
  font-family: 'PublicSans';
  font-size: 1.2em;
  caret-color: #FF5E3A;
  height: 2em;
  color: #2C365D;
  padding-left: 1em;
  margin: 0.5em 0em 0.5em 0em;
  background-color: #F2F2F0;
  border-radius: 0.5em !important;
}
.dform::placeholder {
  color: #fd7d61;
  padding-left: 1em;
  font-size: 1em;
}

.dform:focus::placeholder {
  position: relative;
  color: #FF5E3A;
  top: -0.8em;
  font-size: 0.8em;
  padding-left: 0em;
  transition: 0.2s ease;
}

.dform:target {
  padding-left: 4em;
}

.dataErrors{
  color: #FF5E3A;
  padding: 1em 0em 0em 3em;
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
    margin-top: 1.5em;
    border-radius: 0.5em;
}

.confirm-btn:hover {
	background-color: #fd7d61;
}

.confirm-btn-disabled {
	width: auto !important;
	color: rgb(242, 242, 240, 0.5);
	font-weight: bold;
	text-transform: uppercase;
	cursor: pointer;
	background-color: #bebebe;
	padding: 1em;
	border-radius: 0.5em;
	box-shadow: 0px 0px 0px 0px rgba(0, 0, 0, 0);
}


.confirm-btn:active {
	font-size: 0.9em;
	box-shadow: 0px 0px 10px 2px rgba(0, 0, 0, 0.1);
}




.dataContainer{
  position: absolute;
  height: 92vh;
}

.dataForm{
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 1em;
}

.dataInputs{
  text-align: center;
}

.info{
  display: none;
  position: absolute;
  height: 92vh;
  width: 50%;
  background-color: #2C365D;
}

@media only screen and (min-width: 710px) {
    .dataForm {
        left: 50%;
        transform: translate(-50%, -50%);
        width: 60%;
    }
}

@media only screen and (min-width: 1070px) {
	.dataForm {
        width: 80%;
    }
  
    .info{
            display: block;
    }
    .dataContainer{
        left: 50%;
    }

}


.data{
  font-size: 0.9em;
  margin-top: 2em;
  font-weight: bold;
  color: #2C365D;
  text-align: center;
}

.data > span > div{
  font-size: 1.2em;
  border: 2px solid #2C365D;
  border-radius: 1em;
  padding: 0.5em;
  margin: 0em 2em 0em 2em;
  cursor: pointer;
}

.data > span > div:hover{
  color: #fd7d61;
  border: 2px solid #fd7d61;
}



.dropdown{
    padding-top: 1em;
}

.style-chooser >>> .style-chooser .vs__search::placeholder {
	background: #F2F2F0;
	color: #2C365D;
	opacity: 0.5;
	text-transform: lowercase;
	font-variant: 'PublicSansRegular';
	border-radius: 0.5em !important;
}

.style-chooser >>> .vs__search {
	color: #2C365D;
}

.style-chooser >>> .vs__dropdown-toggle {
	background: #F2F2F0;
	height: 40px;
	border: none;
    color: #F2F2F0;
	text-transform: lowercase;
	font-variant: small-caps;
	border-radius: 0.5em !important;
}

.style-chooser >>> .vs__selected{
	color: #2C365D;
}

.style-chooser >>> .vs__actions > svg{
	fill: #2C365D;
}

.style-chooser >>> .vs__actions > button > svg{
	fill: #2C365D;
}

.style-chooser >>> .vs__dropdown-menu {
	background: #F2F2F0;
	border: none;
	color: #2C365D;
	text-transform: lowercase;
	font-variant: small-caps;
	border-radius: 0.5em !important;
}

.style-chooser >>> .vs__dropdown-option{
	color: #2C365D !important;
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
