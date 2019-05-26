import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        selectedOptions: {
            skolaId: "",
            fakultetId: "",
            smjerId: "",
            zanimanjeId: "",
            slucajOdabira: 0
        },
        routeHandler: false //handling forward and backward route change, to prevent errors
    },
    actions: {
        resetData(context) {
            context.state.selectedOptions.skolaId = ''
			context.state.selectedOptions.fakultetId = ''
			context.state.selectedOptions.smjerId = ''
            context.state.selectedOptions.zanimanjeId = ''
            context.state.selectedOptions.slucajOdabira = 0
        }
      }
})