<script setup>
import { computed, ref } from 'vue'
import { useMainStore } from '@/stores/main'
import { mdiCheckDecagram } from '@mdi/js'
import BaseLevel from '@/components/BaseLevel.vue'
import UserAvatarCurrentUser from '@/components/UserAvatarCurrentUser.vue'
import CardBox from '@/components/CardBox.vue'
import FormCheckRadio from '@/components/FormCheckRadio.vue'
import PillTag from '@/components/PillTag.vue'

const mainStore = useMainStore();

const userSwitchVal = ref(false)
</script>

<template>
  <CardBox>
    <BaseLevel type="justify-around lg:justify-center">
      <UserAvatarCurrentUser class="lg:mx-12" />
      <div class="space-y-3 text-center md:text-left lg:mx-12">
        <h1 class="text-2xl">
          Привет, <b>{{ fullName }}</b>!
        </h1>
<!--        <p>Last login <b>12 mins ago</b> from <b>127.0.0.1</b></p>-->
        <div class="flex justify-center md:block">
          <PillTag label="Подтвержден" color="info" :icon="mdiCheckDecagram" />
        </div>
      </div>
    </BaseLevel>
  </CardBox>
</template>

<script>
import api from "../api";
import axios from 'axios';
import {useMainStore} from "@/stores/main";

export default {
  data() {
    return {
      userProfile: {},
      form: {
        firstName: '',
        lastName: '',
      },
    };
  },
  computed: {
    fullName() {
      return `${this.form.firstname} ${this.form.lastname}`;
    },
  },
  async created() {
    await this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        const mainStore = useMainStore();
        const response = await axios.get(`http://localhost:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
        this.userProfile = response.data;
        this.form.firstname = this.userProfile[0].firstname;
        this.form.lastname = this.userProfile[0].lastname;
      } catch (error) {
        console.error("There was an error fetching the user's profile:", error);
      }
    },
    async updateProfile() {
      try {
        const payload = {
          first_name: this.form.firstname,
          last_name: this.form.lastname,
        };
        await api.patch('/auth/users/me/', payload);
        this.fetchUserProfile();
      } catch (error) {
        console.error("There was an error updating the user's profile:", error);
      }
    },
  },
};
</script>
