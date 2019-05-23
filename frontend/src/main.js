import Vue from 'vue'
import App from './App.vue'
import router from './router'

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
