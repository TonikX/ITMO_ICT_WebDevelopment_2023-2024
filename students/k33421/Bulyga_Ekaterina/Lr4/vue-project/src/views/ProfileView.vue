<script setup>
import { reactive } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiAccount, mdiMail, mdiAsterisk, mdiFormTextboxPassword, mdiGithub } from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import FormFilePicker from '@/components/FormFilePicker.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import UserCard from '@/components/UserCard.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import router from "@/router";
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiAccount" title="Мой профиль" main/>

      <UserCard class="mb-6" />

      <div class="center grid-cols-1:grid-cols-2 gap-6">
        <CardBox is-form @submit.prevent="updateProfile">
          <FormField label="Новый логин" help="Обязательное поле">
            <FormControl
              :icon="mdiAsterisk"
              v-model="form.username"
              name="username"
              type="username"
              autocomplete="username"
            />
          </FormField>

          <template #footer>
            <BaseButtons>
              <BaseButton color="info" type="submit" label="Сохранить" />
            </BaseButtons>
          </template>
        </CardBox>
      </div>
    </SectionMain>
  </LayoutAuthenticated>
</template>

<script>
import api from "../api";
import axios from 'axios';
import {useMainStore} from "@/stores/main";
import router from "@/router";
const mainStore = useMainStore();

if (mainStore.token === '') {
    router.push({path: '/'});
}

const response = await axios.get('http://localhost:8000/api/insureagent/', {headers: {'Authorization': `Token ${mainStore.token}`}});
const items = response.data;

export default {
  data() {
    return {
      userProfile: {},
      form: {
        username: mainStore.userName,
      },
    };
  },
  methods: {
    async updateProfile() {
      try {

        const payload = {
          username: this.form.username,
        };
        const resp = await api.get(`/insureagent/?username=${mainStore.userName}`, {headers: {"Authorization": `Token ${mainStore.token}`}});
        const id = resp.data[0].id;
        await api.patch(`/insureagent/${id}/`, payload, {headers: {"Authorization": `Token ${mainStore.token}`}});
        mainStore.userName = payload.username;
        this.$router.go(0);
      } catch (error) {
        console.error("There was an error updating the user's profile:", error);
      }
    },
  },
};
</script>
