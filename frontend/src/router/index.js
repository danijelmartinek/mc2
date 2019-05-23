import Vue from "vue"
import Router from "vue-router"
Vue.use(Router)

import Start from "@/components/start/index.vue"
import MyPath from "@/components/path/index.vue"

import Case1 from "@/components/generatePath/Case1.vue"
import Case2 from "@/components/generatePath/Case2.vue"
import Case3 from "@/components/generatePath/Case3.vue"
import Case4 from "@/components/generatePath/Case4.vue"

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
    },
    {
      path: "/case/1",
      name: "CaseOne",
      component: Case1
    },
    {
      path: "/case/2",
      name: "CaseTwo",
      component: Case2
    },
    {
      path: "/case/3",
      name: "CaseThree",
      component: Case3
    },
    {
      path: "/case/4",
      name: "CaseFour",
      component: Case4
    }
  ]
});
