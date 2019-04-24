import Vue from "vue"
import Router from "vue-router"
Vue.use(Router)

import Start from "@/components/start/index.vue"
import MyPath from "@/components/path/index.vue"

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "Start",
      component: Start
    },
    {
      path: "/mypath",
      name: "MyPath",
      component: MyPath
    }
  ]
});
