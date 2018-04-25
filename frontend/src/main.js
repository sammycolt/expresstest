// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import store from './store'
import router from './router'
import Router from 'vue-router'
import {Tabs} from 'vue-tabs-component'
// import { sync } from 'vuex-router-sync'

// var jwtDecode = require('jwt-decode')
Vue.use(Router)
Vue.use(Tabs)
Vue.config.productionTip = false
// sync(store, router)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
