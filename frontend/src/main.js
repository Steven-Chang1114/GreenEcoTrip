import Vue from 'vue';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue';
import router from './router';
import store from './store';
import Fragment from 'vue-fragment'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret, faPlane, faBus, faSubway } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
 
library.add(faUserSecret)
library.add(faPlane)
library.add(faBus)
library.add(faSubway)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(Fragment.Plugin)

Vue.use(ElementUI);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
