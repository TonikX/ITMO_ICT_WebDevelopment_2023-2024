import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false

Vue.prototype.$websiteURL = 'http://localhost:8000';
Vue.prototype.$totalPages = 9;

const goTo = function (route) {
  this.$router.push(route).catch(err => {
    if (err.name !== 'NavigationDuplicated') {
      throw err;
    }
  });
}

Vue.prototype.$goTo = goTo;

const formatDate = function(inputDate) {
  if (!inputDate) return '';

  const [year, month, day] = inputDate.split('-');
  return `${day}.${month}.${year}`;
};

Vue.prototype.$formatDate = formatDate;

/* eslint-disable no-new */
new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
