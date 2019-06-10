<template>
	<div class="register">
		<div class="registerErrors" style="padding: 1em 1em 0em 1em; color: #ff0055">
			<h4 v-for="(err, i) in register.errors" :key="i">
				{{ err }}
			</h4>
			<h4>{{register.status}}</h4>
		</div>

		<div style="padding: 0em 2em 2em 2em;">
			<div>
				<input
					v-model="register.email"
					placeholder="E-mail"
					required
				>
			</div>
			<div>
				<input
					v-model="register.password"
					placeholder="Password"
					type="password"
					required
				>
			</div>
			<div>
				<input
					v-model="register.confirmPassword"
					placeholder="Confirm Password"
					type="password"
					required
				>
			</div>
			<div>
				<input
					v-model="register.firstName"
					placeholder="First Name"
				>
			</div>
			<div>
				<input
					v-model="register.lastName"
					placeholder="Last Name"
				>
			</div>
			<button @click="registerHandler">
			Register
			</button>
		</div>

		<modal
			v-show="isModalVisible"
			@close="successfullyRegistered()"
		></modal>

	</div>
</template>

<script>
import axios from "axios"
import modal from "@/components/auth/modal.vue"

export default {
	name: 'Register',
	components: {
		modal,
	},
  data() {
    return {
			isModalVisible: false,
      register: {
        email: null,
        password: null,
        confirmPassword: null,
        firstName: null,
        lastName: null,
        errors: [],
        status: null
      }
    };
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
				profilePic: "default" + (Math.floor(Math.random() * 2) + 1) + ".png"
      }

      if(valid) {
        axios.post("/api/register", registerUserData)
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

			this.$router.push({
				name: "Start"
			})
	
		}
  }
}
</script>
