<template>
  <div id="app">
    <CNavbar expand="lg" color-scheme="dark" class="bg-dark">
      <CContainer fluid>

        <router-link :to="{ name: 'EventHome' }"><CNavbarBrand>Мероприятия</CNavbarBrand></router-link>

        <CNavbarToggler aria-label="Toggle navigation" aria-expanded={visible} @click="visible = !visible"/>
        <CCollapse class="navbar-collapse" :visible="visible">
          <CNavbarNav>

            <CNavItem>
              <router-link :to="{ name: 'UserPage' }"><CNavLink>Мой кабинет</CNavLink></router-link>
            </CNavItem>

            <CDropdown variant="nav-item" :popper="false">
              <CDropdownToggle color="secondary">Авторизация</CDropdownToggle>
              <CDropdownMenu>
                <router-link :to="{ name: 'login' }"><CDropdownItem class="dropdown-item">Вход</CDropdownItem></router-link>
                <router-link :to="{ name: 'registration' }"><CDropdownItem class="dropdown-item">Регистрация</CDropdownItem></router-link>
              </CDropdownMenu>
            </CDropdown>

          </CNavbarNav>
        </CCollapse>
      </CContainer>
    </CNavbar>
    <router-view />

  </div>
</template>

<script>
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
  }
};
</script>

<style>

</style>
