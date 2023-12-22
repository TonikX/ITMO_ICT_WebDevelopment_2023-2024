<template>

    <v-toolbar density="compact" color="teal-darken-4">

      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <div class="py-12 text-center">
      <v-btn v-if="auth">
        <button @click="$router.push(`/userpage/`)">Профиль</button>
      </v-btn>

      <v-btn>
        <button @click="$router.push(`/climbings/`)">Восхождения</button>
      </v-btn>

      <v-btn v-if="auth">
        <button @click="$router.push(`/clubs/`)">Клубы</button>
      </v-btn>

      <v-btn v-if="auth">
        <button @click="$router.push(`/mountains/`)">Горы</button>
      </v-btn>
      </div>

      <v-spacer></v-spacer>

      <v-btn v-if="!auth" @click="goLogin">Вход</v-btn>
      <v-btn v-if="!auth" @click="$router.push(`/registration/`)">Зарегистрироваться</v-btn>
      <v-btn v-else @click="logout">Выход</v-btn>
      <v-spacer></v-spacer>


    </v-toolbar>





</template>

<script>
//import Mountains from "@/components/Mountains.vue";

export default {
  name: 'HelloWorld',
  //components: {Mountains},
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed: {
    auth() {
      if (sessionStorage.getItem("token")) {
        return true
      }
    }
  },
  methods: {
    goLogin() {
      this.$router.push({name: "Login"})
    },
    logout() {
      sessionStorage.removeItem("token")
      window.location = '/'
    }
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
