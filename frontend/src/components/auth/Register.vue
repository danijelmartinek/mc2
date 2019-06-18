<template>
	<div id="register" class="drow">
        <div class="dcol xs-12 ml-6 info">
          <span class="illustration"><img src="./registerIllustration.svg"></span>
        </div>
        <div class="dcol xs-12 ml-6 registerContainer">
            <div class="registerForm">
                <div class="registerErrors">
                  <h4 v-for="(err, i) in register.errors" :key="i">
                      {{ err }}
                  </h4>
                  <h4>{{register.status}}</h4>
                </div>
                
                <div class="xs-12 registerInputs" style="color: #2C365D;"><h1>Registracija</h1></div>
                <div class="xs-12 registerInputs">
                    <div>
                        <input
                            v-model="register.firstName"
                            class="dform"
                            placeholder="Ime"
                        >
                    </div>
                    <div>
                        <input
                            v-model="register.lastName"
                            class="dform"
                            placeholder="Prezime"
                        >
                    </div>
                    <div>
                        <input
                            v-model="register.email"
                            class="dform"
                            placeholder="E-mail"
                            required
                        >
                    </div>
                    <div>
                        <input
                            v-model="register.password"
                            class="dform"
                            placeholder="Lozinka"
                            type="password"
                            required
                        >
                    </div>
                    <div>
                        <input
                            v-model="register.confirmPassword"
                            class="dform"
                            placeholder="Potvrdi lozinku"
                            type="password"
                            required
                        >
                    </div>
                    <div class="offset-xs-1 xs-10 dropdown">
                        <v-select 
                            class="style-chooser" 
                            label="naziv" 
                            :options="skole" 
                            :reduce="skola => skola._id" 
                            v-model="register.highSchool" 
                            placeholder="Škola"
                        >
                        </v-select>
                    </div>
                </div>

                <div class="offset-xs-1 xs-10 offset-m-3 m-6 offset-l-4 l-4">
                <div class="confirm-btn" @click="registerHandler()">Registriraj se</div>
                </div>
                <div class="register offset-xs-1 xs-10 offset-m-3 m-6 offset-l-4 l-4">
                <p>Registriran/a si?</p>
                <router-link tag="span" to="/login"><div>Prijavi se.</div></router-link>
                </div>
            </div>
        </div>
        <modal
          v-show="isModalVisible"
        >
          <div class="modal">
            <div>
                <div style="text-align: center;">
                    <div style="font-size: 4em; margin: 0.5em 0em 0.5em 0em; color: #FF5E3A;"><font-awesome-icon icon="check" /></div>
                    <div class="title">Uspješno ste se registrirali!</div>
                </div>
                <br>
                <div>

                    <button class="btn" @click="successfullyRegistered()">
                        OK
                    </button>
                </div>
            </div>
          </div>
        </modal>
	</div>
</template>

<script>
import axios from "axios"
import modal from "@/assets/scripts/modal/modal.vue"
require('@/assets/css/resetInputsStyle.css')

export default {
  name: 'Register',
  
	components: {
		modal,
  },
  
  data() {
    return {
        isModalVisible: false, //modal koji se otvori nakon registracije
        skole: [],
        register: {
            email: null,
            password: null,
            confirmPassword: null,
            firstName: null,
            lastName: null,
            highSchool: null,
            errors: [],
            status: null
        }
    };
  },

  mounted(){

    axios.get('/api/skole') // preuzima listu škola i stavlja u odabir
    .then(res => {
        if(res.status == 200){
            this.skole = res.data
        }
    })

  },

  methods: {
    validateEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
    },

    registerValidate() {
      
      this.register.errors = []

      if(!this.register.email) {
        this.register.errors.push("Email required.")
      } else if(!this.validateEmail(this.register.email)) {
        this.register.errors.push("Email must be in format example@domain.com")
      }

      if(!this.register.password) this.register.errors.push("Password required.")
      if(!this.register.confirmPassword) {
        this.register.errors.push("Confirm Password required.")
      } else if(this.register.password != this.register.confirmPassword) {
        this.register.errors.push("Passwords must match")
      }
      if(!this.register.firstName) this.register.errors.push("First name required.")
      if(!this.register.lastName) this.register.errors.push("Last name required.")
      if(!this.register.highSchool) this.register.errors.push("High school required.")

      if(!(this.register.errors && this.register.errors.length)){
        return true
      } else{
        return false
      }
      
    },

    registerHandler() {

      let valid = this.registerValidate();

      const registerUserData = {
        email: this.register.email,
        password: this.register.password,
        firstName: this.register.firstName,
        lastName: this.register.lastName,
        highSchool: this.register.highSchool,
        profilePic: "default" + (Math.floor(Math.random() * 2) + 1) + ".png"
      }

      if(valid) {
        axios.post("/api/register", registerUserData) //spremanje podataka novog korisnika i autentikacija toga korisnika
        .then(res => {
          if (res.data.auth == true) {
            this.$store.dispatch('authUser')

            this.isModalVisible = true
          } else {
            this.register.status = res.data.error
          }
        })
      }
		},
	
		successfullyRegistered() {
			this.isModalVisible = false

			this.$router.push({ //preusmjeravanje na početnu stranicu
				name: "Start"
			})
	
		}
  }
}
</script>

<style scoped>

.dform {
  min-width: 80%;
  font-family: 'PublicSans';
  font-size: 1.2em;
  caret-color: #FF5E3A;
  height: 2em;
  color: #F2F2F0;
  padding-left: 1em;
  margin: 0.5em 0em 0.5em 0em;
  background-color: #2C365D;
  border-radius: 0.5em !important;
	box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.2);
}
.dform::placeholder {
  color: #F2F2F0;
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

.registerErrors{
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
  box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.2);
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




.registerContainer{
  position: absolute;
  height: 92vh;
}

.registerForm{
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 1em;
}

.registerInputs{
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
    .registerForm {
        left: 50%;
        transform: translate(-50%, -50%);
        width: 60%;
    }
}

@media only screen and (min-width: 1070px) {
	.registerForm {
        width: 80%;
    }
  
    .info{
            display: block;
    }
    .registerContainer{
        left: 50%;
    }

}


.register{
  font-size: 0.9em;
  margin-top: 2em;
  font-weight: bold;
  color: #2C365D;
  text-align: center;
}

.register > span > div{
  font-size: 1.2em;
  border: 2px solid #2C365D;
  border-radius: 1em;
  padding: 0.5em;
  margin: 0em 2em 0em 2em;
  cursor: pointer;
}

.register > span > div:hover{
  color: #fd7d61;
  border: 2px solid #fd7d61;
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





.modal {
    width: 90%;
    background: #FFFFFF;
    border-radius: 1em;
	box-shadow: 0px 0px 10px 5px rgba(0, 0, 0, 0.2);
    overflow-x: auto;
    display: flex;
    flex-direction: column;
}

@media only screen and (min-width: 710px) {
	.modal {
		width: 70%;
	}
}

@media only screen and (min-width: 1070px) {
	.modal {
		width: 50%;
	}
}

@media only screen and (min-width: 1610px) {
	.modal {
		width: 30%;
	}
}


.title{
    text-transform: uppercase;
    font-weight: bold;
    font-size: 1.3em;
    color: #2c365d;
}

.btn {
	float: right;
	width: auto !important;
	color: #F2F2F0;
	font-weight: bold;
	text-transform: uppercase;
	cursor: pointer;
	background-color: #FF5E3A;
	padding: 1em;
}

.btn:active {
	opacity: 0.8;
}

.illustration > img{
  position: relative;
  top: 35%;
  transform: translateY(-50%);
  margin: 5em;
}

@media only screen and (min-width: 1310px) {
	.illustration > img{
    top: 25%;
    margin: 10em;
  }
}
</style>

