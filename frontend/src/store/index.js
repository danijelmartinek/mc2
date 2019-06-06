import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        userAuthenticated: false,
        user: null,
        selectedOptions: {
            skolaId: "",
            fakultetId: "",
            smjerId: "",
            zanimanjeId: "",
            slucajOdabira: 0
        },
        routeHandler: false //handling forward and backward route change, to prevent errors
    },
    getters: {
        checkAuth(state) { return state.userAuthenticated }
    },
    mutations: {
        logoutUser(state) {
            axios.get("/api/logout")
            .then(res => {
                if(res.data.authCleared == true){
                    state.userAuthenticated = false
                    state.user = null
                }
            })
        }
    },
    actions: {
        resetData(context) {
            context.state.selectedOptions.skolaId = ''
			context.state.selectedOptions.fakultetId = ''
			context.state.selectedOptions.smjerId = ''
            context.state.selectedOptions.zanimanjeId = ''
            context.state.selectedOptions.slucajOdabira = 0
        },

        authUser(context) {
            if(!context.state.userAuthenticated){
                return new Promise(resolve => {
                    axios.get("/api/auth")
                    .then(res => {
                        if(res.data.auth == true){
                            context.state.userAuthenticated = true
                            context.state.user = res.data.userData
                        }
                        resolve(context.state.userAuthenticated)
                    }, error => {
                        resolve(error)
                    })
                })
            }
            else{
                return context.state.userAuthenticated
            }
        },
        permissionAllowed(context, permissionArray){
            if(context.state.userAuthenticated){
                return new Promise(resolve => {
                    resolve(permissionArray.includes(context.state.user.role.roleLevel))
                })
            }else{
                return new Promise(resolve => {
                    context.dispatch('authUser').then(auth => {
                        if(auth === true){
                            resolve(permissionArray.includes(context.state.user.role.roleLevel))
                        } else {
                            resolve(false)
                        }
                    })
                })
            }
        }
    }
})