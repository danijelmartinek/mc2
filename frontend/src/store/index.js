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
            fakultet: "",
            fakultetId: "",
            smjerId: "",
            zanimanjeId: "",
            slucajOdabira: 0
        },
        pathOptions: {
            skole: [],
            fakulteti: [],
            zanimanja: []
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

        getPathOptions(context) {
            axios.get('/api/skole')
            .then(res => {
                if(res.status == 200){
                    context.state.pathOptions.skole = res.data
                }
            })

            axios.get('/api/fakulteti')
            .then(res => {
                if(res.status == 200){
                    context.state.pathOptions.fakulteti = res.data
                }
            })

            axios.get('/api/zanimanja')
            .then(res => {
                if(res.status == 200){
                    context.state.pathOptions.zanimanja = res.data
                }
            })

        },

        authUser(context) {
            if(!context.state.userAuthenticated){
                return new Promise(resolve => {
                    axios.get("/api/auth")
                    .then(res => {
                        if(res.data.auth == true){
                            context.state.userAuthenticated = true
                            context.state.user = res.data.userData
                            
                            if(context.state.user.highSchool){
                                context.state.selectedOptions.skolaId = context.state.user.highSchool
                            }
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