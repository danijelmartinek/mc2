import Vue from "vue"
import Router from "vue-router"
Vue.use(Router)

import Start from "@/components/start/index.vue"
import MyPath from "@/components/path/index.vue"

import Profile from "@/components/profile/index.vue"

import Case1 from "@/components/generatePath/Case1.vue"
import Case2 from "@/components/generatePath/Case2.vue"
import Case3 from "@/components/generatePath/Case3.vue"
import Case4 from "@/components/generatePath/Case4.vue"

import Register from "@/components/auth/Register.vue"
import Login from "@/components/auth/Login.vue"

import authMiddleware from '@/middleware/auth.js';
//import authRoleMiddleware from '@/middleware/authWRoleCheck.js';

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
    },
    {
      path: "/register",
      name: "Register",
      component: Register,
    },
    {
      path: "/login",
      name: "Login",
      component: Login,
    },
    {
      path: "/profile",
      name: "Profile",
      component: Profile,
      beforeEnter: authMiddleware
    }
  ]
});
