<script setup>
import {computed, ref} from 'vue'
import {useMainStore} from '@/stores/main'
import {mdiEye, mdiTableBorder, mdiTrashCan} from '@mdi/js'
import CardBoxModal from '@/components/CardBoxModal.vue'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import BaseLevel from '@/components/BaseLevel.vue'
import BaseButtons from '@/components/BaseButtons.vue'
import BaseButton from '@/components/BaseButton.vue'
import SectionTitleLineWithButton from "@/components/SectionTitleLineWithButton.vue";
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
import router from '../router';
import {computed, ref} from "vue";


const mainStore = useMainStore();

if (mainStore.token === '') {
  router.push({path: '/'});
}

const response = await axios.get('http://localhost:8000/api/individual/', {headers: {"Authorization": `Token ${mainStore.token}`}});
const items = response.data;

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

const checkedRows = ref([])

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


</script>

<template>
  <SectionTitleTable title="Физические лица" main/>
  <table>
    <thead>
    <tr>
      <th>Имя</th>
      <th>Фамилия</th>
      <th>Отчество</th>
      <th>Паспорт</th>
      <th>Телефон</th>
      <th>Адрес</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="client in itemsPaginated">
      <td data-label="Name">
        {{ client.firstname }}
      </td>
      <td data-label="Surname">
        {{ client.lastname }}
      </td>
      <td data-label="Patronymic">
        {{ client.patronymic }}
      </td>
      <td data-label="Passport">
        {{ client.passport }}
      </td>
      <td data-label="Phone">
        {{ client.phone }}
      </td>
      <td data-label="Address">
        {{ client.address }}
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
