<script setup>
import { reactive } from 'vue'
import { useRouter } from 'vue-router'
import { mdiAccount, mdiAsterisk } from '@mdi/js'
import SectionFullScreen from '@/components/SectionFullScreen.vue'
import CardBox from '@/components/CardBox.vue'
import FormCheckRadio from '@/components/FormCheckRadio.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import LayoutGuest from '@/layouts/LayoutGuest.vue'
import {useMainStore} from "@/stores/main";
import router from "@/router";

if (localStorage.getItem('logout') === 'true') {
  localStorage.setItem('logout', 'false');
  router.go(0);
}
</script>

<template>
  <LayoutGuest>
    <SectionFullScreen v-slot="{ cardClass }" bg="purplePink">
      <CardBox :class="cardClass" is-form @submit.prevent="onLogin">
        <FormField label="Логин" help="Введите логин">
          <FormControl
            v-model="loginForm.username"
            :icon="mdiAccount"
            name="login"
            autocomplete="username"
            for="login"
          />
        </FormField>

        <FormField label="Пароль" help="Введите пароль">
          <FormControl
            v-model="loginForm.password"
            :icon="mdiAsterisk"
            type="password"
            name="password"
            for="password"
            autocomplete="current-password"
          />
        </FormField>

        <template #footer>
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Войти" @click="onLogin"/>
          </BaseButtons>
        </template>
      </CardBox>
    </SectionFullScreen>
  </LayoutGuest>
</template>

<script>
import axios from 'axios';
import {useMainStore} from "@/stores/main";

const mainStore = useMainStore()


export default {
  data() {
    return {
      loginForm: {
        username: '',
        password: '',
      },
      rules: {
        required: value => !!value || 'Required.'
      },
    };
  },
  methods: {
    async onLogin() {
        try {
          axios.post(`http://127.0.0.1:8000/auth/token/login/?username=${this.loginForm.username}&password=${this.loginForm.password}`, {'email': '', 'username': this.loginForm.username, 'password': this.loginForm.password})
          .then(response => {
            mainStore.setUser(response.data);
          })
          if (mainStore.userName !== '') {
            this.$router.push({name: 'tables'});
          }
        } catch (error) {
          console.error(error);
        }
      }
    }
};
</script>
