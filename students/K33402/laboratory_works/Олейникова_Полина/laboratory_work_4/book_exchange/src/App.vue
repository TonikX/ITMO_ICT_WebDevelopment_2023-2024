<template>
  <q-layout view="hHh Lpr lff">
    <q-header>
      <q-toolbar>
        <q-btn
          v-if="user"
          flat
          round
          dense
          icon="menu"
          @click="drawer = !drawer"
        />
        <q-toolbar-title>Exchange Books</q-toolbar-title>
        <q-btn-dropdown
          v-if="user"
          color="primary"
          unelevated
          :label="user.username"
        >
          <q-list>
            <q-item
              v-close-popup
              clickable
              to="/profile"
            >
              <q-item-section>
                <q-item-label>Profile</q-item-label>
              </q-item-section>
            </q-item>

            <q-item
              v-close-popup
              clickable
              @click="logout"
            >
              <q-item-section>
                <q-item-label>Logout</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-btn-dropdown>
        <q-btn
          v-else
          unelevated
          @click="changeDarkMode"
        >
          <q-icon
            :name="!$q.dark.isActive ? 'light_mode' : 'dark_mode'"
            color="white"
          />
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-if="user"
      v-model="drawer"
      show-if-above
      :width="250"
      :breakpoint="500"
      bordered
    >
      <q-scroll-area class="fit">
        <q-list>
          <q-item
            v-for="(menuItem, index) in menuList"
            :key="index"
            v-ripple
            clickable
            :to="menuItem.link"
            :active="currentRouteName === menuItem.link"
          >
            <q-item-section avatar>
              <q-icon
                :name="menuItem.icon"
                :color="currentRouteName === menuItem.link ? 'primary' : 'grey'"
              />
            </q-item-section>
            <q-item-section>
              {{ menuItem.label }}
            </q-item-section>
          </q-item>
          <q-separator />
          <q-item
            clickable
            @click="changeDarkMode"
          >
            <q-item-section avatar>
              <q-icon
                :name="!$q.dark.isActive ? 'light_mode' : 'dark_mode'"
                color="grey"
              />
            </q-item-section>
            <q-item-section>
              {{ !$q.dark.isActive ? 'Light' : 'Dark' }}
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useQuasar } from 'quasar'
import { useUserStore } from './stores/user'
import { storeToRefs } from 'pinia'

const menuList = [
  {
    icon: 'book',
    label: 'Books',
    link: '/'
  },
  {
    icon: 'auto_stories',
    label: 'My boooks',
    link: '/books/my'
  },
  {
    icon: 'change_circle',
    label: 'Requests for my books',
    link: '/requests/from'
  },
  {
    icon: 'favorite',
    label: 'My exchange requests',
    link: '/requests/to'
  }
]

export default defineComponent({
  name: 'App',
  setup() {
    const userStore = useUserStore()
    const { user } = storeToRefs(userStore)

    const route = useRoute()
    const router = useRouter()
    const currentRouteName = computed(() => route.path)

    const $q = useQuasar()
    const changeDarkMode = () => {
      $q.dark.toggle()
      localStorage.setItem('dark', $q.dark.isActive.toString())
    }

    onMounted(() => {
      $q.dark.set(localStorage.getItem('dark') === 'true')
      if (localStorage.getItem('Token')) {
        userStore.token = localStorage.getItem('Token')
        userStore.getProfile()
      }
    })

    const logout = async () => {
      const res = await userStore.logout()
      if (res) {
        router.push({ path: '/login' })
      }
    }

    return {
      drawer: ref(false),
      user,
      menuList,
      currentRouteName,
      changeDarkMode,
      logout
    }
  }
})
</script>
