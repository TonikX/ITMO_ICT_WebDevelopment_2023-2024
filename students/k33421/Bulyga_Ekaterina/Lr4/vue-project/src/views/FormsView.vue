<script setup>
import {reactive, ref} from 'vue'
import {mdiBallotOutline, mdiAccount, mdiMail, mdiGithub} from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import CardBox from '@/components/CardBox.vue'
import FormCheckRadioGroup from '@/components/FormCheckRadioGroup.vue'
import FormFilePicker from '@/components/FormFilePicker.vue'
import FormField from '@/components/FormField.vue'
import FormControl from '@/components/FormControl.vue'
import BaseDivider from '@/components/BaseDivider.vue'
import BaseButton from '@/components/BaseButton.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import SectionTitle from '@/components/SectionTitle.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import NotificationBarInCard from '@/components/NotificationBarInCard.vue'
import router from "@/router";

</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiBallotOutline" title="Форма" main/>
      <CardBox form @submit.prevent="submit">
        <FormField label="Страховой агент">
          <FormControl v-model="form.name" :icon="mdiAccount" :readonly="true"/>
          <FormControl v-model="form.insureorganization" :readonly="true"/>
        </FormField>

        <FormField label="Юридическое лицо">
          <FormControl v-model="form.organization" :options="selectOrganization"/>
        </FormField>

        <FormField label="Физическое лицо">
          <FormControl v-model="form.client" :options="selectClient"/>
        </FormField>

        <template #footer>
          <BaseButtons>
            <BaseButton type="submit" color="info" label="Создать" @click="submit"/>
          </BaseButtons>
        </template>
      </CardBox>
    </SectionMain>

  </LayoutAuthenticated>
</template>

<script>
import axios from 'axios';
import {useMainStore} from "@/stores/main";
import router from "@/router";

const mainStore = useMainStore();

if (mainStore.token === '') {
  router.push({path: '/'});
}

const response = await axios.get('http://localhost:8000/api/organization/', {'headers': {'Authorization': `Token ${mainStore.token}`}});
const selectOrganization = response.data.map(item => item['fullname']);

const response2 = await axios.get(`http://localhost:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
const selectAgent = response2.data.map(item => item['firstname'] + ' ' + item['lastname']);

const response2_1 = await axios.get(`http://localhost:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
const selectInsureOrganizationId = response2_1.data.map(item => item['insureorganization']);

const response2_2 = await axios.get(`http://localhost:8000/api/insureorganization/${selectInsureOrganizationId}/`, {headers: {'Authorization': `Token ${mainStore.token}`}});
const selectInsureOrganization = response2_2.data['fullname'];

const response3 = await axios.get(`http://localhost:8000/api/individual`, {headers: {'Authorization': `Token ${mainStore.token}`}});
const selectClient = response3.data.map(item => item['firstname'] + ' ' + item['lastname']);

const form = reactive({
  name: selectAgent,
  insureorganization: selectInsureOrganization,
  organization: selectOrganization[0],
  client: selectClient[0],
})

const customElementsForm = reactive({
  checkbox: ['lorem'],
  radio: 'one',
  switch: ['one'],
  file: null
})

export default {
  methods: {
    async submit() {
      const resp2 = await axios.get(`http://localhost:8000/api/organization/?fullname=${form.organization}`, {'headers': {'Authorization': `Token ${mainStore.token}`}})
      const resp3 = await axios.get(`http://localhost:8000/api/individual/?firstname=${form.client.split(' ')[0]}&lastname=${form.client.split(' ')[1]}`, {'headers': {'Authorization': `Token ${mainStore.token}`}})

      const id = response2.data[0].id;
      console.log({
        'date_from': '2024-03-20',
        'date_to': '2024-10-20',
        'organization': resp2.data[0]['code'],
        'client': resp3.data[0]['id'],
        'agent': id
      });

      axios.post(`http://127.0.0.1:8000/api/contract/`, {
        'date_from': '2024-03-20',
        'date_to': '2024-10-20',
        'organization': resp2.data[0]['code'],
        'client': resp3.data[0]['id'],
        'agent': id
      }, {'headers': {'Authorization': `Token ${mainStore.token}`}});

      this.$router.go(0);
    },
  }
}


const formStatusWithHeader = ref(true)

const formStatusCurrent = ref(0)

const formStatusOptions = ['info', 'success', 'danger', 'warning']

const formStatusSubmit = () => {
  formStatusCurrent.value = formStatusOptions[formStatusCurrent.value + 1]
    ? formStatusCurrent.value + 1
    : 0
}
</script>
