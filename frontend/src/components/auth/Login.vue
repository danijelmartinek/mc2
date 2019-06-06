<template>
	<div class="login">
		<div class="loginErrors" style="padding: 2em 2em 0em 2em; color: #ff0055">
			<h4 v-for="(err, i) in login.errors" :key="i">
				{{ err }}
			</h4>
			<h4>{{login.status}}</h4>
		</div>

		<div style="padding: 0em 2em 2em 2em;">
			<div>
				<input
					v-model="login.email"
					placeholder="E-mail"
					required
				>
			</div>
			<div>
				<input
					v-model="login.password"
					placeholder="Password"
					type="password"
					required
				>
			</div>
			<button @click="loginHandler">
			Login
			</button>
      <br><br><br>
      <div><button @click="logout()">
			Logout
			</button></div>
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
