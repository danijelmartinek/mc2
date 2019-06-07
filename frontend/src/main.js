import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vSelect from 'vue-select'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faCheck, faSave } from '@fortawesome/free-solid-svg-icons'
import { faSave as farSave } from '@fortawesome/free-regular-svg-icons'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCheck, faSave, farSave)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.component('v-select', vSelect)
import 'vue-select/dist/vue-select.css';

require('./assets/css/gridView.css')

import Vue2TouchEvents from 'vue2-touch-events'
 
Vue.use(Vue2TouchEvents, {
  touchClass: '',
  tapTolerance: 100,
  swipeTolerance: 100,
  longTapTimeInterval: 400
})

import {store} from './store/index.js'
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
