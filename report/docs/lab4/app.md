## App.vue

В представлении приложения у меня реализован navbar, который обновляется при регистрации/выходе из аккаунта. Для отслеживания используется библиотека vuex.

``` js title="App.vue"
<template>
  <div id="app">
    <CNavbar expand="lg" color-scheme="dark" class="bg-dark">
      <CContainer fluid>

        <router-link :to="{ name: 'EventHome' }"><CNavbarBrand>Мероприятия</CNavbarBrand></router-link>

        <CNavbarToggler aria-label="Toggle navigation" aria-expanded={visible} @click="visible = !visible"/>
        <CCollapse class="navbar-collapse" :visible="visible">
          <CNavbarNav>
            <div v-if="$store.state.isAuthenticated">
              <CNavItem>
                <router-link :to="{ name: 'UserPage' }"><CNavLink>Мой кабинет</CNavLink></router-link>
              </CNavItem>
              
              <CNavItem>
                <CNavLink @click="logout">Выйти</CNavLink>
              </CNavItem>
            </div>
            <div v-else>
            <CDropdown variant="nav-item" :popper="false">
              <CDropdownToggle color="secondary">Авторизация</CDropdownToggle>
              <CDropdownMenu>
                <router-link :to="{ name: 'login' }"><CDropdownItem class="dropdown-item">Вход</CDropdownItem></router-link>
                <router-link :to="{ name: 'registration' }"><CDropdownItem class="dropdown-item">Регистрация</CDropdownItem></router-link>
              </CDropdownMenu>
            </CDropdown>
            </div>
          </CNavbarNav>
        </CCollapse>
      </CContainer>
    </CNavbar>
    <router-view />

  </div>
</template>

<script>
import { reactive } from 'vue';

import {
  CNavbar,
  CContainer,
  CNavbarBrand,
  CNavbarToggler,
  CCollapse,
  CNavbarNav,
  CNavItem,
  CNavLink,
  CDropdown,
  CDropdownToggle,
  CDropdownMenu,
  CDropdownItem
} from '@coreui/vue';

export default {
  name: 'App',

  setup() {
    const authState = reactive({
      isAuthenticated: !!sessionStorage.getItem('token'),
    });

    return { authState };
  },

  components: {
    CNavbar,
    CContainer,
    CNavbarBrand,
    CNavbarToggler,
    CCollapse,
    CNavbarNav,
    CNavItem,
    CNavLink,
    CDropdown,
    CDropdownToggle,
    CDropdownMenu,
    CDropdownItem
  },
  
  methods: {
    logout() {
      sessionStorage.removeItem('token');
      sessionStorage.removeItem('username');
      sessionStorage.removeItem('password');
      sessionStorage.removeItem('user_id');
      this.$store.commit('setAuthenticated', false);
      this.$router.push({ name: 'login' });
    },
  },

};
  
</script>

<style>

</style>
```