# Vue part

## App.vue
```vue
<!--Запуск vue npm run dev-->
<template>
    <div id="app">
        <router-view/>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
        <link rel="stylesheet" href="https://cdn.bootcss.com/material-design-icons/3.0.1/iconfont/material-icons.css">
    </div>
</template>

<script>
    export default {
        name: 'App',
        created() {
            if (localStorage.getItem("auth_token")) {
                $.ajaxSetup({
                    headers: {'Authorization': "Token " + localStorage.getItem('auth_token')},
                });
            }
        }
    }
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
```

## src/router/index.js
```js
import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Login from '../components/Login'
import Disks from '../components/Disks'
import Games from '../components/Games'
import Sale from '../components/Sale'
import Admission from '../components/Admission'
import Sale_point from '../components/Sale_point'
import Admission_point from '../components/Admission_point'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login/',
      name: 'Login',
      component: Login
    },
    {
      path: '/disks/',
      name: 'Disks',
      component: Disks
    },
    {
      path: '/games/',
      name: 'Games',
      component: Games
    },
    {
      path: '/sale/',
      name: 'Sale',
      component: Sale
    },
    {
      path: '/admission/',
      name: 'Admission',
      component: Admission
    },
    {
      path: '/sale_point/',
      name: 'Sale_point',
      component: Sale_point
    },
    {
      path: '/admission_point/',
      name: 'Admission_point',
      component: Admission_point
    }
  ]
})

```

## src/components/Home.vue
```vue
<template>
    <mu-container>
        <mu-appbar
            style="width: 100.25vmax; height: 6.2vmax; margin-top: -11vh; margin-left: -13.9vh; text-align: left" color="#10df10">
            Home
            <mu-menu slot="left">
                <mu-button large fab value="menu" class="menu-buttons">
                    <mu-icon value="menu"></mu-icon>
                </mu-button>
                <mu-list slot="content">
                    <mu-list-item button @click="goDisks">
                        <mu-list-item-title>Disks</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goGames">
                        <mu-list-item-title>Games</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale" v-if="auth">
                        <mu-list-item-title>Sale</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goAdmission" v-if="auth">
                        <mu-list-item-title>Admission</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goSale_point" v-if="auth">
                        <mu-list-item-title>Sale_point</mu-list-item-title>
                    </mu-list-item>
                    <mu-list-item button @click="goAdmission_point" v-if="auth">
                        <mu-list-item-title>Admission_point</mu-list-item-title>
                    </mu-list-item>
                </mu-list>
            </mu-menu>
            <mu-button large fab slot="right" v-if="!auth" @click="goLogin" class="menu-buttons">LOGIN</mu-button>
            <mu-button large fab slot="right" v-else @click="logout" class="menu-buttons">LOGOUT</mu-button>
        </mu-appbar>
        <mu-container style="font-size: 24px">
            <br>
            Registered users can view all tables and edit the following: Disks, Games, Sale, Login.
            <br>
            Not registered users can only view tables: Disks, Games.
            <br><br><br>
            Зарегистрированные пользователи могут просматривать все таблицы и редактировать следующие: Disks, Games,
            Sale, Admission.
            <br>
            Не зарегистрированные пользователи могут только просматривать таблицы: Disks, Games.
        </mu-container>
    </mu-container>
</template>

<script>
    export default {
        name: "Home",
        computed: {
            auth() {
                if (sessionStorage.getItem("auth_token")) {
                    return true
                }
            }
        },
        methods: {
            goLogin() {
                this.$router.push({name: "Login"})
            },
            logout() {
                sessionStorage.removeItem("auth_token");
                window.location = "/" //костыль
            },
            goDisks() {
                this.$router.push({name: "Disks"});
            },
            goGames() {
                this.$router.push({name: "Games"});
            },
            goSale() {
                this.$router.push({name: "Sale"});
            },
            goAdmission() {
                this.$router.push({name: "Admission"});
            },
            goSale_point() {
                this.$router.push({name: "Sale_point"});
            },
            goAdmission_point() {
                this.$router.push({name: "Admission_point"});
            },
        },
    }
</script>

<style scoped>
    .menu-buttons {
        box-shadow: 0 0 15px white;
        background-color: #10df10;
        margin-top: 1vh;
    }
</style>
```

## src/config/index.js
```js
'use strict'
// Template version: 1.3.1
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path')

module.exports = {
  dev: {

    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {},

    // Various Dev Server settings
    host: 'localhost', // can be overwritten by process.env.HOST
    port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    autoOpenBrowser: false,
    errorOverlay: true,
    notifyOnErrors: true,
    poll: false, // https://webpack.js.org/configuration/dev-server/#devserver-watchoptions-

    
    /**
     * Source Maps
     */

    // https://webpack.js.org/configuration/devtool/#development
    devtool: 'cheap-module-eval-source-map',

    // If you have problems debugging vue-files in devtools,
    // set this to false - it *may* help
    // https://vue-loader.vuejs.org/en/options.html#cachebusting
    cacheBusting: true,

    cssSourceMap: true
  },

  build: {
    // Template for index.html
    index: path.resolve(__dirname, '../dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',

    /**
     * Source Maps
     */

    productionSourceMap: true,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: '#source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report
  }
}

```