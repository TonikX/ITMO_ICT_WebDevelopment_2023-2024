<script setup>
import {mdiMonitorCellphone, mdiTableBorder, mdiTableOff, mdiGithub} from '@mdi/js'
import SectionMain from '@/components/SectionMain.vue'
import NotificationBar from '@/components/NotificationBar.vue'
import TableSampleClients from '@/components/TableSampleClients.vue'
import TableOrganizations from '@/components/TableOrganizations.vue'
import TableContracts from '@/components/TableContracts.vue'
import CardBox from '@/components/CardBox.vue'
import LayoutAuthenticated from '@/layouts/LayoutAuthenticated.vue'
import SectionTitleLineWithButton from '@/components/SectionTitleLineWithButton.vue'
import CardBoxComponentEmpty from '@/components/CardBoxComponentEmpty.vue'
import router from "@/router";
import {useMainStore} from "@/stores/main";

const mainStore = useMainStore();

if (mainStore.token === '') {
  router.push({path: '/'});
}
</script>

<template>
  <LayoutAuthenticated>
    <SectionMain>
      <SectionTitleLineWithButton :icon="mdiTableBorder" title="Таблицы" main/>
      <CardBox class="mb-6" has-table>
        <TableSampleClients checkable/>
      </CardBox>
      <CardBox class="mb-6" has-table>
        <TableOrganizations checkable/>
      </CardBox>
      <CardBox class="mb-6" has-table>
        <TableContracts checkable/>
      </CardBox>
    </SectionMain>
  </LayoutAuthenticated>
</template>
