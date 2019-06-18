
import {store} from "@/store/index.js"
import router from "@/router/index.js"

export default function auth(to, from, next) { //provjera, ako je postavljena na određeni URL, gleda je li korisnik prijavljen
    store.dispatch("authUser").then(() => {
        if (!store.state.userAuthenticated) {
            router.push({name: 'Start'})
        }
        next()
    })
  }