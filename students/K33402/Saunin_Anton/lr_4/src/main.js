import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router/router";
import piniaPluginPersistedState from "pinia-plugin-persistedstate";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const pinia = createPinia();
pinia.use(piniaPluginPersistedState);

const customDarkTheme = {
  dark: true,
  colors: {
    background: "#0B0C10",
    surface: "#1F2833",
    primary: "#3f51b5",
    secondary: "#03dac6",
    error: "#f44336",
    info: "#2196F3",
    success: "#4caf50",
    warning: "#fb8c00",
  },
};

const vuetify = createVuetify({
  components,
  directives,
  theme: {
    defaultTheme: "customDarkTheme",
    themes: {
      customDarkTheme,
    },
  },
});

// export default createVuetify({
//   theme: {
//     defaultTheme: "myCustomLightTheme",
//     themes: {
//       myCustomLightTheme,
//     },
//   },
// });
createApp(App).use(vuetify).use(pinia).use(router).mount("#app");
