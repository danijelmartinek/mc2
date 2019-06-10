<template>
	<div id="login" class="drow">
    <div class="dcol xs-12 ml-6 loginContainer">
      <div class="loginForm">
        <div class="loginErrors">
          <h4 v-for="(err, i) in login.errors" :key="i">
            {{ err }}
          </h4>
          <h4>{{login.status}}</h4>
        </div>

        <div class="xs-12 loginInputs">
          <div>
            <input
              v-model="login.email"
              class="dform"
              placeholder="E-mail"
              required
            >
          </div>
          <div>
            <input
              v-model="login.password"
              class="dform"
              placeholder="Lozinka"
              type="password"
              required
            >
          </div>
        </div>
        <div class="offset-xs-1 xs-10 offset-m-3 m-6 offset-l-4 l-4">
          <div class="confirm-btn" @click="loginHandler()">Prijavi se</div>
          <div class="confirm-btn" @click="logout()">Logout</div>
        </div>
        <div class="register offset-xs-1 xs-10 offset-m-3 m-6 offset-l-4 l-4">
          <p>Nisi registriran/a?</p>
         <router-link tag="span" to="/register"><div>Registriraj se.</div></router-link>
        </div>
      </div>
    </div>

    <div class="dcol xs-12 ml-6 info">
    </div>
	</div>
</template>

<script>
import axios from "axios"

export default {
  name: 'login',
  data() {
    return {
      login: {
        email: null,
        password: null,
        errors: [],
        status: null
      }
    }
  },
  methods:{

    validateEmail(email) {
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
    },

    loginValidate() {
      
      this.login.errors = []

      if(!this.login.email) {
        this.login.errors.push("Email required.")
      } else if(!this.validateEmail(this.login.email)) {
        this.login.errors.push("Email must be in format example@domain.com")
      }
      if(!this.login.password) this.login.errors.push("Password required.")

      if(!(this.login.errors && this.login.errors.length)){
        return true
      } else{
        return false
      }
      
    },
    loginHandler() {
      let valid = this.loginValidate()

      const loginUserData = {
        email: this.login.email,
        password: this.login.password,
      }

      if(valid) {
        axios.post("/api/login", loginUserData)
        .then(res => {
          if (res.data.auth == true) {
            this.$store.dispatch('authUser')
            this.$router.push({
              name: "Start"
            })
          } else {
            this.login.status = res.data.error
          }
        })
      }
    },

    logout(){
      this.$store.commit('logoutUser')
    }
  }
}
</script>

<style scoped>
@import './resetInputsStyle.css';

.dform {
  min-width: 80%;
  font-family: 'PublicSans';
  font-size: 1.2em;
  caret-color: #FF5E3A;
  height: 2.5em;
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

.loginErrors{
  color: #FF5E3A;
  padding: 1em 0em 0em 3em;
}

/**
 * Reset button styles.
 * It takes a bit of work to achieve a neutral look.
 */
button {
  padding: 0;
  border: none;
  font: inherit;
  color: inherit;
  background-color: transparent;
  /* show a hand cursor on hover; some argue that we
  should keep the default arrow cursor for buttons */
  cursor: pointer;
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




.loginContainer{
  position: absolute;
  height: 92vh;
}

.loginForm{
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 100%;
  padding: 1em;
}

.loginInputs{
  text-align: center;
}

.info{
  display: none;
  position: absolute;
  left: 50%;
  height: 92vh;
  width: 50%;
  background-color: #2C365D;
}

@media only screen and (min-width: 710px) {
	.loginForm {
    left: 50%;
    transform: translate(-50%, -50%);
		width: 60%;
  }
}

@media only screen and (min-width: 1070px) {
	.loginForm {
		width: 80%;
  }
  
  .info{
    display: block;
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
</style>

