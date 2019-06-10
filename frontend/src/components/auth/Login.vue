<template>
	<div class="login">
		<div class="loginErrors">
			<h4 v-for="(err, i) in login.errors" :key="i">
				{{ err }}
			</h4>
			<h4>{{login.status}}</h4>
		</div>

		<div style="padding: 0em 2em 2em 2em;">
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
					placeholder="Password"
					type="password"
					required
				>
			</div>
			<div class="confirm-btn" @click="loginHandler()">Login</div>
      <div><div class="confirm-btn" @click="logout()">Logout</div></div>
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

<style>
@import './resetInputsStyle.css';

.dform {
  font-family: 'PublicSans';
  font-size: 1.2em;
  caret-color: #FF5E3A;
  width: 30%;
  height: 2.5em;
  color: #F2F2F0;
  padding-left: 1em;
  margin: 0.5em;
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
	float: left;
	width: auto !important;
	color: #F2F2F0;
	font-weight: bold;
	text-transform: uppercase;
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
	float: left;
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
</style>

