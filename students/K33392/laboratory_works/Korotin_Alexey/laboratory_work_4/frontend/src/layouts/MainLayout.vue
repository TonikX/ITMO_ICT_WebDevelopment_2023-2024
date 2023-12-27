<template>
  <q-layout view="lHh Lpr lFf">
    <q-ajax-bar position="top" color="secondary" size="3px" />
    <q-header elevated class="row no-wrap">
      <q-toolbar>
        <q-toolbar-title shrink>
          Poultary farm
        </q-toolbar-title>
        <q-tabs class="row justfiy-between" indicator-color="secondary">
          <q-route-tab class="q-px-xs-xs q-px-sm-md" to="/facilities" label="Facilities" />
          <q-route-tab class="q-px-xs-xs q-px-sm-md" to="/cages" label="Cages" />
          <q-route-tab class="q-px-xs-xs q-px-sm-md" to="/chicken" label="Chicken" />
          <q-route-tab class="q-px-xs-xs q-px-sm-md" to="/staff" label="Staff" />
          <q-route-tab class="q-px-xs-xs q-px-sm-md" to="/statistics" label="Stats" />
        </q-tabs>
      </q-toolbar>
      <div class="row items-center q-mr-md">
        <q-btn color="secondary" text-color="primary" label="Logout" @click="onLogout" />
      </div>
    </q-header>
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<script>
import { mapActions, getActivePinia } from 'pinia';
import { useAuthStore } from '@/stores/authStore';
export default {
  methods: {
    ...mapActions(useAuthStore, ['logout']),

    onLogout() {
      this.logout();
      getActivePinia()._s.forEach((store) => store.$reset());
      this.$router.push("/auth/login");
    }
  }
}
</script>
