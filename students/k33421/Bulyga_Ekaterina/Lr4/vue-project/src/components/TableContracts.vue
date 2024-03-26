<script setup>
import {computed, ref} from 'vue'
import {useMainStore} from '@/stores/main'
import {mdiEye, mdiTrashCan} from '@mdi/js'
import CardBoxModal from '@/components/CardBoxModal.vue'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import axios from "axios";
import FormControl from "@/components/FormControl.vue";
import SectionTitleTable from "@/components/SectionTitleTable.vue";
// import UserAvatar from '@/components/UserAvatar.vue'
const mainStore = useMainStore()

defineProps({
  checkable: Boolean
})

const isModalActive = ref(false)

const isModalDangerActive = ref(false)
</script>

<script>
import axios from 'axios';
import {useMainStore} from "@/stores/main";
import router from "@/router";
import {ref} from "vue";

const mainStore = useMainStore();

if (mainStore.token === '') {
  mainStore.token = localStorage.getItem('auth_token');
  router.push({path: '/'});
}

const response0 = await axios.get(`http://localhost:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
var userProfile = response0.data[0];
var firstname = userProfile.firstname;
var lastname = userProfile.lastname;

const response = await axios.get(`http://localhost:8000/api/contract/?agent=${userProfile.id}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
const items0 = response.data;

let items = [];
for (var i in items0) {
  var resp = await axios.get(`http://localhost:8000/api/organization/${items0[i].organization}/`, {headers: {'Authorization': `Token ${mainStore.token}`}});
  var org = resp.data;

  var resp = await axios.get(`http://localhost:8000/api/individual/${items0[i].client}/`, {headers: {'Authorization': `Token ${mainStore.token}`}});
  var cli = resp.data;

  var obj = {
    date_from: items0[i].date_from,
    date_to: items0[i].date_to,
    organization: `${org.fullname}` != 'default' ? `${org.fullname}` : '',
    client: `${cli.firstname} ${cli.lastname}` != 'default default' ? `${cli.firstname} ${cli.lastname}` : '',
    agent: `${firstname} ${lastname}`
  };

  items.push(obj);
}

const perPage = ref(5)

const numPages = computed(() => Math.ceil(items.length / perPage.value))

const currentPage = ref(0)

const currentPageHuman = computed(() => currentPage.value + 1)

const pagesList = computed(() => {
  const pagesList = []

  for (let i = 0; i < numPages.value; i++) {
    pagesList.push(i)
  }

  return pagesList
})

const itemsPaginated = computed(() =>
  items.slice(perPage.value * currentPage.value, perPage.value * (currentPage.value + 1))
)

const checkedRows = ref([]);

const remove = (arr, cb) => {
  const newArr = []

  arr.forEach((item) => {
    if (!cb(item)) {
      newArr.push(item)
    }
  })

  return newArr
}

const checked = (isChecked, client) => {
  if (isChecked) {
    checkedRows.value.push(client)
  } else {
    checkedRows.value = remove(checkedRows.value, (row) => row.id === client.id)
  }
}

export default {
  methods: {
    async onSubmit(item) {
      const clientName = item.client === '' ? 'default default' : item.client;
      const orgName = item.organization === '' ? 'default' : item.organization;
      const resp0_1 = await axios.get(`http://127.0.0.1:8000/api/organization/?fullname=${orgName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
      const resp0_2 = await axios.get(`http://127.0.0.1:8000/api/individual/?firstname=${clientName.split(' ')[0]}&lastname=${clientName.split(' ')[1]}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
      const resp0_3 = await axios.get(`http://127.0.0.1:8000/api/insureagent/?username=${mainStore.userName}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
      const resp = await axios.get(`http://127.0.0.1:8000/api/contract/?date_from=${item.date_from}&date_to=${item.date_to}&organization=${resp0_1.data[0].code}&client=${resp0_2.data[0].id}&agent=${resp0_3.data[0].id}`, {headers: {'Authorization': `Token ${mainStore.token}`}});
      await axios.delete(`http://127.0.0.1:8000/api/contract/${resp.data[0].id}/`, {headers: {'Authorization': `Token ${mainStore.token}`}});
      this.$router.go(0);
    }
  }
}
</script>

<template>
  <CardBoxModal v-model="isModalActive" title="Sample modal">
    <p>Lorem ipsum dolor sit amet <b>adipiscing elit</b></p>
    <p>This is sample modal</p>
  </CardBoxModal>

  <CardBoxModal v-model="isModalDangerActive" title="Please confirm" button="danger" has-cancel>
    <p>Вы уверенны, что хотите удалить?</p>
  </CardBoxModal>

  <SectionTitleTable title="Договоры" main/>
  <table>
    <thead>
    <tr>
      <th>Дата начала</th>
      <th>Дата окончания</th>
      <th>Юридическое лицо</th>
      <th>Физическое лицо</th>
      <th>Страховой агент</th>
      <th/>
    </tr>
    </thead>
    <tbody>
    <tr v-for="item in itemsPaginated">
      <td data-label="Date from">
        {{ item.date_from }}
      </td>
      <td data-label="Date to">
        {{ item.date_to }}
      </td>
      <td data-label="Organization">
        {{ item.organization }}
      </td>
      <td data-label="Client">
        {{ item.client }}
      </td>
      <td data-label="Agent">
        {{ item.agent }}
      </td>

      <td class="before:hidden lg:w-1 whitespace-nowrap">
        <BaseButtons type="justify-start lg:justify-end" no-wrap>
<!--          <BaseButton color="info" :icon="mdiEye" small @click="isModalActive = true"/>-->
          <BaseButton color="danger" :icon="mdiTrashCan" small type="submit" :is="item" @click="onSubmit(item)"/>
        </BaseButtons>
      </td>
    </tr>
    </tbody>
  </table>
  <div class="p-3 lg:px-6 border-t border-gray-100 dark:border-slate-800">
    <BaseLevel>
      <BaseButtons>
        <BaseButton
          v-for="page in pagesList"
          :key="page"
          :active="page === currentPage"
          :label="page + 1"
          :color="page === currentPage ? 'lightDark' : 'whiteDark'"
          small
          @click="currentPage = page"
        />
      </BaseButtons>
      <small>Page {{ currentPageHuman }} of {{ numPages }}</small>
    </BaseLevel>
  </div>
</template>

