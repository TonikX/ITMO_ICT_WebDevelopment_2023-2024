<script setup>
const props = defineProps({
  consignments: Array,
  fetching: Boolean,
})

const status = {'a': 'active', 'c':'cancelled', 's':'signed'}
const terms = {'ap': 'afterpay', 'pp': 'prepay'}

</script>

<template>
  <div class="text-center" v-if="fetching">
    <v-progress-circular
      indeterminate
      color="white"
      style="margin-bottom: 10%"
    ></v-progress-circular>
  </div>
  <v-table density="compact" v-else>
    <thead>
      <tr>
        <th class="text-left">
          Id
        </th>
        <th class="text-left">
          Terms
        </th>
        <th class="text-left">
          Status
        </th>
        <th class="text-left">
          Opening Date
        </th>
        <th class="text-left">
          Delivery Date
        </th>
      </tr>
    </thead>
    <tbody>
      <tr
        v-for="item in consignments"
        :key="item.id"
      >
        <td>{{ item.id }}</td>
        <td>{{ terms[item.terms] }}</td>
        <td>{{ status[item.status] }}</td>
        <td>{{ item.opening_date }}</td>
        <td>{{ item.delivery_date }}</td>
      </tr>
    </tbody>
  </v-table>
</template>
